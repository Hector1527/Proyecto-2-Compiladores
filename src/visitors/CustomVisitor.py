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
        self.function_defs = {}
        self.scope_stack = []
        self.indent_level = 0

    def _print_node_info(self, node_name, content=""):
        indent = "  " * self.indent_level
        print(f"{indent}[VISITANDO {node_name}] {content}")

    def _add_error(self, message, ctx=None):
        self.errors.append(message)
        self._print_node_info("ERROR", message)

    def visitPrograma(self, ctx: MiLenguajeParser.ProgramaContext):
        self._print_node_info("PROGRAMA")
        self.indent_level += 1
        self.visitChildren(ctx)
        self.indent_level -= 1
        return None

    def visitDeclaracion(self, ctx: MiLenguajeParser.DeclaracionContext):
        var_type = ctx.tipo().getText()
        var_name = ctx.ID().getText()
        
        # Inicializar con valor por defecto
        default_value = 0.0 if var_type == 'decimal' else 0
        var_info = {
            'type': var_type,
            'value': default_value,
            'scope': self.current_scope,
            'initialized': False
        }
        
        if ctx.expresion():
            value = self.visit(ctx.expresion())
            # Verificar tipo
            if (var_type == 'entero' and not isinstance(value, int)) or \
               (var_type == 'decimal' and not isinstance(value, (int, float))):
                self._add_error(f"Tipo incorrecto para variable '{var_name}'", ctx)
            else:
                var_info['value'] = value
                var_info['initialized'] = True
        
        self.symbol_table[var_name] = var_info
        return None

    def visitTipo(self, ctx: MiLenguajeParser.TipoContext):
        tipo = ctx.getText()
        self._print_node_info("TIPO", tipo)
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
            # Buscar en ámbitos activos
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

    def visitDefinicion_funcion(self, ctx: MiLenguajeParser.Definicion_funcionContext):
        func_name = ctx.ID().getText()
        
        # Registrar la función en la tabla de símbolos
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
        params = []
        # Procesar primer parámetro
        param_type = ctx.tipo().getText()
        param_name = ctx.ID().getText()
        params.append({'type': param_type, 'name': param_name})
        
        # Procesar parámetros adicionales
        if ctx.lista_parametros_prima():
            params += self.visit(ctx.lista_parametros_prima())
        return params

    def visitLista_parametros_prima(self, ctx: MiLenguajeParser.Lista_parametros_primaContext):
        if ctx.getChildCount() == 0:
            return []
        # Procesar siguiente parámetro
        param_type = ctx.tipo().getText()
        param_name = ctx.ID().getText()
        return [{'type': param_type, 'name': param_name}] + self.visit(ctx.lista_parametros_prima())

    def visitLlamada_funcion(self, ctx: MiLenguajeParser.Llamada_funcionContext):
        func_name = ctx.ID().getText()
        
        # 1. Verificar que la función existe
        if func_name not in self.function_defs:
            self._add_error(f"Función '{func_name}' no definida", ctx)
            return None
            
        # 2. Obtener y validar argumentos
        args = self.visit(ctx.argumentos()) if ctx.argumentos() else []
        expected_params = self.function_defs[func_name]['params']
        
        if len(args) != len(expected_params):
            self._add_error(f"Número incorrecto de argumentos para {func_name}", ctx)
            return None
            
        # 3. Crear nuevo ámbito
        self.scope_stack.append(self.current_scope)
        self.current_scope = func_name
        
        # 4. Registrar parámetros con valores reales
        for param, arg_value in zip(expected_params, args):
            var_name = param['name']
            self.symbol_table[var_name] = {
                'type': param['type'],
                'value': arg_value,
                'scope': self.current_scope,
                'initialized': True
            }
            print(f"  [ASIGNACIÓN PARÁMETRO] {var_name} = {arg_value}")
        
        # 5. Ejecutar cuerpo de la función
        try:
            self.visit(self.function_defs[func_name]['body'])
        except TypeError as e:
            self._add_error(str(e), ctx)
        
        # 6. Restaurar ámbito y limpiar
        self.current_scope = self.scope_stack.pop()
        for param in expected_params:
            del self.symbol_table[param['name']]
        
        return None

    def visitArgumentos(self, ctx: MiLenguajeParser.ArgumentosContext):
        if ctx.lista_argumentos():
            return self.visit(ctx.lista_argumentos())
        return []

    def visitLista_argumentos(self, ctx: MiLenguajeParser.Lista_argumentosContext):
        args = [self.visit(ctx.expresion())]
        if ctx.lista_argumentos_prima():
            args += self.visit(ctx.lista_argumentos_prima())
        return args

    def visitLista_argumentos_prima(self, ctx: MiLenguajeParser.Lista_argumentos_primaContext):
        if ctx.getChildCount() == 0:
            return []
        return [self.visit(ctx.expresion())] + self.visit(ctx.lista_argumentos_prima())

    def visitArgumentos(self, ctx: MiLenguajeParser.ArgumentosContext):
        if ctx.lista_argumentos():
            return self.visit(ctx.lista_argumentos())
        return []

    def visitLista_argumentos(self, ctx: MiLenguajeParser.Lista_argumentosContext):
        args = [self.visit(ctx.expresion())]
        if ctx.lista_argumentos_prima():
            args += self.visit(ctx.lista_argumentos_prima())
        return args

    def visitLista_argumentos_prima(self, ctx: MiLenguajeParser.Lista_argumentos_primaContext):
        if ctx.getChildCount() == 0:
            return []
        return [self.visit(ctx.expresion())] + self.visit(ctx.lista_argumentos_prima())
