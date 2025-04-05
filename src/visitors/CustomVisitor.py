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
        value = self.visit(ctx.expresion())
        self._print_node_info("ASIGNACION", f"Valor calculado: {value}")
        self.indent_level -= 1
        return None

    def visitExpresion(self, ctx: MiLenguajeParser.ExpresionContext):
        left_value = self.visit(ctx.termino())

        if ctx.expresion_prima() and ctx.expresion_prima().getChildCount() > 0:
            delta = self.visit(ctx.expresion_prima())
            if isinstance(left_value, (int, float)) and isinstance(delta, (int, float)):
                result = left_value + delta
            else:
                raise TypeError(
                    f"No se puede operar entre {type(left_value).__name__} y {type(delta).__name__}"
                )
            self._print_node_info("EXPRESION", f"Resultado: {result}")
            return result
        else:
            self._print_node_info("EXPRESION", f"Resultado: {left_value}")
            return left_value

    def visitExpresion_prima(self, ctx: MiLenguajeParser.Expresion_primaContext):
        if ctx.getChildCount() == 0:
            return 0

        op = ctx.getChild(0).getText()  # '+' o '-'
        term_value = self.visit(ctx.termino())
        delta = self.visit(ctx.expresion_prima())

        if not isinstance(term_value, (int, float)) or not isinstance(delta, (int, float)):
            raise TypeError(
                f"No se puede operar entre {type(term_value).__name__} y {type(delta).__name__}"
            )

        if op == '+':
            return term_value + delta
        else:  # op == '-'
            return term_value - delta

    def visitTermino(self, ctx: MiLenguajeParser.TerminoContext):
        left_value = self.visit(ctx.factor())
        if ctx.termino_prima() and ctx.termino_prima().getChildCount() > 0:
            right_value = self.visit(ctx.termino_prima())
            if isinstance(left_value, (int, float)) and isinstance(right_value, (int, float)):
                result = left_value * right_value
            else:
                raise TypeError(
                    f"No se puede multiplicar/dividir {type(left_value).__name__} con {type(right_value).__name__}"
                )
            self._print_node_info("TERMINO", f"Resultado: {result}")
            return result
        else:
            self._print_node_info("TERMINO", f"Resultado: {left_value}")
            return left_value

    def visitTermino_prima(self, ctx: MiLenguajeParser.Termino_primaContext):
        if ctx.getChildCount() == 0:
            return 1 

        op = ctx.getChild(0).getText()
        factor_value = self.visit(ctx.factor())
        next_value = self.visit(ctx.termino_prima())

        if not isinstance(factor_value, (int, float)) or not isinstance(next_value, (int, float)):
            raise TypeError(
                f"No se puede multiplicar/dividir {type(factor_value).__name__} con {type(next_value).__name__}"
            )

        if op == '*':
            return factor_value * next_value
        elif op == '/':
            return factor_value / next_value
        elif op == '%':
            return factor_value % next_value
        else:
            return 1

    def visitFactor(self, ctx: MiLenguajeParser.FactorContext):
        if ctx.NUMERO():
            num_str = ctx.NUMERO().getText()
            if '.' in num_str:
                result = float(num_str)
            else:
                result = int(num_str)
            content = f"Número: {num_str}"

        elif ctx.ID():
            var_name = ctx.ID().getText()
            content = f"Variable: {var_name}"
            result = self.symbol_table.get(var_name, 0)

        elif ctx.CADENA_LITERAL():
            text_raw = ctx.CADENA_LITERAL().getText()
            text_clean = text_raw.strip('"')
            content = f"Cadena: {text_raw}"
            result = text_clean

        elif ctx.BOOLEAN_LITERAL():
            bool_str = ctx.BOOLEAN_LITERAL().getText()
            result = True if bool_str == "verdadero" else False
            content = f"Booleano: {bool_str}"

        elif ctx.expresion():
            content = "Expresión entre paréntesis"
            result = self.visit(ctx.expresion())

        else:
            content = "Tipo desconocido"
            result = None

        self._print_node_info("FACTOR", content)
        return result

    def visitEntrada_salida(self, ctx: MiLenguajeParser.Entrada_salidaContext):
        if ctx.LEER():
            var_name = ctx.ID().getText()
            self._print_node_info("LEER", f"Variable: {var_name}")
            return None
        elif ctx.ESCRIBIR():
            val = self.visit(ctx.expresion())
            self._print_node_info("ESCRIBIR", f"Valor: {val}")
            return val

