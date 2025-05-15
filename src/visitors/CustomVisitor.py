from MiLenguajeVisitor import MiLenguajeVisitor
from MiLenguajeParser import MiLenguajeParser

class CustomVisitor(MiLenguajeVisitor):
    def __init__(self):
        # Archivo de salida para transcripción a Python
        self.output_file = open('output.py', 'w', encoding='utf-8')
        # Encabezado del archivo Python
        self.output_file.write('# Transcripción generada por CustomVisitor\n')

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

    def _write(self, code_line: str):
        # Escribe línea en archivo con indentación
        self.output_file.write('    ' * self.indent_level + code_line + '\n')

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
        self._write("def main():")
        self.indent_level += 1
        self.visitChildren(ctx)
        self.indent_level -= 1
        self._write("if __name__ == '__main__': main()")
        self.output_file.close()
        return None

    def visitDeclaracion(self, ctx: MiLenguajeParser.DeclaracionContext):
        var_type = ctx.tipo().getText()
        var_name = ctx.ID().getText()
        
        # Valor por defecto según el tipo
        default_value = 0.0 if var_type == 'decimal' else 0
        
        var_info = {
            'type': var_type,
            'value': default_value,
            'scope': self.current_scope,
            'initialized': False
        }
        
        if ctx.expresion():
            value = self.visit(ctx.expresion())
            
            # Conversión explícita para decimales
            if var_type == 'decimal':
                if isinstance(value, int):
                    value = float(value)
                    print(f"[ASIGNACIÓN] {var_name} = {value:.1f}")  # Muestra el .0 para decimales
                elif not isinstance(value, float):
                    self._add_error(f"Tipo incorrecto para variable decimal '{var_name}'", ctx)
            elif var_type == 'entero' and not isinstance(value, int):
                self._add_error(f"Tipo incorrecto para variable entera '{var_name}'", ctx)
            
            var_info['value'] = value
            var_info['initialized'] = True

            # Escritura de declaración en Python
            py_val = repr(value)
            self._write(f"{var_name} = {py_val}")

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
        
        # Conversión explícita para decimales
        if var_info['type'] == 'decimal':
            if isinstance(value, int):
                value = float(value)
                print(f"[ASIGNACIÓN] {var_name} = {value:.1f}")  # Muestra el .0 para decimales
            elif not isinstance(value, float):
                self._add_error(f"Tipo incorrecto en asignación para '{var_name}'", ctx)
        elif var_info['type'] == 'entero' and not isinstance(value, int):
            self._add_error(f"Tipo incorrecto en asignación para '{var_name}'", ctx)
        else:
            var_info['value'] = value
            var_info['initialized'] = True

            # Escritura de asignación en Python
            py_val = repr(value)
            self._write(f"{var_name} = {py_val}")
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
            # Escritura en Python
            self._write(f"# Expresión suma: {left_value} + {delta}")
            self._write(f"result = {repr(left_value)} + {repr(delta)}")
            return result
        self._print_node_info("EXPRESION", f"Resultado: {left_value}")
        self._write(f"# Expresión simple: {left_value}")
        self._write(f"result = {repr(left_value)}")
        return left_value

    def visitExpresion_prima(self, ctx: MiLenguajeParser.Expresion_primaContext):
        if ctx.getChildCount() == 0:
            return 0
        op = ctx.getChild(0).getText()
        term_value = self.visit(ctx.termino())
        delta = self.visit(ctx.expresion_prima())
        if not isinstance(term_value, (int, float)) or not isinstance(delta, (int, float)):
            raise TypeError("Tipos incompatibles en + / -")
        # Escritura en Python de la operación prima
        self._write(f"# Operación prima: {term_value} {op} {delta}")
        self._write(f"{term_value} {op} {delta}")
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
            self._write(f"# Termino producto: {left_value} * {right_value}")
            self._write(f"result = {repr(left_value)} * {repr(right_value)}")
            return result
        self._print_node_info("TERMINO", f"Resultado: {left_value}")
        self._write(f"# Termino simple: {left_value}")
        self._write(f"result = {repr(left_value)}")
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
        self._write(f"# Operación termino prima: {factor_value} {op} {next_value}")
        self._write(f"{factor_value} {op} {next_value}")
        return 1

    def visitFactor(self, ctx: MiLenguajeParser.FactorContext):
        if ctx.NUMERO():
            num_str = ctx.NUMERO().getText()
            result = float(num_str) if '.' in num_str else int(num_str)
            content = f"Número: {num_str}"
            self._write(f"# Factor número: {num_str}")
            self._write(f"{num_str}")
        elif ctx.ID():
            var_name = ctx.ID().getText()
            for scope in [self.current_scope] + self.scope_stack:
                if var_name in self.symbol_table and self.symbol_table[var_name]['scope'] == scope:
                    self._write(f"# Factor variable: {var_name}")
                    self._write(var_name)
                    return self.symbol_table[var_name]['value']
            self._add_error(f"Variable '{var_name}' no declarada", ctx)
            return None
        elif ctx.CADENA_LITERAL():
            text_raw = ctx.CADENA_LITERAL().getText()
            result = text_raw.strip('"')
            self._write(f"# Factor cadena: {text_raw}")
            self._write(repr(result))
            content = f"Cadena: {text_raw}"
        elif ctx.BOOLEAN_LITERAL():
            bool_str = ctx.BOOLEAN_LITERAL().getText()
            result = bool_str == "verdadero"
            self._write(f"# Factor booleano: {bool_str}")
            self._write(str(result))
            content = f"Booleano: {bool_str}"
        elif ctx.expresion():
            content = "Expresión entre paréntesis"
            result = self.visit(ctx.expresion())
            self._write(f"# Factor paréntesis: ({ctx.expresion().getText()})")
            self._write(f"({ctx.expresion().getText()})")
        else:
            content = "Tipo desconocido"
            result = None
            self._write("# Factor tipo desconocido")
        self._print_node_info("FACTOR", content)
        return result

    # ------------- E/S -------------
    def visitEntrada_salida(self, ctx: MiLenguajeParser.Entrada_salidaContext):
        if ctx.LEER():
            var_name = ctx.ID().getText()
            self._print_node_info("LEER", f"Variable: {var_name}")
            self._write(f"# LEER variable {var_name}")
            self._write(f"input_value = input()  # LEER {var_name}")
            return None
        val = self.visit(ctx.expresion())
        self._print_node_info("ESCRIBIR", f"Valor: {val}")
        self._write(f"# ESCRIBIR valor {val}")
        self._write(f"print({repr(val)})")
        return val

    # ------------- IF / ELSE -------------
    def visitCondicional(self, ctx: MiLenguajeParser.CondicionalContext):
        cond_text = ctx.condicion().getText()
        self._print_node_info("CONDICIONAL", f"Evaluando condición: {cond_text}")
        self._write(f"if {cond_text}:")
        self.indent_level += 1
        if self._eval_condition(ctx.condicion()):
            self._print_node_info("CONDICIONAL", "Condición verdadera, ejecutando bloque if")
            self.visit(ctx.cuerpo())          
        elif ctx.sino():
            self.indent_level -= 1
            self._write("else:")
            self.indent_level += 1
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
        cond_text = ctx.condicion().getText()
        self._print_node_info("BUCLE", f"Evaluando condición del while: {cond_text}")
        self._write(f"while {cond_text}:")
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
        cond = {
            '==': left == right,
            '!=': left != right,
            '>':  left > right,
            '<':  left < right,
            '>=': left >= right,
            '<=': left <= right
        }.get(op, False)
        self._write(f"# Evaluar condición: {left} {op} {right}")
        self._write(f"{left} {op} {right}")
        return cond

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
        self._write(f"def {func_name}({', '.join(p['name'] for p in self.function_defs[func_name]['params'])}):")
        self.indent_level += 1
        # El cuerpo se transcribe al visitar el contexto
        self.visit(ctx.cuerpo())
        self.indent_level -= 1
        return None

    def visitParametros(self, ctx: MiLenguajeParser.ParametrosContext):
        self._write("# Inicio de parámetros")
        if ctx.lista_parametros():
            params = self.visit(ctx.lista_parametros())
        else:
            params = []
        self._write(f"# Parámetros obtenidos: {params}")
        return params

    def visitLista_parametros(self, ctx: MiLenguajeParser.Lista_parametrosContext):
        self._print_node_info("LISTA_PARAMETROS", "Procesando lista de parámetros")
        # Obtener el primer parámetro
        params = [{'type': ctx.tipo().getText(), 'name': ctx.ID().getText()}]
        # Transcribir parámetro a Python
        self._write(f"# Parametro: {params[0]}")
        if ctx.lista_parametros_prima():
            rest = self.visit(ctx.lista_parametros_prima())
            params += rest
            self._write(f"# Parámetros adicionales: {rest}")
        return params

    def visitLista_parametros_prima(self, ctx: MiLenguajeParser.Lista_parametros_primaContext):
        self._print_node_info("LISTA_PARAMETROS_PRIMA", "Procesando parámetros en cola")
        if ctx.getChildCount() == 0:
            self._write("# Sin más parámetros")
            return []
        current = {'type': ctx.tipo().getText(), 'name': ctx.ID().getText()}
        self._write(f"# Parametro en cola: {current}")
        rest = self.visit(ctx.lista_parametros_prima())
        return [current] + rest

    def visitLlamada_funcion(self, ctx: MiLenguajeParser.Llamada_funcionContext):
        func_name = ctx.ID().getText()
        self._print_node_info("LLAMADA_FUNCION", f"Llamando función: {func_name}")
        self._write(f"# Llamada a función: {func_name}")
        if func_name not in self.function_defs:
            self._add_error(f"Función '{func_name}' no definida", ctx)
            return None
        args = self.visit(ctx.argumentos()) if ctx.argumentos() else []
        self._write(f"# Argumentos para llamada: {args}")
        expected = self.function_defs[func_name]['params']
        if len(args) != len(expected):
            self._add_error(f"Número incorrecto de argumentos para {func_name}", ctx)
            return None

        backup_vars = {p['name']: self.symbol_table[p['name']] for p in expected
                       if p['name'] in self.symbol_table}
        self.scope_stack.append(self.current_scope)
        self.current_scope = func_name

        # Asignación de parámetros locales
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
            self._write(f"# Parámetro local {p['name']} = {val} ({vtype})")

        # Ejecutar cuerpo de la función
        self.visit(self.function_defs[func_name]['body'])

        # Restaurar estado
        for p in expected:
            self.symbol_table.pop(p['name'], None)
        self.symbol_table.update(backup_vars)
        self.current_scope = self.scope_stack.pop()
        return None

    # ------------ Argumentos ------------
    def visitArgumentos(self, ctx: MiLenguajeParser.ArgumentosContext):
        self._print_node_info("ARGUMENTOS", "Recolectando argumentos de llamada")
        self._write("# Inicio de argumentos")
        if ctx.lista_argumentos():
            args = self.visit(ctx.lista_argumentos())
        else:
            args = []
        self._write(f"# Argumentos obtenidos: {args}")
        return args

    def visitLista_argumentos(self, ctx: MiLenguajeParser.Lista_argumentosContext):
        self._print_node_info("LISTA_ARGUMENTOS", "Procesando lista de argumentos")
        first = self.visit(ctx.expresion())
        self._write(f"# Primer argumento: {first}")
        args = [first]
        if ctx.lista_argumentos_prima():
            rest = self.visit(ctx.lista_argumentos_prima())
            args += rest
            self._write(f"# Argumentos adicionales: {rest}")
        return args

    def visitLista_argumentos_prima(self, ctx: MiLenguajeParser.Lista_argumentos_primaContext):
        self._print_node_info("LISTA_ARGUMENTOS_PRIMA", "Procesando argumentos extras en cola")
        if ctx.getChildCount() == 0:
            self._write("# Sin más argumentos")
            return []
        arg = self.visit(ctx.expresion())
        self._write(f"# Argumento en cola: {arg}")
        rest = self.visit(ctx.lista_argumentos_prima())
        return [arg] + rest

    def generar_codigo_python(self, filename: str):
        """
        Finaliza el archivo de salida y renombra a `filename`.
        """
        try:
            # Cierra el archivo si sigue abierto
            if not self.output_file.closed:
                self.output_file.close()
            import os
            os.replace('output.py', filename)
            print(f"[CÓDIGO PYTHON] Archivo generado: {filename}")
        except Exception as e:
            print(f"Error al generar el archivo Python: {e}")
