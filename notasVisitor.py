# Generated from notas.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .notasParser import notasParser
else:
    from notasParser import notasParser

# This class defines a complete generic visitor for a parse tree produced by notasParser.

class notasVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by notasParser#prog.
    def visitProg(self, ctx:notasParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by notasParser#noteList.
    def visitNoteList(self, ctx:notasParser.NoteListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by notasParser#noteExpr.
    def visitNoteExpr(self, ctx:notasParser.NoteExprContext):
        return self.visitChildren(ctx)



del notasParser