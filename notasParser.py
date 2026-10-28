# Generated from notas.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\t")
        buf.write("!\4\2\t\2\4\3\t\3\4\4\t\4\3\2\3\2\3\2\3\3\3\3\3\3\7\3")
        buf.write("\17\n\3\f\3\16\3\22\13\3\3\4\3\4\5\4\26\n\4\3\4\5\4\31")
        buf.write("\n\4\3\4\7\4\34\n\4\f\4\16\4\37\13\4\3\4\2\2\5\2\4\6\2")
        buf.write("\3\3\2\4\5\2!\2\b\3\2\2\2\4\13\3\2\2\2\6\23\3\2\2\2\b")
        buf.write("\t\5\4\3\2\t\n\7\2\2\3\n\3\3\2\2\2\13\20\5\6\4\2\f\r\7")
        buf.write("\3\2\2\r\17\5\6\4\2\16\f\3\2\2\2\17\22\3\2\2\2\20\16\3")
        buf.write("\2\2\2\20\21\3\2\2\2\21\5\3\2\2\2\22\20\3\2\2\2\23\25")
        buf.write("\t\2\2\2\24\26\7\6\2\2\25\24\3\2\2\2\25\26\3\2\2\2\26")
        buf.write("\30\3\2\2\2\27\31\7\7\2\2\30\27\3\2\2\2\30\31\3\2\2\2")
        buf.write("\31\35\3\2\2\2\32\34\7\b\2\2\33\32\3\2\2\2\34\37\3\2\2")
        buf.write("\2\35\33\3\2\2\2\35\36\3\2\2\2\36\7\3\2\2\2\37\35\3\2")
        buf.write("\2\2\6\20\25\30\35")
        return buf.getvalue()


class notasParser ( Parser ):

    grammarFileName = "notas.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "SEPARATOR", "NOTE_NAME", "LETTER", "ACCIDENTAL", 
                      "OCTAVE", "APOSTROPHE", "WS" ]

    RULE_prog = 0
    RULE_noteList = 1
    RULE_noteExpr = 2

    ruleNames =  [ "prog", "noteList", "noteExpr" ]

    EOF = Token.EOF
    SEPARATOR=1
    NOTE_NAME=2
    LETTER=3
    ACCIDENTAL=4
    OCTAVE=5
    APOSTROPHE=6
    WS=7

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def noteList(self):
            return self.getTypedRuleContext(notasParser.NoteListContext,0)


        def EOF(self):
            return self.getToken(notasParser.EOF, 0)

        def getRuleIndex(self):
            return notasParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = notasParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 6
            self.noteList()
            self.state = 7
            self.match(notasParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NoteListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def noteExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(notasParser.NoteExprContext)
            else:
                return self.getTypedRuleContext(notasParser.NoteExprContext,i)


        def SEPARATOR(self, i:int=None):
            if i is None:
                return self.getTokens(notasParser.SEPARATOR)
            else:
                return self.getToken(notasParser.SEPARATOR, i)

        def getRuleIndex(self):
            return notasParser.RULE_noteList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNoteList" ):
                listener.enterNoteList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNoteList" ):
                listener.exitNoteList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNoteList" ):
                return visitor.visitNoteList(self)
            else:
                return visitor.visitChildren(self)




    def noteList(self):

        localctx = notasParser.NoteListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_noteList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9
            self.noteExpr()
            self.state = 14
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==notasParser.SEPARATOR:
                self.state = 10
                self.match(notasParser.SEPARATOR)
                self.state = 11
                self.noteExpr()
                self.state = 16
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NoteExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOTE_NAME(self):
            return self.getToken(notasParser.NOTE_NAME, 0)

        def LETTER(self):
            return self.getToken(notasParser.LETTER, 0)

        def ACCIDENTAL(self):
            return self.getToken(notasParser.ACCIDENTAL, 0)

        def OCTAVE(self):
            return self.getToken(notasParser.OCTAVE, 0)

        def APOSTROPHE(self, i:int=None):
            if i is None:
                return self.getTokens(notasParser.APOSTROPHE)
            else:
                return self.getToken(notasParser.APOSTROPHE, i)

        def getRuleIndex(self):
            return notasParser.RULE_noteExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNoteExpr" ):
                listener.enterNoteExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNoteExpr" ):
                listener.exitNoteExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNoteExpr" ):
                return visitor.visitNoteExpr(self)
            else:
                return visitor.visitChildren(self)




    def noteExpr(self):

        localctx = notasParser.NoteExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_noteExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            _la = self._input.LA(1)
            if not(_la==notasParser.NOTE_NAME or _la==notasParser.LETTER):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 19
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==notasParser.ACCIDENTAL:
                self.state = 18
                self.match(notasParser.ACCIDENTAL)


            self.state = 22
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==notasParser.OCTAVE:
                self.state = 21
                self.match(notasParser.OCTAVE)


            self.state = 27
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==notasParser.APOSTROPHE:
                self.state = 24
                self.match(notasParser.APOSTROPHE)
                self.state = 29
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





