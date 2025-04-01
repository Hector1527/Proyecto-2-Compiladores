# Generated from MiLenguaje.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MiLenguajeParser import MiLenguajeParser
else:
    from MiLenguajeParser import MiLenguajeParser

# This class defines a complete listener for a parse tree produced by MiLenguajeParser.
class MiLenguajeListener(ParseTreeListener):

    # Enter a parse tree produced by MiLenguajeParser#programa.
    def enterPrograma(self, ctx:MiLenguajeParser.ProgramaContext):
        pass

    # Exit a parse tree produced by MiLenguajeParser#programa.
    def exitPrograma(self, ctx:MiLenguajeParser.ProgramaContext):
        pass


    # Enter a parse tree produced by MiLenguajeParser#declaraciones.
    def enterDeclaraciones(self, ctx:MiLenguajeParser.DeclaracionesContext):
        pass

    # Exit a parse tree produced by MiLenguajeParser#declaraciones.
    def exitDeclaraciones(self, ctx:MiLenguajeParser.DeclaracionesContext):
        pass


    # Enter a parse tree produced by MiLenguajeParser#declaracion.
    def enterDeclaracion(self, ctx:MiLenguajeParser.DeclaracionContext):
        pass

    # Exit a parse tree produced by MiLenguajeParser#declaracion.
    def exitDeclaracion(self, ctx:MiLenguajeParser.DeclaracionContext):
        pass


    # Enter a parse tree produced by MiLenguajeParser#tipo.
    def enterTipo(self, ctx:MiLenguajeParser.TipoContext):
        pass

    # Exit a parse tree produced by MiLenguajeParser#tipo.
    def exitTipo(self, ctx:MiLenguajeParser.TipoContext):
        pass


    # Enter a parse tree produced by MiLenguajeParser#cuerpo.
    def enterCuerpo(self, ctx:MiLenguajeParser.CuerpoContext):
        pass

    # Exit a parse tree produced by MiLenguajeParser#cuerpo.
    def exitCuerpo(self, ctx:MiLenguajeParser.CuerpoContext):
        pass


    # Enter a parse tree produced by MiLenguajeParser#instruccion.
    def enterInstruccion(self, ctx:MiLenguajeParser.InstruccionContext):
        pass

    # Exit a parse tree produced by MiLenguajeParser#instruccion.
    def exitInstruccion(self, ctx:MiLenguajeParser.InstruccionContext):
        pass


    # Enter a parse tree produced by MiLenguajeParser#asignacion.
    def enterAsignacion(self, ctx:MiLenguajeParser.AsignacionContext):
        pass

    # Exit a parse tree produced by MiLenguajeParser#asignacion.
    def exitAsignacion(self, ctx:MiLenguajeParser.AsignacionContext):
        pass


    # Enter a parse tree produced by MiLenguajeParser#expresion.
    def enterExpresion(self, ctx:MiLenguajeParser.ExpresionContext):
        pass

    # Exit a parse tree produced by MiLenguajeParser#expresion.
    def exitExpresion(self, ctx:MiLenguajeParser.ExpresionContext):
        pass


    # Enter a parse tree produced by MiLenguajeParser#expresion_prima.
    def enterExpresion_prima(self, ctx:MiLenguajeParser.Expresion_primaContext):
        pass

    # Exit a parse tree produced by MiLenguajeParser#expresion_prima.
    def exitExpresion_prima(self, ctx:MiLenguajeParser.Expresion_primaContext):
        pass


    # Enter a parse tree produced by MiLenguajeParser#termino.
    def enterTermino(self, ctx:MiLenguajeParser.TerminoContext):
        pass

    # Exit a parse tree produced by MiLenguajeParser#termino.
    def exitTermino(self, ctx:MiLenguajeParser.TerminoContext):
        pass


    # Enter a parse tree produced by MiLenguajeParser#termino_prima.
    def enterTermino_prima(self, ctx:MiLenguajeParser.Termino_primaContext):
        pass

    # Exit a parse tree produced by MiLenguajeParser#termino_prima.
    def exitTermino_prima(self, ctx:MiLenguajeParser.Termino_primaContext):
        pass


    # Enter a parse tree produced by MiLenguajeParser#factor.
    def enterFactor(self, ctx:MiLenguajeParser.FactorContext):
        pass

    # Exit a parse tree produced by MiLenguajeParser#factor.
    def exitFactor(self, ctx:MiLenguajeParser.FactorContext):
        pass


    # Enter a parse tree produced by MiLenguajeParser#condicional.
    def enterCondicional(self, ctx:MiLenguajeParser.CondicionalContext):
        pass

    # Exit a parse tree produced by MiLenguajeParser#condicional.
    def exitCondicional(self, ctx:MiLenguajeParser.CondicionalContext):
        pass


    # Enter a parse tree produced by MiLenguajeParser#sino.
    def enterSino(self, ctx:MiLenguajeParser.SinoContext):
        pass

    # Exit a parse tree produced by MiLenguajeParser#sino.
    def exitSino(self, ctx:MiLenguajeParser.SinoContext):
        pass


    # Enter a parse tree produced by MiLenguajeParser#condicion.
    def enterCondicion(self, ctx:MiLenguajeParser.CondicionContext):
        pass

    # Exit a parse tree produced by MiLenguajeParser#condicion.
    def exitCondicion(self, ctx:MiLenguajeParser.CondicionContext):
        pass


    # Enter a parse tree produced by MiLenguajeParser#op_relacional.
    def enterOp_relacional(self, ctx:MiLenguajeParser.Op_relacionalContext):
        pass

    # Exit a parse tree produced by MiLenguajeParser#op_relacional.
    def exitOp_relacional(self, ctx:MiLenguajeParser.Op_relacionalContext):
        pass


    # Enter a parse tree produced by MiLenguajeParser#bucle.
    def enterBucle(self, ctx:MiLenguajeParser.BucleContext):
        pass

    # Exit a parse tree produced by MiLenguajeParser#bucle.
    def exitBucle(self, ctx:MiLenguajeParser.BucleContext):
        pass


    # Enter a parse tree produced by MiLenguajeParser#entrada_salida.
    def enterEntrada_salida(self, ctx:MiLenguajeParser.Entrada_salidaContext):
        pass

    # Exit a parse tree produced by MiLenguajeParser#entrada_salida.
    def exitEntrada_salida(self, ctx:MiLenguajeParser.Entrada_salidaContext):
        pass


    # Enter a parse tree produced by MiLenguajeParser#definicion_funcion.
    def enterDefinicion_funcion(self, ctx:MiLenguajeParser.Definicion_funcionContext):
        pass

    # Exit a parse tree produced by MiLenguajeParser#definicion_funcion.
    def exitDefinicion_funcion(self, ctx:MiLenguajeParser.Definicion_funcionContext):
        pass


    # Enter a parse tree produced by MiLenguajeParser#parametros.
    def enterParametros(self, ctx:MiLenguajeParser.ParametrosContext):
        pass

    # Exit a parse tree produced by MiLenguajeParser#parametros.
    def exitParametros(self, ctx:MiLenguajeParser.ParametrosContext):
        pass


    # Enter a parse tree produced by MiLenguajeParser#lista_parametros.
    def enterLista_parametros(self, ctx:MiLenguajeParser.Lista_parametrosContext):
        pass

    # Exit a parse tree produced by MiLenguajeParser#lista_parametros.
    def exitLista_parametros(self, ctx:MiLenguajeParser.Lista_parametrosContext):
        pass


    # Enter a parse tree produced by MiLenguajeParser#lista_parametros_prima.
    def enterLista_parametros_prima(self, ctx:MiLenguajeParser.Lista_parametros_primaContext):
        pass

    # Exit a parse tree produced by MiLenguajeParser#lista_parametros_prima.
    def exitLista_parametros_prima(self, ctx:MiLenguajeParser.Lista_parametros_primaContext):
        pass


    # Enter a parse tree produced by MiLenguajeParser#llamada_funcion.
    def enterLlamada_funcion(self, ctx:MiLenguajeParser.Llamada_funcionContext):
        pass

    # Exit a parse tree produced by MiLenguajeParser#llamada_funcion.
    def exitLlamada_funcion(self, ctx:MiLenguajeParser.Llamada_funcionContext):
        pass


    # Enter a parse tree produced by MiLenguajeParser#argumentos.
    def enterArgumentos(self, ctx:MiLenguajeParser.ArgumentosContext):
        pass

    # Exit a parse tree produced by MiLenguajeParser#argumentos.
    def exitArgumentos(self, ctx:MiLenguajeParser.ArgumentosContext):
        pass


    # Enter a parse tree produced by MiLenguajeParser#lista_argumentos.
    def enterLista_argumentos(self, ctx:MiLenguajeParser.Lista_argumentosContext):
        pass

    # Exit a parse tree produced by MiLenguajeParser#lista_argumentos.
    def exitLista_argumentos(self, ctx:MiLenguajeParser.Lista_argumentosContext):
        pass


    # Enter a parse tree produced by MiLenguajeParser#lista_argumentos_prima.
    def enterLista_argumentos_prima(self, ctx:MiLenguajeParser.Lista_argumentos_primaContext):
        pass

    # Exit a parse tree produced by MiLenguajeParser#lista_argumentos_prima.
    def exitLista_argumentos_prima(self, ctx:MiLenguajeParser.Lista_argumentos_primaContext):
        pass



del MiLenguajeParser