def main():
    x = 0
    y = 0
    print("Ingrese un número:")
    x = int(input())
    print("Ingrese otro número:")
    y = int(input())
    def suma(a, b):
        print("La suma es:")
        print(a + b)
    suma(x, y)

if __name__ == '__main__': main()