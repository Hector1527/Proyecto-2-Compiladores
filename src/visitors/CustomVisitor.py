from MiLenguajeVisitor import MiLenguajeVisitor
from MiLenguajeParser import MiLenguajeParser

class CustomVisitor(MiLenguajeVisitor):
    def __init__(self):
        self.symbol_table = {}
        self.current_scope = "global"
        self.indent_level = 0

    def _print_node_info(self, node_name, content=""):
        indent = "  " * self.indent_level
        print(f"{indent}[VISITANDO {node_name}] {content}")

    # Método para "programa"
    def visitPrograma(self, ctx: MiLenguajeParser.ProgramaContext):
        self._print_node_info("PROGRAMA")
        self.indent_level += 1
        self.visitChildren(ctx)
        self.indent_level -= 1
        return None

    # Declaración y tipo
    def visitDeclaracion(self, ctx: MiLenguajeParser.DeclaracionContext):
        var_type = ctx.tipo().getText()
        var_name = ctx.ID().getText()
        self._print_node_info("DECLARACION", f"Tipo: {var_type}, Nombre: {var_name}")
        self.indent_level += 1
        self.visitChildren(ctx)
        self.indent_level -= 1
        return None

    def visitTipo(self, ctx: MiLenguajeParser.TipoContext):
        tipo = ctx.getText()
        self._print_node_info("TIPO", tipo)
        return None

    # Asignación
    def visitAsignacion(self, ctx: MiLenguajeParser.AsignacionContext):
        var_name = ctx.ID().getText()
        self._print_node_info("ASIGNACION", f"Variable: {var_name}")
        self.indent_level += 1
        self.visitChildren(ctx)
        self.indent_level -= 1
        return None

    # EXPRESIONES (Operaciones aritméticas)
    def visitExpresion(self, ctx: MiLenguajeParser.ExpresionContext):
        left_value = self.visit(ctx.termino())
        delta = self.visit(ctx.expresion_prima())
        result = left_value + delta
        self._print_node_info("EXPRESION", f"Resultado: {result}")
        return result

    # Regla: expresion_prima: (SUMA | RESTA) termino expresion_prima | ;
    def visitExpresion_prima(self, ctx: MiLenguajeParser.Expresion_primaContext):
        if ctx.getChildCount() == 0:
            return 0
        op = ctx.getChild(0).getText()
        term_value = self.visit(ctx.termino())
        delta = self.visit(ctx.expresion_prima())
        if op == '+':
            return term_value + delta
        elif op == '-':
            return -term_value + delta

    # La regla: termino: factor termino_prima;
    def visitTermino(self, ctx: MiLenguajeParser.TerminoContext):
        left_value = self.visit(ctx.factor())
        result = self._visitTermino_prima(ctx.termino_prima(), left_value)
        self._print_node_info("TERMINO", f"Resultado: {result}")
        return result

    # Helper recursivo para evaluar la parte derecha de la multiplicación/división
    def _visitTermino_prima(self, ctx, inherited):
        if ctx.getChildCount() == 0:
            return inherited
        op = ctx.getChild(0).getText()
        factor_value = self.visit(ctx.factor())
        if op == '*':
            new_value = inherited * factor_value
        elif op == '/':
            new_value = inherited / factor_value
        elif op == '%':
            new_value = inherited % factor_value
        else:
            new_value = inherited
        return self._visitTermino_prima(ctx.termino_prima(), new_value)

    # Aunque no es estrictamente necesario, definimos visitTermino_prima delegando en el helper.
    def visitTermino_prima(self, ctx: MiLenguajeParser.Termino_primaContext):
        return self._visitTermino_prima(ctx, 1)

    # Factor (números, identificadores, cadenas, booleanos o expresión entre paréntesis)
    def visitFactor(self, ctx: MiLenguajeParser.FactorContext):
        if ctx.NUMERO():
            content = f"Número: {ctx.NUMERO().getText()}"
            result = float(ctx.NUMERO().getText())
        elif ctx.ID():
            content = f"Variable: {ctx.ID().getText()}"
            result = 0
        elif ctx.CADENA_LITERAL():
            content = f"Cadena: {ctx.CADENA_LITERAL().getText()}"
            result = ctx.CADENA_LITERAL().getText()
        elif ctx.BOOLEAN_LITERAL():
            content = f"Booleano: {ctx.BOOLEAN_LITERAL().getText()}"
            result = True if ctx.BOOLEAN_LITERAL().getText() == "verdadero" else False
        elif ctx.expresion():
            content = "Expresión entre paréntesis"
            result = self.visit(ctx.expresion())
        else:
            content = "Tipo desconocido"
            result = None
        
        self._print_node_info("FACTOR", content)
        return result

    # Entrada/Salida
    def visitEntrada_salida(self, ctx: MiLenguajeParser.Entrada_salidaContext):
        if ctx.LEER():
            self._print_node_info("LEER", f"Variable: {ctx.ID().getText()}")
        else:
            self._print_node_info("ESCRIBIR")
        self.indent_level += 1
        self.visitChildren(ctx)
        self.indent_level -= 1
        return None
