def main():
    impar = 0
    par = 0
    for i in range(10):
        numero = int(input('Informe um numero'))
        if numero % 2 == 0:
            par += 1
        else:
            impar += 1

    print('Par', par, 'impar', impar)

if __name__ == '__main__':
    main()