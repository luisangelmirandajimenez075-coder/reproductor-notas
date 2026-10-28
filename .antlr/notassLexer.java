// Generated from /home/luis/Documentos/5_Sinfonia_Bethoven/notas.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class notassLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		SEPARATOR=1, NOTE_NAME=2, LETTER=3, ACCIDENTAL=4, OCTAVE=5, APOSTROPHE=6, 
		WS=7;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"SEPARATOR", "NOTE_NAME", "LETTER", "ACCIDENTAL", "OCTAVE", "APOSTROPHE", 
			"WS"
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


	public notassLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "notas.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u0000\u00077\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0001\u0000"+
		"\u0001\u0000\u0004\u0000\u0012\b\u0000\u000b\u0000\f\u0000\u0013\u0003"+
		"\u0000\u0016\b\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0003\u0001\'\b"+
		"\u0001\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0004\u0001"+
		"\u0004\u0001\u0005\u0001\u0005\u0001\u0006\u0004\u00062\b\u0006\u000b"+
		"\u0006\f\u00063\u0001\u0006\u0001\u0006\u0000\u0000\u0007\u0001\u0001"+
		"\u0003\u0002\u0005\u0003\u0007\u0004\t\u0005\u000b\u0006\r\u0007\u0001"+
		"\u0000\u0010\u0003\u0000,-;;\u2013\u2014\u0003\u0000\t\n\r\r  \u0002\u0000"+
		"DDdd\u0002\u0000OOoo\u0002\u0000RRrr\u0002\u0000EEee\u0002\u0000MMmm\u0002"+
		"\u0000IIii\u0002\u0000FFff\u0002\u0000AAaa\u0002\u0000SSss\u0002\u0000"+
		"LLll\u0002\u0000AGag\u0004\u0000##bb\u266d\u266d\u266f\u266f\u0001\u0000"+
		"08\u0003\u0000\'\'\u2019\u2019\u2032\u2032?\u0000\u0001\u0001\u0000\u0000"+
		"\u0000\u0000\u0003\u0001\u0000\u0000\u0000\u0000\u0005\u0001\u0000\u0000"+
		"\u0000\u0000\u0007\u0001\u0000\u0000\u0000\u0000\t\u0001\u0000\u0000\u0000"+
		"\u0000\u000b\u0001\u0000\u0000\u0000\u0000\r\u0001\u0000\u0000\u0000\u0001"+
		"\u0015\u0001\u0000\u0000\u0000\u0003&\u0001\u0000\u0000\u0000\u0005(\u0001"+
		"\u0000\u0000\u0000\u0007*\u0001\u0000\u0000\u0000\t,\u0001\u0000\u0000"+
		"\u0000\u000b.\u0001\u0000\u0000\u0000\r1\u0001\u0000\u0000\u0000\u000f"+
		"\u0016\u0007\u0000\u0000\u0000\u0010\u0012\u0007\u0001\u0000\u0000\u0011"+
		"\u0010\u0001\u0000\u0000\u0000\u0012\u0013\u0001\u0000\u0000\u0000\u0013"+
		"\u0011\u0001\u0000\u0000\u0000\u0013\u0014\u0001\u0000\u0000\u0000\u0014"+
		"\u0016\u0001\u0000\u0000\u0000\u0015\u000f\u0001\u0000\u0000\u0000\u0015"+
		"\u0011\u0001\u0000\u0000\u0000\u0016\u0002\u0001\u0000\u0000\u0000\u0017"+
		"\u0018\u0007\u0002\u0000\u0000\u0018\'\u0007\u0003\u0000\u0000\u0019\u001a"+
		"\u0007\u0004\u0000\u0000\u001a\'\u0007\u0005\u0000\u0000\u001b\u001c\u0007"+
		"\u0006\u0000\u0000\u001c\'\u0007\u0007\u0000\u0000\u001d\u001e\u0007\b"+
		"\u0000\u0000\u001e\'\u0007\t\u0000\u0000\u001f \u0007\n\u0000\u0000 !"+
		"\u0007\u0003\u0000\u0000!\'\u0007\u000b\u0000\u0000\"#\u0007\u000b\u0000"+
		"\u0000#\'\u0007\t\u0000\u0000$%\u0007\n\u0000\u0000%\'\u0007\u0007\u0000"+
		"\u0000&\u0017\u0001\u0000\u0000\u0000&\u0019\u0001\u0000\u0000\u0000&"+
		"\u001b\u0001\u0000\u0000\u0000&\u001d\u0001\u0000\u0000\u0000&\u001f\u0001"+
		"\u0000\u0000\u0000&\"\u0001\u0000\u0000\u0000&$\u0001\u0000\u0000\u0000"+
		"\'\u0004\u0001\u0000\u0000\u0000()\u0007\f\u0000\u0000)\u0006\u0001\u0000"+
		"\u0000\u0000*+\u0007\r\u0000\u0000+\b\u0001\u0000\u0000\u0000,-\u0007"+
		"\u000e\u0000\u0000-\n\u0001\u0000\u0000\u0000./\u0007\u000f\u0000\u0000"+
		"/\f\u0001\u0000\u0000\u000002\u0007\u0001\u0000\u000010\u0001\u0000\u0000"+
		"\u000023\u0001\u0000\u0000\u000031\u0001\u0000\u0000\u000034\u0001\u0000"+
		"\u0000\u000045\u0001\u0000\u0000\u000056\u0006\u0006\u0000\u00006\u000e"+
		"\u0001\u0000\u0000\u0000\u0005\u0000\u0013\u0015&3\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}