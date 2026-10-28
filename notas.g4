grammar notas;

// Regla inicial
prog
    : noteList EOF
    ;

// Secuencia de notas separadas por espacios, comas, guiones o puntos y comas
noteList
    : noteExpr (SEPARATOR noteExpr)*
    ;

SEPARATOR
    : ',' | '-' | ';' | '–' | '—' | [ \t\r\n]+
    ;

// Una nota musical individual
noteExpr
    : (NOTE_NAME | LETTER) ACCIDENTAL? OCTAVE? APOSTROPHE*
    ;

// Nombres de notas en español
NOTE_NAME
    : [dD][oO]
    | [rR][eE]
    | [mM][iI]
    | [fF][aA]
    | [sS][oO][lL]
    | [lL][aA]
    | [sS][iI]
    ;

// Nombres de notas en notación anglosajona (C, D, E, F, G, A, B)
LETTER
    : [a-gA-G]
    ;

ACCIDENTAL
    : '#' | 'b' | '♯' | '♭'
    ;

OCTAVE
    : [0-8]
    ;

APOSTROPHE
    : '\'' | '’' | '′'
    ;

WS
    : [ \t\r\n]+ -> skip
    ;