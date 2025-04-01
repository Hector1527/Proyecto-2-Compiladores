# Generated from MiLenguaje.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,36,208,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,1,0,1,0,1,
        0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,62,8,1,1,2,1,2,1,2,1,2,1,3,1,3,1,4,
        1,4,1,4,1,4,3,4,74,8,4,1,5,1,5,1,5,1,5,1,5,1,5,3,5,82,8,5,1,6,1,
        6,1,6,1,6,1,6,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,3,8,97,8,8,1,9,1,9,
        1,9,1,10,1,10,1,10,1,10,1,10,3,10,107,8,10,1,11,1,11,1,11,1,11,1,
        11,1,11,1,11,1,11,3,11,117,8,11,1,12,1,12,1,12,1,12,1,12,1,12,1,
        12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,3,13,134,8,13,1,14,1,
        14,1,14,1,14,1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,
        17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,3,17,161,8,
        17,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,19,1,19,3,19,174,
        8,19,1,20,1,20,1,20,1,20,1,21,1,21,1,21,1,21,1,21,1,21,3,21,186,
        8,21,1,22,1,22,1,22,1,22,1,22,1,22,1,23,1,23,3,23,196,8,23,1,24,
        1,24,1,24,1,25,1,25,1,25,1,25,1,25,3,25,206,8,25,1,25,0,0,26,0,2,
        4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,
        50,0,4,1,0,3,6,1,0,14,15,1,0,16,18,1,0,19,24,200,0,52,1,0,0,0,2,
        61,1,0,0,0,4,63,1,0,0,0,6,67,1,0,0,0,8,73,1,0,0,0,10,81,1,0,0,0,
        12,83,1,0,0,0,14,88,1,0,0,0,16,96,1,0,0,0,18,98,1,0,0,0,20,106,1,
        0,0,0,22,116,1,0,0,0,24,118,1,0,0,0,26,133,1,0,0,0,28,135,1,0,0,
        0,30,139,1,0,0,0,32,141,1,0,0,0,34,160,1,0,0,0,36,162,1,0,0,0,38,
        173,1,0,0,0,40,175,1,0,0,0,42,185,1,0,0,0,44,187,1,0,0,0,46,195,
        1,0,0,0,48,197,1,0,0,0,50,205,1,0,0,0,52,53,5,1,0,0,53,54,3,2,1,
        0,54,55,3,8,4,0,55,56,5,2,0,0,56,1,1,0,0,0,57,58,3,4,2,0,58,59,3,
        2,1,0,59,62,1,0,0,0,60,62,1,0,0,0,61,57,1,0,0,0,61,60,1,0,0,0,62,
        3,1,0,0,0,63,64,3,6,3,0,64,65,5,32,0,0,65,66,5,30,0,0,66,5,1,0,0,
        0,67,68,7,0,0,0,68,7,1,0,0,0,69,70,3,10,5,0,70,71,3,8,4,0,71,74,
        1,0,0,0,72,74,1,0,0,0,73,69,1,0,0,0,73,72,1,0,0,0,74,9,1,0,0,0,75,
        82,3,12,6,0,76,82,3,24,12,0,77,82,3,32,16,0,78,82,3,34,17,0,79,82,
        3,44,22,0,80,82,3,36,18,0,81,75,1,0,0,0,81,76,1,0,0,0,81,77,1,0,
        0,0,81,78,1,0,0,0,81,79,1,0,0,0,81,80,1,0,0,0,82,11,1,0,0,0,83,84,
        5,32,0,0,84,85,5,25,0,0,85,86,3,14,7,0,86,87,5,30,0,0,87,13,1,0,
        0,0,88,89,3,18,9,0,89,90,3,16,8,0,90,15,1,0,0,0,91,92,7,1,0,0,92,
        93,3,18,9,0,93,94,3,16,8,0,94,97,1,0,0,0,95,97,1,0,0,0,96,91,1,0,
        0,0,96,95,1,0,0,0,97,17,1,0,0,0,98,99,3,22,11,0,99,100,3,20,10,0,
        100,19,1,0,0,0,101,102,7,2,0,0,102,103,3,22,11,0,103,104,3,20,10,
        0,104,107,1,0,0,0,105,107,1,0,0,0,106,101,1,0,0,0,106,105,1,0,0,
        0,107,21,1,0,0,0,108,109,5,26,0,0,109,110,3,14,7,0,110,111,5,27,
        0,0,111,117,1,0,0,0,112,117,5,32,0,0,113,117,5,33,0,0,114,117,5,
        34,0,0,115,117,5,13,0,0,116,108,1,0,0,0,116,112,1,0,0,0,116,113,
        1,0,0,0,116,114,1,0,0,0,116,115,1,0,0,0,117,23,1,0,0,0,118,119,5,
        7,0,0,119,120,5,26,0,0,120,121,3,28,14,0,121,122,5,27,0,0,122,123,
        5,28,0,0,123,124,3,8,4,0,124,125,5,29,0,0,125,126,3,26,13,0,126,
        25,1,0,0,0,127,128,5,8,0,0,128,129,5,28,0,0,129,130,3,8,4,0,130,
        131,5,29,0,0,131,134,1,0,0,0,132,134,1,0,0,0,133,127,1,0,0,0,133,
        132,1,0,0,0,134,27,1,0,0,0,135,136,3,14,7,0,136,137,3,30,15,0,137,
        138,3,14,7,0,138,29,1,0,0,0,139,140,7,3,0,0,140,31,1,0,0,0,141,142,
        5,9,0,0,142,143,5,26,0,0,143,144,3,28,14,0,144,145,5,27,0,0,145,
        146,5,28,0,0,146,147,3,8,4,0,147,148,5,29,0,0,148,33,1,0,0,0,149,
        150,5,10,0,0,150,151,5,26,0,0,151,152,5,32,0,0,152,153,5,27,0,0,
        153,161,5,30,0,0,154,155,5,11,0,0,155,156,5,26,0,0,156,157,3,14,
        7,0,157,158,5,27,0,0,158,159,5,30,0,0,159,161,1,0,0,0,160,149,1,
        0,0,0,160,154,1,0,0,0,161,35,1,0,0,0,162,163,5,12,0,0,163,164,5,
        32,0,0,164,165,5,26,0,0,165,166,3,38,19,0,166,167,5,27,0,0,167,168,
        5,28,0,0,168,169,3,8,4,0,169,170,5,29,0,0,170,37,1,0,0,0,171,174,
        3,40,20,0,172,174,1,0,0,0,173,171,1,0,0,0,173,172,1,0,0,0,174,39,
        1,0,0,0,175,176,3,6,3,0,176,177,5,32,0,0,177,178,3,42,21,0,178,41,
        1,0,0,0,179,180,5,31,0,0,180,181,3,6,3,0,181,182,5,32,0,0,182,183,
        3,42,21,0,183,186,1,0,0,0,184,186,1,0,0,0,185,179,1,0,0,0,185,184,
        1,0,0,0,186,43,1,0,0,0,187,188,5,32,0,0,188,189,5,26,0,0,189,190,
        3,46,23,0,190,191,5,27,0,0,191,192,5,30,0,0,192,45,1,0,0,0,193,196,
        3,48,24,0,194,196,1,0,0,0,195,193,1,0,0,0,195,194,1,0,0,0,196,47,
        1,0,0,0,197,198,3,14,7,0,198,199,3,50,25,0,199,49,1,0,0,0,200,201,
        5,31,0,0,201,202,3,14,7,0,202,203,3,50,25,0,203,206,1,0,0,0,204,
        206,1,0,0,0,205,200,1,0,0,0,205,204,1,0,0,0,206,51,1,0,0,0,12,61,
        73,81,96,106,116,133,160,173,185,195,205
    ]

class MiLenguajeParser ( Parser ):

    grammarFileName = "MiLenguaje.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'inicio'", "'fin'", "'entero'", "'decimal'", 
                     "'cadena'", "'booleano'", "'si'", "'sino'", "'mientras'", 
                     "'leer'", "'escribir'", "'funcion'", "<INVALID>", "'+'", 
                     "'-'", "'*'", "'/'", "'%'", "'=='", "'!='", "'>'", 
                     "'<'", "'>='", "'<='", "'='", "'('", "')'", "'{'", 
                     "'}'", "';'", "','" ]

    symbolicNames = [ "<INVALID>", "INICIO", "FIN", "ENTERO", "DECIMAL", 
                      "CADENA", "BOOLEANO", "SI", "SINO", "MIENTRAS", "LEER", 
                      "ESCRIBIR", "FUNCION", "BOOLEAN_LITERAL", "SUMA", 
                      "RESTA", "MULT", "DIV", "MOD", "IGUAL", "DISTINTO", 
                      "MAYOR", "MENOR", "MAYOR_IGUAL", "MENOR_IGUAL", "ASIGNACION", 
                      "PAR_IZQ", "PAR_DER", "LLAVE_IZQ", "LLAVE_DER", "PUNTO_COMA", 
                      "COMA", "ID", "NUMERO", "CADENA_LITERAL", "WS", "COMMENT" ]

    RULE_programa = 0
    RULE_declaraciones = 1
    RULE_declaracion = 2
    RULE_tipo = 3
    RULE_cuerpo = 4
    RULE_instruccion = 5
    RULE_asignacion = 6
    RULE_expresion = 7
    RULE_expresion_prima = 8
    RULE_termino = 9
    RULE_termino_prima = 10
    RULE_factor = 11
    RULE_condicional = 12
    RULE_sino = 13
    RULE_condicion = 14
    RULE_op_relacional = 15
    RULE_bucle = 16
    RULE_entrada_salida = 17
    RULE_definicion_funcion = 18
    RULE_parametros = 19
    RULE_lista_parametros = 20
    RULE_lista_parametros_prima = 21
    RULE_llamada_funcion = 22
    RULE_argumentos = 23
    RULE_lista_argumentos = 24
    RULE_lista_argumentos_prima = 25

    ruleNames =  [ "programa", "declaraciones", "declaracion", "tipo", "cuerpo", 
                   "instruccion", "asignacion", "expresion", "expresion_prima", 
                   "termino", "termino_prima", "factor", "condicional", 
                   "sino", "condicion", "op_relacional", "bucle", "entrada_salida", 
                   "definicion_funcion", "parametros", "lista_parametros", 
                   "lista_parametros_prima", "llamada_funcion", "argumentos", 
                   "lista_argumentos", "lista_argumentos_prima" ]

    EOF = Token.EOF
    INICIO=1
    FIN=2
    ENTERO=3
    DECIMAL=4
    CADENA=5
    BOOLEANO=6
    SI=7
    SINO=8
    MIENTRAS=9
    LEER=10
    ESCRIBIR=11
    FUNCION=12
    BOOLEAN_LITERAL=13
    SUMA=14
    RESTA=15
    MULT=16
    DIV=17
    MOD=18
    IGUAL=19
    DISTINTO=20
    MAYOR=21
    MENOR=22
    MAYOR_IGUAL=23
    MENOR_IGUAL=24
    ASIGNACION=25
    PAR_IZQ=26
    PAR_DER=27
    LLAVE_IZQ=28
    LLAVE_DER=29
    PUNTO_COMA=30
    COMA=31
    ID=32
    NUMERO=33
    CADENA_LITERAL=34
    WS=35
    COMMENT=36

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INICIO(self):
            return self.getToken(MiLenguajeParser.INICIO, 0)

        def declaraciones(self):
            return self.getTypedRuleContext(MiLenguajeParser.DeclaracionesContext,0)


        def cuerpo(self):
            return self.getTypedRuleContext(MiLenguajeParser.CuerpoContext,0)


        def FIN(self):
            return self.getToken(MiLenguajeParser.FIN, 0)

        def getRuleIndex(self):
            return MiLenguajeParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)




    def programa(self):

        localctx = MiLenguajeParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(MiLenguajeParser.INICIO)
            self.state = 53
            self.declaraciones()
            self.state = 54
            self.cuerpo()
            self.state = 55
            self.match(MiLenguajeParser.FIN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracionesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracion(self):
            return self.getTypedRuleContext(MiLenguajeParser.DeclaracionContext,0)


        def declaraciones(self):
            return self.getTypedRuleContext(MiLenguajeParser.DeclaracionesContext,0)


        def getRuleIndex(self):
            return MiLenguajeParser.RULE_declaraciones

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaraciones" ):
                listener.enterDeclaraciones(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaraciones" ):
                listener.exitDeclaraciones(self)




    def declaraciones(self):

        localctx = MiLenguajeParser.DeclaracionesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaraciones)
        try:
            self.state = 61
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4, 5, 6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 57
                self.declaracion()
                self.state = 58
                self.declaraciones()
                pass
            elif token in [2, 7, 9, 10, 11, 12, 32]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo(self):
            return self.getTypedRuleContext(MiLenguajeParser.TipoContext,0)


        def ID(self):
            return self.getToken(MiLenguajeParser.ID, 0)

        def PUNTO_COMA(self):
            return self.getToken(MiLenguajeParser.PUNTO_COMA, 0)

        def getRuleIndex(self):
            return MiLenguajeParser.RULE_declaracion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracion" ):
                listener.enterDeclaracion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracion" ):
                listener.exitDeclaracion(self)




    def declaracion(self):

        localctx = MiLenguajeParser.DeclaracionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaracion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.tipo()
            self.state = 64
            self.match(MiLenguajeParser.ID)
            self.state = 65
            self.match(MiLenguajeParser.PUNTO_COMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TipoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ENTERO(self):
            return self.getToken(MiLenguajeParser.ENTERO, 0)

        def DECIMAL(self):
            return self.getToken(MiLenguajeParser.DECIMAL, 0)

        def CADENA(self):
            return self.getToken(MiLenguajeParser.CADENA, 0)

        def BOOLEANO(self):
            return self.getToken(MiLenguajeParser.BOOLEANO, 0)

        def getRuleIndex(self):
            return MiLenguajeParser.RULE_tipo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipo" ):
                listener.enterTipo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipo" ):
                listener.exitTipo(self)




    def tipo(self):

        localctx = MiLenguajeParser.TipoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_tipo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 120) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CuerpoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instruccion(self):
            return self.getTypedRuleContext(MiLenguajeParser.InstruccionContext,0)


        def cuerpo(self):
            return self.getTypedRuleContext(MiLenguajeParser.CuerpoContext,0)


        def getRuleIndex(self):
            return MiLenguajeParser.RULE_cuerpo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCuerpo" ):
                listener.enterCuerpo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCuerpo" ):
                listener.exitCuerpo(self)




    def cuerpo(self):

        localctx = MiLenguajeParser.CuerpoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_cuerpo)
        try:
            self.state = 73
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7, 9, 10, 11, 12, 32]:
                self.enterOuterAlt(localctx, 1)
                self.state = 69
                self.instruccion()
                self.state = 70
                self.cuerpo()
                pass
            elif token in [2, 29]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstruccionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def asignacion(self):
            return self.getTypedRuleContext(MiLenguajeParser.AsignacionContext,0)


        def condicional(self):
            return self.getTypedRuleContext(MiLenguajeParser.CondicionalContext,0)


        def bucle(self):
            return self.getTypedRuleContext(MiLenguajeParser.BucleContext,0)


        def entrada_salida(self):
            return self.getTypedRuleContext(MiLenguajeParser.Entrada_salidaContext,0)


        def llamada_funcion(self):
            return self.getTypedRuleContext(MiLenguajeParser.Llamada_funcionContext,0)


        def definicion_funcion(self):
            return self.getTypedRuleContext(MiLenguajeParser.Definicion_funcionContext,0)


        def getRuleIndex(self):
            return MiLenguajeParser.RULE_instruccion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstruccion" ):
                listener.enterInstruccion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstruccion" ):
                listener.exitInstruccion(self)




    def instruccion(self):

        localctx = MiLenguajeParser.InstruccionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_instruccion)
        try:
            self.state = 81
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 75
                self.asignacion()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 76
                self.condicional()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 77
                self.bucle()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 78
                self.entrada_salida()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 79
                self.llamada_funcion()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 80
                self.definicion_funcion()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiLenguajeParser.ID, 0)

        def ASIGNACION(self):
            return self.getToken(MiLenguajeParser.ASIGNACION, 0)

        def expresion(self):
            return self.getTypedRuleContext(MiLenguajeParser.ExpresionContext,0)


        def PUNTO_COMA(self):
            return self.getToken(MiLenguajeParser.PUNTO_COMA, 0)

        def getRuleIndex(self):
            return MiLenguajeParser.RULE_asignacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacion" ):
                listener.enterAsignacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacion" ):
                listener.exitAsignacion(self)




    def asignacion(self):

        localctx = MiLenguajeParser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(MiLenguajeParser.ID)
            self.state = 84
            self.match(MiLenguajeParser.ASIGNACION)
            self.state = 85
            self.expresion()
            self.state = 86
            self.match(MiLenguajeParser.PUNTO_COMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def termino(self):
            return self.getTypedRuleContext(MiLenguajeParser.TerminoContext,0)


        def expresion_prima(self):
            return self.getTypedRuleContext(MiLenguajeParser.Expresion_primaContext,0)


        def getRuleIndex(self):
            return MiLenguajeParser.RULE_expresion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresion" ):
                listener.enterExpresion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresion" ):
                listener.exitExpresion(self)




    def expresion(self):

        localctx = MiLenguajeParser.ExpresionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_expresion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.termino()
            self.state = 89
            self.expresion_prima()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expresion_primaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def termino(self):
            return self.getTypedRuleContext(MiLenguajeParser.TerminoContext,0)


        def expresion_prima(self):
            return self.getTypedRuleContext(MiLenguajeParser.Expresion_primaContext,0)


        def SUMA(self):
            return self.getToken(MiLenguajeParser.SUMA, 0)

        def RESTA(self):
            return self.getToken(MiLenguajeParser.RESTA, 0)

        def getRuleIndex(self):
            return MiLenguajeParser.RULE_expresion_prima

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresion_prima" ):
                listener.enterExpresion_prima(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresion_prima" ):
                listener.exitExpresion_prima(self)




    def expresion_prima(self):

        localctx = MiLenguajeParser.Expresion_primaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_expresion_prima)
        self._la = 0 # Token type
        try:
            self.state = 96
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14, 15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 91
                _la = self._input.LA(1)
                if not(_la==14 or _la==15):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 92
                self.termino()
                self.state = 93
                self.expresion_prima()
                pass
            elif token in [19, 20, 21, 22, 23, 24, 27, 30, 31]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TerminoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(MiLenguajeParser.FactorContext,0)


        def termino_prima(self):
            return self.getTypedRuleContext(MiLenguajeParser.Termino_primaContext,0)


        def getRuleIndex(self):
            return MiLenguajeParser.RULE_termino

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermino" ):
                listener.enterTermino(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermino" ):
                listener.exitTermino(self)




    def termino(self):

        localctx = MiLenguajeParser.TerminoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_termino)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.factor()
            self.state = 99
            self.termino_prima()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Termino_primaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(MiLenguajeParser.FactorContext,0)


        def termino_prima(self):
            return self.getTypedRuleContext(MiLenguajeParser.Termino_primaContext,0)


        def MULT(self):
            return self.getToken(MiLenguajeParser.MULT, 0)

        def DIV(self):
            return self.getToken(MiLenguajeParser.DIV, 0)

        def MOD(self):
            return self.getToken(MiLenguajeParser.MOD, 0)

        def getRuleIndex(self):
            return MiLenguajeParser.RULE_termino_prima

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermino_prima" ):
                listener.enterTermino_prima(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermino_prima" ):
                listener.exitTermino_prima(self)




    def termino_prima(self):

        localctx = MiLenguajeParser.Termino_primaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_termino_prima)
        self._la = 0 # Token type
        try:
            self.state = 106
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16, 17, 18]:
                self.enterOuterAlt(localctx, 1)
                self.state = 101
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 458752) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 102
                self.factor()
                self.state = 103
                self.termino_prima()
                pass
            elif token in [14, 15, 19, 20, 21, 22, 23, 24, 27, 30, 31]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PAR_IZQ(self):
            return self.getToken(MiLenguajeParser.PAR_IZQ, 0)

        def expresion(self):
            return self.getTypedRuleContext(MiLenguajeParser.ExpresionContext,0)


        def PAR_DER(self):
            return self.getToken(MiLenguajeParser.PAR_DER, 0)

        def ID(self):
            return self.getToken(MiLenguajeParser.ID, 0)

        def NUMERO(self):
            return self.getToken(MiLenguajeParser.NUMERO, 0)

        def CADENA_LITERAL(self):
            return self.getToken(MiLenguajeParser.CADENA_LITERAL, 0)

        def BOOLEAN_LITERAL(self):
            return self.getToken(MiLenguajeParser.BOOLEAN_LITERAL, 0)

        def getRuleIndex(self):
            return MiLenguajeParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)




    def factor(self):

        localctx = MiLenguajeParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_factor)
        try:
            self.state = 116
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26]:
                self.enterOuterAlt(localctx, 1)
                self.state = 108
                self.match(MiLenguajeParser.PAR_IZQ)
                self.state = 109
                self.expresion()
                self.state = 110
                self.match(MiLenguajeParser.PAR_DER)
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 2)
                self.state = 112
                self.match(MiLenguajeParser.ID)
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 3)
                self.state = 113
                self.match(MiLenguajeParser.NUMERO)
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 4)
                self.state = 114
                self.match(MiLenguajeParser.CADENA_LITERAL)
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 5)
                self.state = 115
                self.match(MiLenguajeParser.BOOLEAN_LITERAL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondicionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SI(self):
            return self.getToken(MiLenguajeParser.SI, 0)

        def PAR_IZQ(self):
            return self.getToken(MiLenguajeParser.PAR_IZQ, 0)

        def condicion(self):
            return self.getTypedRuleContext(MiLenguajeParser.CondicionContext,0)


        def PAR_DER(self):
            return self.getToken(MiLenguajeParser.PAR_DER, 0)

        def LLAVE_IZQ(self):
            return self.getToken(MiLenguajeParser.LLAVE_IZQ, 0)

        def cuerpo(self):
            return self.getTypedRuleContext(MiLenguajeParser.CuerpoContext,0)


        def LLAVE_DER(self):
            return self.getToken(MiLenguajeParser.LLAVE_DER, 0)

        def sino(self):
            return self.getTypedRuleContext(MiLenguajeParser.SinoContext,0)


        def getRuleIndex(self):
            return MiLenguajeParser.RULE_condicional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondicional" ):
                listener.enterCondicional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondicional" ):
                listener.exitCondicional(self)




    def condicional(self):

        localctx = MiLenguajeParser.CondicionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_condicional)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.match(MiLenguajeParser.SI)
            self.state = 119
            self.match(MiLenguajeParser.PAR_IZQ)
            self.state = 120
            self.condicion()
            self.state = 121
            self.match(MiLenguajeParser.PAR_DER)
            self.state = 122
            self.match(MiLenguajeParser.LLAVE_IZQ)
            self.state = 123
            self.cuerpo()
            self.state = 124
            self.match(MiLenguajeParser.LLAVE_DER)
            self.state = 125
            self.sino()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SinoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SINO(self):
            return self.getToken(MiLenguajeParser.SINO, 0)

        def LLAVE_IZQ(self):
            return self.getToken(MiLenguajeParser.LLAVE_IZQ, 0)

        def cuerpo(self):
            return self.getTypedRuleContext(MiLenguajeParser.CuerpoContext,0)


        def LLAVE_DER(self):
            return self.getToken(MiLenguajeParser.LLAVE_DER, 0)

        def getRuleIndex(self):
            return MiLenguajeParser.RULE_sino

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSino" ):
                listener.enterSino(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSino" ):
                listener.exitSino(self)




    def sino(self):

        localctx = MiLenguajeParser.SinoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_sino)
        try:
            self.state = 133
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 127
                self.match(MiLenguajeParser.SINO)
                self.state = 128
                self.match(MiLenguajeParser.LLAVE_IZQ)
                self.state = 129
                self.cuerpo()
                self.state = 130
                self.match(MiLenguajeParser.LLAVE_DER)
                pass
            elif token in [2, 7, 9, 10, 11, 12, 29, 32]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondicionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiLenguajeParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(MiLenguajeParser.ExpresionContext,i)


        def op_relacional(self):
            return self.getTypedRuleContext(MiLenguajeParser.Op_relacionalContext,0)


        def getRuleIndex(self):
            return MiLenguajeParser.RULE_condicion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondicion" ):
                listener.enterCondicion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondicion" ):
                listener.exitCondicion(self)




    def condicion(self):

        localctx = MiLenguajeParser.CondicionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_condicion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.expresion()
            self.state = 136
            self.op_relacional()
            self.state = 137
            self.expresion()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op_relacionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IGUAL(self):
            return self.getToken(MiLenguajeParser.IGUAL, 0)

        def DISTINTO(self):
            return self.getToken(MiLenguajeParser.DISTINTO, 0)

        def MAYOR(self):
            return self.getToken(MiLenguajeParser.MAYOR, 0)

        def MENOR(self):
            return self.getToken(MiLenguajeParser.MENOR, 0)

        def MAYOR_IGUAL(self):
            return self.getToken(MiLenguajeParser.MAYOR_IGUAL, 0)

        def MENOR_IGUAL(self):
            return self.getToken(MiLenguajeParser.MENOR_IGUAL, 0)

        def getRuleIndex(self):
            return MiLenguajeParser.RULE_op_relacional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOp_relacional" ):
                listener.enterOp_relacional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOp_relacional" ):
                listener.exitOp_relacional(self)




    def op_relacional(self):

        localctx = MiLenguajeParser.Op_relacionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_op_relacional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 33030144) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BucleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MIENTRAS(self):
            return self.getToken(MiLenguajeParser.MIENTRAS, 0)

        def PAR_IZQ(self):
            return self.getToken(MiLenguajeParser.PAR_IZQ, 0)

        def condicion(self):
            return self.getTypedRuleContext(MiLenguajeParser.CondicionContext,0)


        def PAR_DER(self):
            return self.getToken(MiLenguajeParser.PAR_DER, 0)

        def LLAVE_IZQ(self):
            return self.getToken(MiLenguajeParser.LLAVE_IZQ, 0)

        def cuerpo(self):
            return self.getTypedRuleContext(MiLenguajeParser.CuerpoContext,0)


        def LLAVE_DER(self):
            return self.getToken(MiLenguajeParser.LLAVE_DER, 0)

        def getRuleIndex(self):
            return MiLenguajeParser.RULE_bucle

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBucle" ):
                listener.enterBucle(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBucle" ):
                listener.exitBucle(self)




    def bucle(self):

        localctx = MiLenguajeParser.BucleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_bucle)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.match(MiLenguajeParser.MIENTRAS)
            self.state = 142
            self.match(MiLenguajeParser.PAR_IZQ)
            self.state = 143
            self.condicion()
            self.state = 144
            self.match(MiLenguajeParser.PAR_DER)
            self.state = 145
            self.match(MiLenguajeParser.LLAVE_IZQ)
            self.state = 146
            self.cuerpo()
            self.state = 147
            self.match(MiLenguajeParser.LLAVE_DER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Entrada_salidaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEER(self):
            return self.getToken(MiLenguajeParser.LEER, 0)

        def PAR_IZQ(self):
            return self.getToken(MiLenguajeParser.PAR_IZQ, 0)

        def ID(self):
            return self.getToken(MiLenguajeParser.ID, 0)

        def PAR_DER(self):
            return self.getToken(MiLenguajeParser.PAR_DER, 0)

        def PUNTO_COMA(self):
            return self.getToken(MiLenguajeParser.PUNTO_COMA, 0)

        def ESCRIBIR(self):
            return self.getToken(MiLenguajeParser.ESCRIBIR, 0)

        def expresion(self):
            return self.getTypedRuleContext(MiLenguajeParser.ExpresionContext,0)


        def getRuleIndex(self):
            return MiLenguajeParser.RULE_entrada_salida

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEntrada_salida" ):
                listener.enterEntrada_salida(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEntrada_salida" ):
                listener.exitEntrada_salida(self)




    def entrada_salida(self):

        localctx = MiLenguajeParser.Entrada_salidaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_entrada_salida)
        try:
            self.state = 160
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 149
                self.match(MiLenguajeParser.LEER)
                self.state = 150
                self.match(MiLenguajeParser.PAR_IZQ)
                self.state = 151
                self.match(MiLenguajeParser.ID)
                self.state = 152
                self.match(MiLenguajeParser.PAR_DER)
                self.state = 153
                self.match(MiLenguajeParser.PUNTO_COMA)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 154
                self.match(MiLenguajeParser.ESCRIBIR)
                self.state = 155
                self.match(MiLenguajeParser.PAR_IZQ)
                self.state = 156
                self.expresion()
                self.state = 157
                self.match(MiLenguajeParser.PAR_DER)
                self.state = 158
                self.match(MiLenguajeParser.PUNTO_COMA)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Definicion_funcionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCION(self):
            return self.getToken(MiLenguajeParser.FUNCION, 0)

        def ID(self):
            return self.getToken(MiLenguajeParser.ID, 0)

        def PAR_IZQ(self):
            return self.getToken(MiLenguajeParser.PAR_IZQ, 0)

        def parametros(self):
            return self.getTypedRuleContext(MiLenguajeParser.ParametrosContext,0)


        def PAR_DER(self):
            return self.getToken(MiLenguajeParser.PAR_DER, 0)

        def LLAVE_IZQ(self):
            return self.getToken(MiLenguajeParser.LLAVE_IZQ, 0)

        def cuerpo(self):
            return self.getTypedRuleContext(MiLenguajeParser.CuerpoContext,0)


        def LLAVE_DER(self):
            return self.getToken(MiLenguajeParser.LLAVE_DER, 0)

        def getRuleIndex(self):
            return MiLenguajeParser.RULE_definicion_funcion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefinicion_funcion" ):
                listener.enterDefinicion_funcion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefinicion_funcion" ):
                listener.exitDefinicion_funcion(self)




    def definicion_funcion(self):

        localctx = MiLenguajeParser.Definicion_funcionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_definicion_funcion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.match(MiLenguajeParser.FUNCION)
            self.state = 163
            self.match(MiLenguajeParser.ID)
            self.state = 164
            self.match(MiLenguajeParser.PAR_IZQ)
            self.state = 165
            self.parametros()
            self.state = 166
            self.match(MiLenguajeParser.PAR_DER)
            self.state = 167
            self.match(MiLenguajeParser.LLAVE_IZQ)
            self.state = 168
            self.cuerpo()
            self.state = 169
            self.match(MiLenguajeParser.LLAVE_DER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametrosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lista_parametros(self):
            return self.getTypedRuleContext(MiLenguajeParser.Lista_parametrosContext,0)


        def getRuleIndex(self):
            return MiLenguajeParser.RULE_parametros

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParametros" ):
                listener.enterParametros(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParametros" ):
                listener.exitParametros(self)




    def parametros(self):

        localctx = MiLenguajeParser.ParametrosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_parametros)
        try:
            self.state = 173
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4, 5, 6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 171
                self.lista_parametros()
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lista_parametrosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo(self):
            return self.getTypedRuleContext(MiLenguajeParser.TipoContext,0)


        def ID(self):
            return self.getToken(MiLenguajeParser.ID, 0)

        def lista_parametros_prima(self):
            return self.getTypedRuleContext(MiLenguajeParser.Lista_parametros_primaContext,0)


        def getRuleIndex(self):
            return MiLenguajeParser.RULE_lista_parametros

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLista_parametros" ):
                listener.enterLista_parametros(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLista_parametros" ):
                listener.exitLista_parametros(self)




    def lista_parametros(self):

        localctx = MiLenguajeParser.Lista_parametrosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_lista_parametros)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.tipo()
            self.state = 176
            self.match(MiLenguajeParser.ID)
            self.state = 177
            self.lista_parametros_prima()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lista_parametros_primaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMA(self):
            return self.getToken(MiLenguajeParser.COMA, 0)

        def tipo(self):
            return self.getTypedRuleContext(MiLenguajeParser.TipoContext,0)


        def ID(self):
            return self.getToken(MiLenguajeParser.ID, 0)

        def lista_parametros_prima(self):
            return self.getTypedRuleContext(MiLenguajeParser.Lista_parametros_primaContext,0)


        def getRuleIndex(self):
            return MiLenguajeParser.RULE_lista_parametros_prima

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLista_parametros_prima" ):
                listener.enterLista_parametros_prima(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLista_parametros_prima" ):
                listener.exitLista_parametros_prima(self)




    def lista_parametros_prima(self):

        localctx = MiLenguajeParser.Lista_parametros_primaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_lista_parametros_prima)
        try:
            self.state = 185
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                self.enterOuterAlt(localctx, 1)
                self.state = 179
                self.match(MiLenguajeParser.COMA)
                self.state = 180
                self.tipo()
                self.state = 181
                self.match(MiLenguajeParser.ID)
                self.state = 182
                self.lista_parametros_prima()
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Llamada_funcionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiLenguajeParser.ID, 0)

        def PAR_IZQ(self):
            return self.getToken(MiLenguajeParser.PAR_IZQ, 0)

        def argumentos(self):
            return self.getTypedRuleContext(MiLenguajeParser.ArgumentosContext,0)


        def PAR_DER(self):
            return self.getToken(MiLenguajeParser.PAR_DER, 0)

        def PUNTO_COMA(self):
            return self.getToken(MiLenguajeParser.PUNTO_COMA, 0)

        def getRuleIndex(self):
            return MiLenguajeParser.RULE_llamada_funcion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLlamada_funcion" ):
                listener.enterLlamada_funcion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLlamada_funcion" ):
                listener.exitLlamada_funcion(self)




    def llamada_funcion(self):

        localctx = MiLenguajeParser.Llamada_funcionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_llamada_funcion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.match(MiLenguajeParser.ID)
            self.state = 188
            self.match(MiLenguajeParser.PAR_IZQ)
            self.state = 189
            self.argumentos()
            self.state = 190
            self.match(MiLenguajeParser.PAR_DER)
            self.state = 191
            self.match(MiLenguajeParser.PUNTO_COMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lista_argumentos(self):
            return self.getTypedRuleContext(MiLenguajeParser.Lista_argumentosContext,0)


        def getRuleIndex(self):
            return MiLenguajeParser.RULE_argumentos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgumentos" ):
                listener.enterArgumentos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgumentos" ):
                listener.exitArgumentos(self)




    def argumentos(self):

        localctx = MiLenguajeParser.ArgumentosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_argumentos)
        try:
            self.state = 195
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13, 26, 32, 33, 34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 193
                self.lista_argumentos()
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lista_argumentosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion(self):
            return self.getTypedRuleContext(MiLenguajeParser.ExpresionContext,0)


        def lista_argumentos_prima(self):
            return self.getTypedRuleContext(MiLenguajeParser.Lista_argumentos_primaContext,0)


        def getRuleIndex(self):
            return MiLenguajeParser.RULE_lista_argumentos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLista_argumentos" ):
                listener.enterLista_argumentos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLista_argumentos" ):
                listener.exitLista_argumentos(self)




    def lista_argumentos(self):

        localctx = MiLenguajeParser.Lista_argumentosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_lista_argumentos)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.expresion()
            self.state = 198
            self.lista_argumentos_prima()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lista_argumentos_primaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMA(self):
            return self.getToken(MiLenguajeParser.COMA, 0)

        def expresion(self):
            return self.getTypedRuleContext(MiLenguajeParser.ExpresionContext,0)


        def lista_argumentos_prima(self):
            return self.getTypedRuleContext(MiLenguajeParser.Lista_argumentos_primaContext,0)


        def getRuleIndex(self):
            return MiLenguajeParser.RULE_lista_argumentos_prima

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLista_argumentos_prima" ):
                listener.enterLista_argumentos_prima(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLista_argumentos_prima" ):
                listener.exitLista_argumentos_prima(self)




    def lista_argumentos_prima(self):

        localctx = MiLenguajeParser.Lista_argumentos_primaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_lista_argumentos_prima)
        try:
            self.state = 205
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                self.enterOuterAlt(localctx, 1)
                self.state = 200
                self.match(MiLenguajeParser.COMA)
                self.state = 201
                self.expresion()
                self.state = 202
                self.lista_argumentos_prima()
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





