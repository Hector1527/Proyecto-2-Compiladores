from MiLenguajeVisitor import MiLenguajeVisitor
from MiLenguajeParser import MiLenguajeParser

class CustomVisitor(MiLenguajeVisitor):
    def __init__(self):
        self.symbol_table = {
            'escribir': {
                'type': 'funcion',
                'params': [{'type': 'any', 'name': 'valor'}],
                'body': None,
                'scope': 'global'
            }
        }
        self.current_scope = "global"
        self.errors = []
        self.warnings = []            
        self.function_defs = {}
        self.scope_stack = []
        self.indent_level = 0

    # ------------------------------------------------------------------
    def _print_node_info(self, node_name, content=""):
        indent = "  " * self.indent_level
        print(f"{indent}[VISITANDO {node_name}] {content}")

    def _add_error(self, message, ctx=None):
        self.errors.append(message)
        self._print_node_info("ERROR", message)

    def _add_warning(self, message, ctx=None): 
        self.warnings.append(message)
        self._print_node_info("ADVERTENCIA", message)

    # ------------------------------------------------------------------
    def visitPrograma(self, ctx: MiLenguajeParser.ProgramaContext):
        self._print_node_info("PROGRAMA")
        self.indent_level += 1
        self.visitChildren(ctx)
        self.indent_level -= 1
        return None

    def visitDeclaracion(self, ctx: MiLenguajeParser.DeclaracionContext):
        var_type = ctx.tipo().getText()
        var_name = ctx.ID().getText()
        default_value = 0.0 if var_type == 'decimal' else 0
        var_info = {
            'type': var_type,
            'value': default_value,
            'scope': self.current_scope,
            'initialized': False
        }
        if ctx.expresion():
            value = self.visit(ctx.expresion())
            if (var_type == 'entero' and not isinstance(value, int)) or \
               (var_type == 'decimal' and not isinstance(value, (int, float))):
                self._add_error(f"Tipo incorrecto para variable '{var_name}'", ctx)
            else:
                var_info['value'] = value
                var_info['initialized'] = True
        self.symbol_table[var_name] = var_info
        return None

    def visitTipo(self, ctx: MiLenguajeParser.TipoContext):
        self._print_node_info("TIPO", ctx.getText())
        return None

    def visitAsignacion(self, ctx: MiLenguajeParser.AsignacionContext):
        var_name = ctx.ID().getText()
        value = self.visit(ctx.expresion())
        if var_name not in self.symbol_table:
            self._add_error(f"Variable '{var_name}' no declarada", ctx)
            return None
        var_info = self.symbol_table[var_name]
        if (var_info['type'] == 'entero' and not isinstance(value, int)) or \
           (var_info['type'] == 'decimal' and not isinstance(value, (int, float))):
            self._add_error(f"Tipo incorrecto en asignación para '{var_name}'", ctx)
        else:
            var_info['value'] = value
            var_info['initialized'] = True
        return None

    # ------------- EXPRESIONES -------------
    def visitExpresion(self, ctx: MiLenguajeParser.ExpresionContext):
        left_value = self.visit(ctx.termino())
        if ctx.expresion_prima() and ctx.expresion_prima().getChildCount() > 0:
            delta = self.visit(ctx.expresion_prima())
            if isinstance(left_value, (int, float)) and isinstance(delta, (int, float)):
                result = left_value + delta
            else:
                raise TypeError("Tipos incompatibles en + / -")
            self._print_node_info("EXPRESION", f"Resultado: {result}")
            return result
        self._print_node_info("EXPRESION", f"Resultado: {left_value}")
        return left_value

    def visitExpresion_prima(self, ctx: MiLenguajeParser.Expresion_primaContext):
        if ctx.getChildCount() == 0:
            return 0
        op = ctx.getChild(0).getText()
        term_value = self.visit(ctx.termino())
        delta = self.visit(ctx.expresion_prima())
        if not isinstance(term_value, (int, float)) or not isinstance(delta, (int, float)):
            raise TypeError("Tipos incompatibles en + / -")
        return term_value + delta if op == '+' else term_value - delta

    def visitTermino(self, ctx: MiLenguajeParser.TerminoContext):
        left_value = self.visit(ctx.factor())
        if ctx.termino_prima() and ctx.termino_prima().getChildCount() > 0:
            right_value = self.visit(ctx.termino_prima())
            if isinstance(left_value, (int, float)) and isinstance(right_value, (int, float)):
                result = left_value * right_value
            else:
                raise TypeError("Tipos incompatibles en *, /, %")
            self._print_node_info("TERMINO", f"Resultado: {result}")
            return result
        self._print_node_info("TERMINO", f"Resultado: {left_value}")
        return left_value

    def visitTermino_prima(self, ctx: MiLenguajeParser.Termino_primaContext):
        if ctx.getChildCount() == 0:
            return 1
        op = ctx.getChild(0).getText()
        factor_value = self.visit(ctx.factor())
        next_value = self.visit(ctx.termino_prima())
        if not isinstance(factor_value, (int, float)) or not isinstance(next_value, (int, float)):
            raise TypeError("Tipos incompatibles en *, /, %")
        if op == '*': return factor_value * next_value
        if op == '/': return factor_value / next_value
        if op == '%': return factor_value % next_value
        return 1

    def visitFactor(self, ctx: MiLenguajeParser.FactorContext):
        if ctx.NUMERO():
            num_str = ctx.NUMERO().getText()
            result = float(num_str) if '.' in num_str else int(num_str)
            content = f"Número: {num_str}"
        elif ctx.ID():
            var_name = ctx.ID().getText()
            for scope in [self.current_scope] + self.scope_stack:
                if var_name in self.symbol_table and self.symbol_table[var_name]['scope'] == scope:
                    return self.symbol_table[var_name]['value']
            self._add_error(f"Variable '{var_name}' no declarada", ctx)
            return None
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

    # ------------- E/S -------------
    def visitEntrada_salida(self, ctx: MiLenguajeParser.Entrada_salidaContext):
        if ctx.LEER():
            var_name = ctx.ID().getText()
            self._print_node_info("LEER", f"Variable: {var_name}")
            return None
        val = self.visit(ctx.expresion())
        self._print_node_info("ESCRIBIR", f"Valor: {val}")
        return val

    # ------------- IF / ELSE -------------
    def visitCondicional(self, ctx: MiLenguajeParser.CondicionalContext):
        self._print_node_info("CONDICIONAL", "Evaluando condición del if")
        self.indent_level += 1
        if self._eval_condition(ctx.condicion()):
            self._print_node_info("CONDICIONAL", "Condición verdadera, ejecutando bloque if")
            self.visit(ctx.cuerpo())            # ← CAMBIO
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

    # ------------- WHILE -------------
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
        return {
            '==': left == right,
            '!=': left != right,
            '>':  left > right,
            '<':  left < right,
            '>=': left >= right,
            '<=': left <= right
        }.get(op, False)

    # ------------- FUNCIONES -------------
    def visitDefinicion_funcion(self, ctx: MiLenguajeParser.Definicion_funcionContext):
        func_name = ctx.ID().getText()
        self.function_defs[func_name] = {
            'params': self.visit(ctx.parametros()) if ctx.parametros() else [],
            'body': ctx.cuerpo(),
            'scope': self.current_scope
        }
        self.symbol_table[func_name] = {
            'type': 'funcion',
            'params': self.function_defs[func_name]['params'],
            'scope': self.current_scope
        }
        print(f"[DEFINICIÓN FUNCIÓN] {func_name}")
        return None

    def visitParametros(self, ctx: MiLenguajeParser.ParametrosContext):
        if ctx.lista_parametros():
            return self.visit(ctx.lista_parametros())
        return []

    def visitLista_parametros(self, ctx: MiLenguajeParser.Lista_parametrosContext):
        params = [{'type': ctx.tipo().getText(), 'name': ctx.ID().getText()}]
        if ctx.lista_parametros_prima():
            params += self.visit(ctx.lista_parametros_prima())
        return params

    def visitLista_parametros_prima(self, ctx: MiLenguajeParser.Lista_parametros_primaContext):
        if ctx.getChildCount() == 0:
            return []
        return [{'type': ctx.tipo().getText(), 'name': ctx.ID().getText()}] + \
               self.visit(ctx.lista_parametros_prima())

    def visitLlamada_funcion(self, ctx: MiLenguajeParser.Llamada_funcionContext):
        func_name = ctx.ID().getText()
        if func_name not in self.function_defs:
            self._add_error(f"Función '{func_name}' no definida", ctx)
            return None
        args = self.visit(ctx.argumentos()) if ctx.argumentos() else []
        expected = self.function_defs[func_name]['params']
        if len(args) != len(expected):
            self._add_error(f"Número incorrecto de argumentos para {func_name}", ctx)
            return None

        backup_vars = {p['name']: self.symbol_table[p['name']] for p in expected
                       if p['name'] in self.symbol_table}

        self.scope_stack.append(self.current_scope)
        self.current_scope = func_name

        for p, arg in zip(expected, args):
            vtype = p['type']
            val = arg
            if vtype == 'decimal' and isinstance(val, int):
                val = float(val)
            elif vtype == 'entero' and isinstance(val, float):
                self._add_warning(f"Conversión implícita de decimal a entero: {val}", ctx)
                val = int(val)
            self.symbol_table[p['name']] = {
                'type': vtype, 'value': val,
                'scope': self.current_scope, 'initialized': True
            }
            print(f"  [ASIGNACIÓN PARÁMETRO] {p['name']} = {val} ({vtype})")

        self.visit(self.function_defs[func_name]['body'])

        for p in expected:
            self.symbol_table.pop(p['name'], None)
        self.symbol_table.update(backup_vars)

        self.current_scope = self.scope_stack.pop()
        return None

    # ------------ Argumentos ------------
    def visitArgumentos(self, ctx: MiLenguajeParser.ArgumentosContext):
        return self.visit(ctx.lista_argumentos()) if ctx.lista_argumentos() else []

    def visitLista_argumentos(self, ctx: MiLenguajeParser.Lista_argumentosContext):
        args = [self.visit(ctx.expresion())]
        if ctx.lista_argumentos_prima():
            args += self.visit(ctx.lista_argumentos_prima())
        return args

    def visitLista_argumentos_prima(self, ctx: MiLenguajeParser.Lista_argumentos_primaContext):
        if ctx.getChildCount() == 0:
            return []
        return [self.visit(ctx.expresion())] + self.visit(ctx.lista_argumentos_prima())
