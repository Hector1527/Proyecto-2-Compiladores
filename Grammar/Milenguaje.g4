grammar MiLenguaje;

programa: INICIO declaraciones cuerpo FIN;

declaraciones: declaracion declaraciones | ;

declaracion: tipo ID ('=' expresion)? ';';

tipo: ENTERO | DECIMAL | CADENA | BOOLEANO;

cuerpo: instruccion cuerpo | ;

instruccion: asignacion
           | condicional
           | bucle
           | entrada_salida
           | llamada_funcion
           | definicion_funcion;

asignacion: ID '=' expresion ';';

// Expresiones
expresion: termino expresion_prima;

expresion_prima: (SUMA | RESTA) termino expresion_prima | ;

termino: factor termino_prima;

termino_prima: (MULT | DIV | MOD) factor termino_prima | ;

factor: '(' expresion ')'
      | ID
      | NUMERO
      | CADENA_LITERAL
      | BOOLEAN_LITERAL;

condicional: SI '(' condicion ')' '{' cuerpo '}' sino;

sino: SINO '{' cuerpo '}' | ;

condicion: expresion op_relacional expresion;

op_relacional: IGUAL | DISTINTO | MAYOR | MENOR | MAYOR_IGUAL | MENOR_IGUAL;

bucle: MIENTRAS '(' condicion ')' '{' cuerpo '}';

entrada_salida: LEER '(' ID ')' ';'
              | ESCRIBIR '(' expresion ')' ';';

definicion_funcion: FUNCION ID '(' parametros ')' '{' cuerpo '}'

parametros: lista_parametros | ;

lista_parametros: tipo ID lista_parametros_prima;

lista_parametros_prima: COMA tipo ID lista_parametros_prima | ;

llamada_funcion: ID '(' argumentos ')' ';';

argumentos: lista_argumentos | ;

lista_argumentos: expresion lista_argumentos_prima;

lista_argumentos_prima: COMA expresion lista_argumentos_prima | ;

// Tokens (palabras reservadas)
INICIO: 'inicio';
FIN: 'fin';
ENTERO: 'entero';
DECIMAL: 'decimal';
CADENA: 'cadena';
BOOLEANO: 'booleano';
SI: 'si';
SINO: 'sino';
MIENTRAS: 'mientras';
LEER: 'leer';
ESCRIBIR: 'escribir';
FUNCION: 'funcion';
BOOLEAN_LITERAL: 'verdadero' | 'falso';

// Operadores
SUMA: '+';
RESTA: '-';
MULT: '*';
DIV: '/';
MOD: '%';
IGUAL: '==';
DISTINTO: '!=';
MAYOR: '>';
MENOR: '<';
MAYOR_IGUAL: '>=';
MENOR_IGUAL: '<=';
ASIGNACION: '=';

// Símbolos
PAR_IZQ: '(';
PAR_DER: ')';
LLAVE_IZQ: '{';
LLAVE_DER: '}';
PUNTO_COMA: ';';
COMA: ',';

// Tokens complejos
ID: [a-zA-Z][a-zA-Z0-9]*;
NUMERO: [0-9]+ ('.' [0-9]+)?;
CADENA_LITERAL: '"' ~["\r\n]* '"';

// Espacios y comentarios
WS: [ \t\r\n]+ -> skip;
COMMENT: '//' ~[\r\n]* -> skip;