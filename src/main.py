import sys
import os
from antlr4 import *
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
sys.path.insert(0, str(BASE_DIR))
sys.path.insert(1, str(BASE_DIR / "generated"))

from MiLenguajeLexer import MiLenguajeLexer
from MiLenguajeParser import MiLenguajeParser
from visitors.CustomVisitor import CustomVisitor

def seleccionar_prueba():
    print("\nPruebas disponibles:")
    print("1. Hola Mundo")
    print("2. Operación aritmética")
    print("3. Condicional con input")
    print("4. Función con parámetros")
    print("5. Bucle while")
    print("6. Error léxico")
    print("7. Error sintáctico")
    print("8. Error semántico")
    print("0. Salir")
    
    while True:
        try:
            opcion = int(input("\nSeleccione el número de prueba (1-8): "))
            if 0 <= opcion <= 8:
                return opcion
            print("Por favor ingrese un número entre 1 y 8 (0 para salir)")
        except ValueError:
            print("Entrada inválida. Ingrese un número.")

def main():
    base_dir = Path(__file__).parent.parent
    
    while True:
        opcion = seleccionar_prueba()
        if opcion == 0:
            break
        
        test_file = base_dir / f"test{opcion}.mileng"
        if not test_file.exists():
            test_file = base_dir / f"test{opcion}_error_lexico.mileng"
        
        try:
            print(f"\n=== Ejecutando prueba {opcion} ===")
            input_stream = FileStream(str(test_file), encoding='utf-8')
            
            lexer = MiLenguajeLexer(input_stream)
            stream = CommonTokenStream(lexer)
            parser = MiLenguajeParser(stream)
            
            tree = parser.programa()
            visitor = CustomVisitor()
            visitor.visit(tree)
            
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo {test_file.name}")
        except Exception as e:
            print(f"Error durante la ejecución: {str(e)}")
        
        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    main()
