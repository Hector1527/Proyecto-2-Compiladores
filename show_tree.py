from antlr4 import *
from generated.MiLenguajeLexer import MiLenguajeLexer
from generated.MiLenguajeParser import MiLenguajeParser

def main():
    input = FileStream("test1.mileng")
    lexer = MiLenguajeLexer(input)
    stream = CommonTokenStream(lexer)
    parser = MiLenguajeParser(stream)
    tree = parser.programa()  # Asegúrate que "programa" es tu regla inicial
    print(tree.toStringTree(recog=parser))

if __name__ == "__main__":
    main()