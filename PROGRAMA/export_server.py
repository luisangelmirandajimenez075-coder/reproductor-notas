from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import subprocess
import antlr4

WORKSPACE = Path(__file__).resolve().parent.parent
MAX_UPLOAD_BYTES = 100 * 1024 * 1024


class ExportHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(WORKSPACE), **kwargs)

    def end_headers(self):
        origin = self.headers.get("Origin", "")
        if origin.startswith("http://127.0.0.1:") or origin.startswith("http://localhost:"):
            self.send_header("Access-Control-Allow-Origin", origin)
            self.send_header("Vary", "Origin")
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header("Access-Control-Max-Age", "600")
        self.end_headers()

    def do_POST(self):
        if self.path != "/convert":
            self.send_error(404, "Ruta no encontrada")
            return

        try:
            content_length = int(self.headers.get("Content-Length", "0"))
        except ValueError:
            self.send_error(400, "Longitud de archivo no válida")
            return

        if content_length <= 0 or content_length > MAX_UPLOAD_BYTES:
            self.send_error(413, "El video está vacío o supera los 100 MB")
            return

        webm_data = self.rfile.read(content_length)
        command = [
            "ffmpeg",
            "-hide_banner",
            "-loglevel",
            "error",
            "-i",
            "pipe:0",
            "-c:v",
            "libx264",
            "-preset",
            "ultrafast",
            "-pix_fmt",
            "yuv420p",
            "-c:a",
            "aac",
            "-b:a",
            "128k",
            "-movflags",
            "frag_keyframe+empty_moov+default_base_moof",
            "-f",
            "mp4",
            "pipe:1",
        ]

        try:
            result = subprocess.run(command, input=webm_data, capture_output=True, check=True)
        except FileNotFoundError:
            self.send_error(503, "No se encontró ffmpeg en este equipo")
            return
        except subprocess.CalledProcessError as error:
            message = error.stderr.decode("utf-8", errors="replace")[-1500:]
            self.send_error(500, f"No se pudo convertir el video: {message}")
            return

        self.send_response(200)
        self.send_header("Content-Type", "video/mp4")
        self.send_header("Content-Length", str(len(result.stdout)))
        self.send_header("Content-Disposition", 'attachment; filename="partitura-musical.mp4"')
        self.end_headers()
        self.wfile.write(result.stdout)


if __name__ == "__main__":
    server = ThreadingHTTPServer(("127.0.0.1", 8765), ExportHandler)
    print("Servidor listo en http://127.0.0.1:8765/PROGRAMA/notas.html")
    server.serve_forever()
