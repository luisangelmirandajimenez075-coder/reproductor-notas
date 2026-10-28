// Generated from /home/luis/Documentos/5_Sinfonia_Bethoven/notas.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class notasParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		SEPARATOR=1, NOTE_NAME=2, LETTER=3, ACCIDENTAL=4, OCTAVE=5, APOSTROPHE=6, 
		WS=7;
	public static final int
		RULE_prog = 0, RULE_noteList = 1, RULE_noteExpr = 2;
	private static String[] makeRuleNames() {
		return new String[] {
			"prog", "noteList", "noteExpr"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "SEPARATOR", "NOTE_NAME", "LETTER", "ACCIDENTAL", "OCTAVE", "APOSTROPHE", 
			"WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "notas.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public notasParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgContext extends ParserRuleContext {
		public NoteListContext noteList() {
			return getRuleContext(NoteListContext.class,0);
		}
		public TerminalNode EOF() { return getToken(notasParser.EOF, 0); }
		public ProgContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_prog; }
	}

	public final ProgContext prog() throws RecognitionException {
		ProgContext _localctx = new ProgContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_prog);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(6);
			noteList();
			setState(7);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class NoteListContext extends ParserRuleContext {
		public List<NoteExprContext> noteExpr() {
			return getRuleContexts(NoteExprContext.class);
		}
		public NoteExprContext noteExpr(int i) {
			return getRuleContext(NoteExprContext.class,i);
		}
		public List<TerminalNode> SEPARATOR() { return getTokens(notasParser.SEPARATOR); }
		public TerminalNode SEPARATOR(int i) {
			return getToken(notasParser.SEPARATOR, i);
		}
		public NoteListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_noteList; }
	}

	public final NoteListContext noteList() throws RecognitionException {
		NoteListContext _localctx = new NoteListContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_noteList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(9);
			noteExpr();
			setState(14);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==SEPARATOR) {
				{
				{
				setState(10);
				match(SEPARATOR);
				setState(11);
				noteExpr();
				}
				}
				setState(16);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class NoteExprContext extends ParserRuleContext {
		public TerminalNode NOTE_NAME() { return getToken(notasParser.NOTE_NAME, 0); }
		public TerminalNode LETTER() { return getToken(notasParser.LETTER, 0); }
		public TerminalNode ACCIDENTAL() { return getToken(notasParser.ACCIDENTAL, 0); }
		public TerminalNode OCTAVE() { return getToken(notasParser.OCTAVE, 0); }
		public List<TerminalNode> APOSTROPHE() { return getTokens(notasParser.APOSTROPHE); }
		public TerminalNode APOSTROPHE(int i) {
			return getToken(notasParser.APOSTROPHE, i);
		}
		public NoteExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_noteExpr; }
	}

	public final NoteExprContext noteExpr() throws RecognitionException {
		NoteExprContext _localctx = new NoteExprContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_noteExpr);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(17);
			_la = _input.LA(1);
			if ( !(_la==NOTE_NAME || _la==LETTER) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(19);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ACCIDENTAL) {
				{
				setState(18);
				match(ACCIDENTAL);
				}
			}

			setState(22);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==OCTAVE) {
				{
				setState(21);
				match(OCTAVE);
				}
			}

			setState(27);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==APOSTROPHE) {
				{
				{
				setState(24);
				match(APOSTROPHE);
				}
				}
				setState(29);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001\u0007\u001f\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001"+
		"\u0002\u0002\u0007\u0002\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0005\u0001\r\b\u0001\n\u0001\f\u0001\u0010\t"+
		"\u0001\u0001\u0002\u0001\u0002\u0003\u0002\u0014\b\u0002\u0001\u0002\u0003"+
		"\u0002\u0017\b\u0002\u0001\u0002\u0005\u0002\u001a\b\u0002\n\u0002\f\u0002"+
		"\u001d\t\u0002\u0001\u0002\u0000\u0000\u0003\u0000\u0002\u0004\u0000\u0001"+
		"\u0001\u0000\u0002\u0003\u001f\u0000\u0006\u0001\u0000\u0000\u0000\u0002"+
		"\t\u0001\u0000\u0000\u0000\u0004\u0011\u0001\u0000\u0000\u0000\u0006\u0007"+
		"\u0003\u0002\u0001\u0000\u0007\b\u0005\u0000\u0000\u0001\b\u0001\u0001"+
		"\u0000\u0000\u0000\t\u000e\u0003\u0004\u0002\u0000\n\u000b\u0005\u0001"+
		"\u0000\u0000\u000b\r\u0003\u0004\u0002\u0000\f\n\u0001\u0000\u0000\u0000"+
		"\r\u0010\u0001\u0000\u0000\u0000\u000e\f\u0001\u0000\u0000\u0000\u000e"+
		"\u000f\u0001\u0000\u0000\u0000\u000f\u0003\u0001\u0000\u0000\u0000\u0010"+
		"\u000e\u0001\u0000\u0000\u0000\u0011\u0013\u0007\u0000\u0000\u0000\u0012"+
		"\u0014\u0005\u0004\u0000\u0000\u0013\u0012\u0001\u0000\u0000\u0000\u0013"+
		"\u0014\u0001\u0000\u0000\u0000\u0014\u0016\u0001\u0000\u0000\u0000\u0015"+
		"\u0017\u0005\u0005\u0000\u0000\u0016\u0015\u0001\u0000\u0000\u0000\u0016"+
		"\u0017\u0001\u0000\u0000\u0000\u0017\u001b\u0001\u0000\u0000\u0000\u0018"+
		"\u001a\u0005\u0006\u0000\u0000\u0019\u0018\u0001\u0000\u0000\u0000\u001a"+
		"\u001d\u0001\u0000\u0000\u0000\u001b\u0019\u0001\u0000\u0000\u0000\u001b"+
		"\u001c\u0001\u0000\u0000\u0000\u001c\u0005\u0001\u0000\u0000\u0000\u001d"+
		"\u001b\u0001\u0000\u0000\u0000\u0004\u000e\u0013\u0016\u001b";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}