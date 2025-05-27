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
from visitors.CustomVisitor import CustomVisitor2

def seleccionar_prueba():
    print("\nPruebas disponibles:")
    print("1. Operaciones aritméticas")
    print("2. Llamada a funciones y variables")
    print("3. Llamada a funciones, ciclos y operaciones ariméticas")
    print("4. Error semántico")
    print("0. Salir")
    
    while True:
        try:
            opcion = int(input("\nSeleccione el número de prueba (1-4): "))
            if 0 <= opcion <= 4:
                return opcion
            print("Por favor ingrese un número entre 1 y 4 (0 para salir)")
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
            #visitor = CustomVisitor()
            #visitor.visit(tree)


            visitor2 = CustomVisitor2()
            visitor2.visit(tree)
            visitor2.generar_codigo_python(f"test{opcion}.py")

            


        except FileNotFoundError:
            print(f"Error: No se encontró el archivo {test_file.name}")
        except Exception as e:
            print(f"Error durante la ejecución: {str(e)}")
        
        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    main()
