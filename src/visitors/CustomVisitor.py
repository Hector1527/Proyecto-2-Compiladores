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

    # Métodos de visita para cada regla gramatical
    def visitPrograma(self, ctx: MiLenguajeParser.ProgramaContext):
        self._print_node_info("PROGRAMA")
        self.indent_level += 1
        self.visitChildren(ctx)
        self.indent_level -= 1
        return None

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

    def visitAsignacion(self, ctx: MiLenguajeParser.AsignacionContext):
        var_name = ctx.ID().getText()
        self._print_node_info("ASIGNACION", f"Variable: {var_name}")
        self.indent_level += 1
        self.visitChildren(ctx)
        self.indent_level -= 1
        return None

    def visitExpresion(self, ctx: MiLenguajeParser.ExpresionContext):
        self._print_node_info("EXPRESION")
        self.indent_level += 1
        result = self.visitChildren(ctx)
        self.indent_level -= 1
        return result

    def visitTermino(self, ctx: MiLenguajeParser.TerminoContext):
        self._print_node_info("TERMINO")
        self.indent_level += 1
        result = self.visitChildren(ctx)
        self.indent_level -= 1
        return result

    def visitFactor(self, ctx: MiLenguajeParser.FactorContext):
        if ctx.NUMERO():
            content = f"Número: {ctx.NUMERO().getText()}"
        elif ctx.ID():
            content = f"Variable: {ctx.ID().getText()}"
        elif ctx.CADENA_LITERAL():
            content = f"Cadena: {ctx.CADENA_LITERAL().getText()}"
        elif ctx.BOOLEAN():
            content = f"Booleano: {ctx.BOOLEAN().getText()}"
        elif ctx.expresion():
            content = "Expresión entre paréntesis"
        else:
            content = "Tipo desconocido"
        
        self._print_node_info("FACTOR", content)
        return self.visitChildren(ctx)

    def visitEntrada_salida(self, ctx: MiLenguajeParser.Entrada_salidaContext):
        if ctx.LEER():
            self._print_node_info("LEER", f"Variable: {ctx.ID().getText()}")
        else:
            self._print_node_info("ESCRIBIR")
        self.indent_level += 1
        self.visitChildren(ctx)
        self.indent_level -= 1
        return None

