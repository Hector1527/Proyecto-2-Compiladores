// Generated from grammar/MiLenguaje.g4 by ANTLR 4.13.2
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link MiLenguajeParser}.
 */
public interface MiLenguajeListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link MiLenguajeParser#programa}.
	 * @param ctx the parse tree
	 */
	void enterPrograma(MiLenguajeParser.ProgramaContext ctx);
	/**
	 * Exit a parse tree produced by {@link MiLenguajeParser#programa}.
	 * @param ctx the parse tree
	 */
	void exitPrograma(MiLenguajeParser.ProgramaContext ctx);
	/**
	 * Enter a parse tree produced by {@link MiLenguajeParser#declaraciones}.
	 * @param ctx the parse tree
	 */
	void enterDeclaraciones(MiLenguajeParser.DeclaracionesContext ctx);
	/**
	 * Exit a parse tree produced by {@link MiLenguajeParser#declaraciones}.
	 * @param ctx the parse tree
	 */
	void exitDeclaraciones(MiLenguajeParser.DeclaracionesContext ctx);
	/**
	 * Enter a parse tree produced by {@link MiLenguajeParser#declaracion}.
	 * @param ctx the parse tree
	 */
	void enterDeclaracion(MiLenguajeParser.DeclaracionContext ctx);
	/**
	 * Exit a parse tree produced by {@link MiLenguajeParser#declaracion}.
	 * @param ctx the parse tree
	 */
	void exitDeclaracion(MiLenguajeParser.DeclaracionContext ctx);
	/**
	 * Enter a parse tree produced by {@link MiLenguajeParser#tipo}.
	 * @param ctx the parse tree
	 */
	void enterTipo(MiLenguajeParser.TipoContext ctx);
	/**
	 * Exit a parse tree produced by {@link MiLenguajeParser#tipo}.
	 * @param ctx the parse tree
	 */
	void exitTipo(MiLenguajeParser.TipoContext ctx);
	/**
	 * Enter a parse tree produced by {@link MiLenguajeParser#cuerpo}.
	 * @param ctx the parse tree
	 */
	void enterCuerpo(MiLenguajeParser.CuerpoContext ctx);
	/**
	 * Exit a parse tree produced by {@link MiLenguajeParser#cuerpo}.
	 * @param ctx the parse tree
	 */
	void exitCuerpo(MiLenguajeParser.CuerpoContext ctx);
	/**
	 * Enter a parse tree produced by {@link MiLenguajeParser#instruccion}.
	 * @param ctx the parse tree
	 */
	void enterInstruccion(MiLenguajeParser.InstruccionContext ctx);
	/**
	 * Exit a parse tree produced by {@link MiLenguajeParser#instruccion}.
	 * @param ctx the parse tree
	 */
	void exitInstruccion(MiLenguajeParser.InstruccionContext ctx);
	/**
	 * Enter a parse tree produced by {@link MiLenguajeParser#asignacion}.
	 * @param ctx the parse tree
	 */
	void enterAsignacion(MiLenguajeParser.AsignacionContext ctx);
	/**
	 * Exit a parse tree produced by {@link MiLenguajeParser#asignacion}.
	 * @param ctx the parse tree
	 */
	void exitAsignacion(MiLenguajeParser.AsignacionContext ctx);
	/**
	 * Enter a parse tree produced by {@link MiLenguajeParser#expresion}.
	 * @param ctx the parse tree
	 */
	void enterExpresion(MiLenguajeParser.ExpresionContext ctx);
	/**
	 * Exit a parse tree produced by {@link MiLenguajeParser#expresion}.
	 * @param ctx the parse tree
	 */
	void exitExpresion(MiLenguajeParser.ExpresionContext ctx);
	/**
	 * Enter a parse tree produced by {@link MiLenguajeParser#expresion_prima}.
	 * @param ctx the parse tree
	 */
	void enterExpresion_prima(MiLenguajeParser.Expresion_primaContext ctx);
	/**
	 * Exit a parse tree produced by {@link MiLenguajeParser#expresion_prima}.
	 * @param ctx the parse tree
	 */
	void exitExpresion_prima(MiLenguajeParser.Expresion_primaContext ctx);
	/**
	 * Enter a parse tree produced by {@link MiLenguajeParser#termino}.
	 * @param ctx the parse tree
	 */
	void enterTermino(MiLenguajeParser.TerminoContext ctx);
	/**
	 * Exit a parse tree produced by {@link MiLenguajeParser#termino}.
	 * @param ctx the parse tree
	 */
	void exitTermino(MiLenguajeParser.TerminoContext ctx);
	/**
	 * Enter a parse tree produced by {@link MiLenguajeParser#termino_prima}.
	 * @param ctx the parse tree
	 */
	void enterTermino_prima(MiLenguajeParser.Termino_primaContext ctx);
	/**
	 * Exit a parse tree produced by {@link MiLenguajeParser#termino_prima}.
	 * @param ctx the parse tree
	 */
	void exitTermino_prima(MiLenguajeParser.Termino_primaContext ctx);
	/**
	 * Enter a parse tree produced by {@link MiLenguajeParser#factor}.
	 * @param ctx the parse tree
	 */
	void enterFactor(MiLenguajeParser.FactorContext ctx);
	/**
	 * Exit a parse tree produced by {@link MiLenguajeParser#factor}.
	 * @param ctx the parse tree
	 */
	void exitFactor(MiLenguajeParser.FactorContext ctx);
	/**
	 * Enter a parse tree produced by {@link MiLenguajeParser#condicional}.
	 * @param ctx the parse tree
	 */
	void enterCondicional(MiLenguajeParser.CondicionalContext ctx);
	/**
	 * Exit a parse tree produced by {@link MiLenguajeParser#condicional}.
	 * @param ctx the parse tree
	 */
	void exitCondicional(MiLenguajeParser.CondicionalContext ctx);
	/**
	 * Enter a parse tree produced by {@link MiLenguajeParser#sino}.
	 * @param ctx the parse tree
	 */
	void enterSino(MiLenguajeParser.SinoContext ctx);
	/**
	 * Exit a parse tree produced by {@link MiLenguajeParser#sino}.
	 * @param ctx the parse tree
	 */
	void exitSino(MiLenguajeParser.SinoContext ctx);
	/**
	 * Enter a parse tree produced by {@link MiLenguajeParser#condicion}.
	 * @param ctx the parse tree
	 */
	void enterCondicion(MiLenguajeParser.CondicionContext ctx);
	/**
	 * Exit a parse tree produced by {@link MiLenguajeParser#condicion}.
	 * @param ctx the parse tree
	 */
	void exitCondicion(MiLenguajeParser.CondicionContext ctx);
	/**
	 * Enter a parse tree produced by {@link MiLenguajeParser#op_relacional}.
	 * @param ctx the parse tree
	 */
	void enterOp_relacional(MiLenguajeParser.Op_relacionalContext ctx);
	/**
	 * Exit a parse tree produced by {@link MiLenguajeParser#op_relacional}.
	 * @param ctx the parse tree
	 */
	void exitOp_relacional(MiLenguajeParser.Op_relacionalContext ctx);
	/**
	 * Enter a parse tree produced by {@link MiLenguajeParser#bucle}.
	 * @param ctx the parse tree
	 */
	void enterBucle(MiLenguajeParser.BucleContext ctx);
	/**
	 * Exit a parse tree produced by {@link MiLenguajeParser#bucle}.
	 * @param ctx the parse tree
	 */
	void exitBucle(MiLenguajeParser.BucleContext ctx);
	/**
	 * Enter a parse tree produced by {@link MiLenguajeParser#entrada_salida}.
	 * @param ctx the parse tree
	 */
	void enterEntrada_salida(MiLenguajeParser.Entrada_salidaContext ctx);
	/**
	 * Exit a parse tree produced by {@link MiLenguajeParser#entrada_salida}.
	 * @param ctx the parse tree
	 */
	void exitEntrada_salida(MiLenguajeParser.Entrada_salidaContext ctx);
	/**
	 * Enter a parse tree produced by {@link MiLenguajeParser#definicion_funcion}.
	 * @param ctx the parse tree
	 */
	void enterDefinicion_funcion(MiLenguajeParser.Definicion_funcionContext ctx);
	/**
	 * Exit a parse tree produced by {@link MiLenguajeParser#definicion_funcion}.
	 * @param ctx the parse tree
	 */
	void exitDefinicion_funcion(MiLenguajeParser.Definicion_funcionContext ctx);
	/**
	 * Enter a parse tree produced by {@link MiLenguajeParser#parametros}.
	 * @param ctx the parse tree
	 */
	void enterParametros(MiLenguajeParser.ParametrosContext ctx);
	/**
	 * Exit a parse tree produced by {@link MiLenguajeParser#parametros}.
	 * @param ctx the parse tree
	 */
	void exitParametros(MiLenguajeParser.ParametrosContext ctx);
	/**
	 * Enter a parse tree produced by {@link MiLenguajeParser#lista_parametros}.
	 * @param ctx the parse tree
	 */
	void enterLista_parametros(MiLenguajeParser.Lista_parametrosContext ctx);
	/**
	 * Exit a parse tree produced by {@link MiLenguajeParser#lista_parametros}.
	 * @param ctx the parse tree
	 */
	void exitLista_parametros(MiLenguajeParser.Lista_parametrosContext ctx);
	/**
	 * Enter a parse tree produced by {@link MiLenguajeParser#lista_parametros_prima}.
	 * @param ctx the parse tree
	 */
	void enterLista_parametros_prima(MiLenguajeParser.Lista_parametros_primaContext ctx);
	/**
	 * Exit a parse tree produced by {@link MiLenguajeParser#lista_parametros_prima}.
	 * @param ctx the parse tree
	 */
	void exitLista_parametros_prima(MiLenguajeParser.Lista_parametros_primaContext ctx);
	/**
	 * Enter a parse tree produced by {@link MiLenguajeParser#llamada_funcion}.
	 * @param ctx the parse tree
	 */
	void enterLlamada_funcion(MiLenguajeParser.Llamada_funcionContext ctx);
	/**
	 * Exit a parse tree produced by {@link MiLenguajeParser#llamada_funcion}.
	 * @param ctx the parse tree
	 */
	void exitLlamada_funcion(MiLenguajeParser.Llamada_funcionContext ctx);
	/**
	 * Enter a parse tree produced by {@link MiLenguajeParser#argumentos}.
	 * @param ctx the parse tree
	 */
	void enterArgumentos(MiLenguajeParser.ArgumentosContext ctx);
	/**
	 * Exit a parse tree produced by {@link MiLenguajeParser#argumentos}.
	 * @param ctx the parse tree
	 */
	void exitArgumentos(MiLenguajeParser.ArgumentosContext ctx);
	/**
	 * Enter a parse tree produced by {@link MiLenguajeParser#lista_argumentos}.
	 * @param ctx the parse tree
	 */
	void enterLista_argumentos(MiLenguajeParser.Lista_argumentosContext ctx);
	/**
	 * Exit a parse tree produced by {@link MiLenguajeParser#lista_argumentos}.
	 * @param ctx the parse tree
	 */
	void exitLista_argumentos(MiLenguajeParser.Lista_argumentosContext ctx);
	/**
	 * Enter a parse tree produced by {@link MiLenguajeParser#lista_argumentos_prima}.
	 * @param ctx the parse tree
	 */
	void enterLista_argumentos_prima(MiLenguajeParser.Lista_argumentos_primaContext ctx);
	/**
	 * Exit a parse tree produced by {@link MiLenguajeParser#lista_argumentos_prima}.
	 * @param ctx the parse tree
	 */
	void exitLista_argumentos_prima(MiLenguajeParser.Lista_argumentos_primaContext ctx);
}