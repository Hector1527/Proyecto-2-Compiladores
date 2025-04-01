from antlr4 import *
from MiLenguajeLexer import MiLenguajeLexer
from MiLenguajeParser import MiLenguajeParser

def main():
    # Leer un archivo de entrada (ej. 'test.mileng')
    input_file = FileStream("test.mileng", encoding="utf-8")
    
    # Crear el lexer y parser
    lexer = MiLenguajeLexer(input_file)
    stream = CommonTokenStream(lexer)
    parser = MiLenguajeParser(stream)
    
    # Parsear desde la regla inicial 'programa'
    tree = parser.programa()
    
    # Imprimir el árbol en formato LISP
    print(tree.toStringTree(recog=parser))

if __name__ == "__main__":
    main()