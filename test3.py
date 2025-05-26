def main():
    i = int(0)
    def cuadrado(n):
        print(n * n)
    while i < 5:
        cuadrado(i)
        i = i + 1

if __name__ == '__main__': main()