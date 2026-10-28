# Generated from notas.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .notasParser import notasParser
else:
    from notasParser import notasParser

# This class defines a complete listener for a parse tree produced by notasParser.
class notasListener(ParseTreeListener):

    # Enter a parse tree produced by notasParser#prog.
    def enterProg(self, ctx:notasParser.ProgContext):
        pass

    # Exit a parse tree produced by notasParser#prog.
    def exitProg(self, ctx:notasParser.ProgContext):
        pass


    # Enter a parse tree produced by notasParser#noteList.
    def enterNoteList(self, ctx:notasParser.NoteListContext):
        pass

    # Exit a parse tree produced by notasParser#noteList.
    def exitNoteList(self, ctx:notasParser.NoteListContext):
        pass


    # Enter a parse tree produced by notasParser#noteExpr.
    def enterNoteExpr(self, ctx:notasParser.NoteExprContext):
        pass

    # Exit a parse tree produced by notasParser#noteExpr.
    def exitNoteExpr(self, ctx:notasParser.NoteExprContext):
        pass



del notasParser