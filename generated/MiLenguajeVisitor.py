# Generated from grammar/MiLenguaje.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MiLenguajeParser import MiLenguajeParser
else:
    from MiLenguajeParser import MiLenguajeParser

# This class defines a complete generic visitor for a parse tree produced by MiLenguajeParser.

class MiLenguajeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiLenguajeParser#programa.
    def visitPrograma(self, ctx:MiLenguajeParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiLenguajeParser#declaraciones.
    def visitDeclaraciones(self, ctx:MiLenguajeParser.DeclaracionesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiLenguajeParser#declaracion.
    def visitDeclaracion(self, ctx:MiLenguajeParser.DeclaracionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiLenguajeParser#tipo.
    def visitTipo(self, ctx:MiLenguajeParser.TipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiLenguajeParser#cuerpo.
    def visitCuerpo(self, ctx:MiLenguajeParser.CuerpoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiLenguajeParser#instruccion.
    def visitInstruccion(self, ctx:MiLenguajeParser.InstruccionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiLenguajeParser#asignacion.
    def visitAsignacion(self, ctx:MiLenguajeParser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiLenguajeParser#expresion.
    def visitExpresion(self, ctx:MiLenguajeParser.ExpresionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiLenguajeParser#expresion_prima.
    def visitExpresion_prima(self, ctx:MiLenguajeParser.Expresion_primaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiLenguajeParser#termino.
    def visitTermino(self, ctx:MiLenguajeParser.TerminoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiLenguajeParser#termino_prima.
    def visitTermino_prima(self, ctx:MiLenguajeParser.Termino_primaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiLenguajeParser#factor.
    def visitFactor(self, ctx:MiLenguajeParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiLenguajeParser#condicional.
    def visitCondicional(self, ctx:MiLenguajeParser.CondicionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiLenguajeParser#sino.
    def visitSino(self, ctx:MiLenguajeParser.SinoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiLenguajeParser#condicion.
    def visitCondicion(self, ctx:MiLenguajeParser.CondicionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiLenguajeParser#op_relacional.
    def visitOp_relacional(self, ctx:MiLenguajeParser.Op_relacionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiLenguajeParser#bucle.
    def visitBucle(self, ctx:MiLenguajeParser.BucleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiLenguajeParser#entrada_salida.
    def visitEntrada_salida(self, ctx:MiLenguajeParser.Entrada_salidaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiLenguajeParser#definicion_funcion.
    def visitDefinicion_funcion(self, ctx:MiLenguajeParser.Definicion_funcionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiLenguajeParser#parametros.
    def visitParametros(self, ctx:MiLenguajeParser.ParametrosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiLenguajeParser#lista_parametros.
    def visitLista_parametros(self, ctx:MiLenguajeParser.Lista_parametrosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiLenguajeParser#lista_parametros_prima.
    def visitLista_parametros_prima(self, ctx:MiLenguajeParser.Lista_parametros_primaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiLenguajeParser#llamada_funcion.
    def visitLlamada_funcion(self, ctx:MiLenguajeParser.Llamada_funcionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiLenguajeParser#argumentos.
    def visitArgumentos(self, ctx:MiLenguajeParser.ArgumentosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiLenguajeParser#lista_argumentos.
    def visitLista_argumentos(self, ctx:MiLenguajeParser.Lista_argumentosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiLenguajeParser#lista_argumentos_prima.
    def visitLista_argumentos_prima(self, ctx:MiLenguajeParser.Lista_argumentos_primaContext):
        return self.visitChildren(ctx)



del MiLenguajeParser