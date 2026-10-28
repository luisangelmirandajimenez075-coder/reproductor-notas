import sys
from antlr4 import *
from notasLexer import notasLexer
from notasParser import notasParser
from notasVisitor import notasVisitor

# Diccionarios de apoyo para semitonos
PITCH_CLASSES = {'c': 0, 'd': 2, 'e': 4, 'f': 5, 'g': 7, 'a': 9, 'b': 11}
SPANISH_NOTES = {'do': 'c', 're': 'd', 'mi': 'e', 'fa': 'f', 'sol': 'g', 'la': 'a', 'si': 'b'}
NOTE_NUMBERS = {'c': 0, 'd': 1, 'e': 2, 'f': 3, 'g': 4, 'a': 5, 'b': 6}

class MusicEvaluator(notasVisitor):
    def __init__(self):
        self.notes = []

    def visitNoteExpr(self, ctx: notasParser.NoteExprContext):
        token_text = ctx.getText()
        
        # Extraer partes usando los hijos del nodo o texto
        raw_note = ctx.getChild(0).getText().lower()
        letter = SPANISH_NOTES.get(raw_note, raw_note)
        
        semitone = PITCH_CLASSES[letter]
        
        # Verificar alteración (# o b)
        accidental_idx = 1
        accidental = 0
        if ctx.getChildCount() > accidental_idx and ctx.getChild(accidental_idx).symbol.type == notasParser.ACCIDENTAL:
            acc_text = ctx.getChild(accidental_idx).getText()
            if acc_text in ['#', '♯']:
                semitone += 1
                accidental = 1
            elif acc_text in ['b', '♭']:
                semitone -= 1
                accidental = -1
            accidental_idx += 1

        # Calcular octava y apóstrofos (')
        octave = 4
        apostrophes = 0
        for i in range(accidental_idx, ctx.getChildCount()):
            child_text = ctx.getChild(i).getText()
            if child_text.isdigit():
                octave = int(child_text)
            elif child_text in ["'", "’", "′"]:
                apostrophes += len(child_text)
        
        total_octave = octave + apostrophes
        midi = (total_octave + 1) * 12 + semitone
        frequency = 440 * (2 ** ((midi - 69) / 12))

        self.notes.append({
            "token": token_text,
            "midi": midi,
            "frequency": frequency,
            "letter": letter,
            "semitone": semitone
        })
        return self.notes

def parse_melody_with_antlr(input_string):
    input_stream = InputStream(input_string)
    lexer = notasLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = notasParser(stream)
    
    tree = parser.prog()
    evaluator = MusicEvaluator()
    evaluator.visit(tree)
    return evaluator.notes

# Bloque de ejecución principal
if __name__ == "__main__":
    secuencia = "Si4 - Si4 - Do5 - Re5"
    resultado = parse_melody_with_antlr(secuencia)
    print("Notas parseadas con ANTLR:", resultado)