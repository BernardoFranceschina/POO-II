def main():
    base = int(input('Informe a base'))
    expoente = int(input('Informe a expoente'))

    resultado = 1
    for i in range(expoente):
        resultado *= base

    print(resultado)

if __name__ == '__main__':
    main()