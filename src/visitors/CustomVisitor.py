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
        if ctx.expresion():
            value = self.visit(ctx.expresion())
            self.symbol_table[var_name] = value
        else:
            self.symbol_table[var_name] = 0
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
        self.symbol_table[var_name] = value
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
                raise TypeError(f"No se puede operar entre {type(left_value).__name__} y {type(delta).__name__}")
            self._print_node_info("EXPRESION", f"Resultado: {result}")
            return result
        else:
            self._print_node_info("EXPRESION", f"Resultado: {left_value}")
            return left_value

    def visitExpresion_prima(self, ctx: MiLenguajeParser.Expresion_primaContext):
        if ctx.getChildCount() == 0:
            return 0
        op = ctx.getChild(0).getText()
        term_value = self.visit(ctx.termino())
        delta = self.visit(ctx.expresion_prima())
        if not isinstance(term_value, (int, float)) or not isinstance(delta, (int, float)):
            raise TypeError(f"No se puede operar entre {type(term_value).__name__} y {type(delta).__name__}")
        return term_value + delta if op == '+' else term_value - delta

    def visitTermino(self, ctx: MiLenguajeParser.TerminoContext):
        left_value = self.visit(ctx.factor())
        if ctx.termino_prima() and ctx.termino_prima().getChildCount() > 0:
            right_value = self.visit(ctx.termino_prima())
            if isinstance(left_value, (int, float)) and isinstance(right_value, (int, float)):
                result = left_value * right_value
            else:
                raise TypeError(f"No se puede multiplicar/dividir {type(left_value).__name__} con {type(right_value).__name__}")
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
            raise TypeError(f"No se puede multiplicar/dividir {type(factor_value).__name__} con {type(next_value).__name__}")
        if op == '*': return factor_value * next_value
        elif op == '/': return factor_value / next_value
        elif op == '%': return factor_value % next_value
        return 1

    def visitFactor(self, ctx: MiLenguajeParser.FactorContext):
        if ctx.NUMERO():
            num_str = ctx.NUMERO().getText()
            result = float(num_str) if '.' in num_str else int(num_str)
            content = f"Número: {num_str}"
        elif ctx.ID():
            var_name = ctx.ID().getText()
            if var_name not in self.symbol_table:
                self._print_node_info("ERROR SEMÁNTICO", f"La variable '{var_name}' no ha sido declarada.")
                result = None
            else:
                result = self.symbol_table[var_name]
            content = f"Variable: {var_name}"
        elif ctx.CADENA_LITERAL():
            text_raw = ctx.CADENA_LITERAL().getText()
            result = text_raw.strip('"')
            content = f"Cadena: {text_raw}"
        elif ctx.BOOLEAN_LITERAL():
            bool_str = ctx.BOOLEAN_LITERAL().getText()
            result = bool_str == "verdadero"
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

    def visitCondicional(self, ctx: MiLenguajeParser.CondicionalContext):
        self._print_node_info("CONDICIONAL", "Evaluando condición del if")
        self.indent_level += 1
        if self._eval_condition(ctx.condicion()):
            self._print_node_info("CONDICIONAL", "Condición verdadera, ejecutando bloque if")
            self.visit(ctx.cuerpo(0))
        elif ctx.sino():
            self._print_node_info("CONDICIONAL", "Condición falsa, ejecutando bloque else")
            self.visit(ctx.sino())
        self.indent_level -= 1
        return None

    def visitSino(self, ctx: MiLenguajeParser.SinoContext):
        if ctx.cuerpo():
            self._print_node_info("SINO", "Ejecutando cuerpo del else")
            self.indent_level += 1
            self.visit(ctx.cuerpo())
            self.indent_level -= 1
        return None

    def visitBucle(self, ctx: MiLenguajeParser.BucleContext):
        self._print_node_info("BUCLE", "Evaluando condición del while")
        self.indent_level += 1
        while self._eval_condition(ctx.condicion()):
            self._print_node_info("BUCLE", "Ejecutando cuerpo")
            self.visit(ctx.cuerpo())
        self.indent_level -= 1
        return None

    def _eval_condition(self, ctx):
        left = self.visit(ctx.expresion(0))
        right = self.visit(ctx.expresion(1))
        op = ctx.op_relacional().getText()

        if op == '==': return left == right
        elif op == '!=': return left != right
        elif op == '>': return left > right
        elif op == '<': return left < right
        elif op == '>=': return left >= right
        elif op == '<=': return left <= right
        else:
            self._print_node_info("ERROR SEMÁNTICO", f"Operador relacional no reconocido: {op}")
            return False
