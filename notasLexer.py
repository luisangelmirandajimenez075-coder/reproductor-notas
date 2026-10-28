# Generated from notas.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\t")
        buf.write("9\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\3\2\3\2\6\2\24\n\2\r\2\16\2\25\5\2\30\n\2\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\5\3)\n\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\6\b\64")
        buf.write("\n\b\r\b\16\b\65\3\b\3\b\2\2\t\3\3\5\4\7\5\t\6\13\7\r")
        buf.write("\b\17\t\3\2\22\5\2./==\u2015\u2016\5\2\13\f\17\17\"\"")
        buf.write("\4\2FFff\4\2QQqq\4\2TTtt\4\2GGgg\4\2OOoo\4\2KKkk\4\2H")
        buf.write("Hhh\4\2CCcc\4\2UUuu\4\2NNnn\4\2CIci\6\2%%dd\u266f\u266f")
        buf.write("\u2671\u2671\3\2\62:\5\2))\u201b\u201b\u2034\u2034\2A")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\3\27\3\2\2\2\5(\3\2")
        buf.write("\2\2\7*\3\2\2\2\t,\3\2\2\2\13.\3\2\2\2\r\60\3\2\2\2\17")
        buf.write("\63\3\2\2\2\21\30\t\2\2\2\22\24\t\3\2\2\23\22\3\2\2\2")
        buf.write("\24\25\3\2\2\2\25\23\3\2\2\2\25\26\3\2\2\2\26\30\3\2\2")
        buf.write("\2\27\21\3\2\2\2\27\23\3\2\2\2\30\4\3\2\2\2\31\32\t\4")
        buf.write("\2\2\32)\t\5\2\2\33\34\t\6\2\2\34)\t\7\2\2\35\36\t\b\2")
        buf.write("\2\36)\t\t\2\2\37 \t\n\2\2 )\t\13\2\2!\"\t\f\2\2\"#\t")
        buf.write("\5\2\2#)\t\r\2\2$%\t\r\2\2%)\t\13\2\2&\'\t\f\2\2\')\t")
        buf.write("\t\2\2(\31\3\2\2\2(\33\3\2\2\2(\35\3\2\2\2(\37\3\2\2\2")
        buf.write("(!\3\2\2\2($\3\2\2\2(&\3\2\2\2)\6\3\2\2\2*+\t\16\2\2+")
        buf.write("\b\3\2\2\2,-\t\17\2\2-\n\3\2\2\2./\t\20\2\2/\f\3\2\2\2")
        buf.write("\60\61\t\21\2\2\61\16\3\2\2\2\62\64\t\3\2\2\63\62\3\2")
        buf.write("\2\2\64\65\3\2\2\2\65\63\3\2\2\2\65\66\3\2\2\2\66\67\3")
        buf.write("\2\2\2\678\b\b\2\28\20\3\2\2\2\7\2\25\27(\65\3\b\2\2")
        return buf.getvalue()


class notasLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    SEPARATOR = 1
    NOTE_NAME = 2
    LETTER = 3
    ACCIDENTAL = 4
    OCTAVE = 5
    APOSTROPHE = 6
    WS = 7

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "SEPARATOR", "NOTE_NAME", "LETTER", "ACCIDENTAL", "OCTAVE", 
            "APOSTROPHE", "WS" ]

    ruleNames = [ "SEPARATOR", "NOTE_NAME", "LETTER", "ACCIDENTAL", "OCTAVE", 
                  "APOSTROPHE", "WS" ]

    grammarFileName = "notas.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


