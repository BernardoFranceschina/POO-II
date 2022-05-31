def main():
    n1 = int(input('informe o numero inicial'))
    n2 = int(input('informe o numero final'))

    soma = 0
    for i in range(n1, n2+1):
        soma += i
        print(i)

    print('soma', soma)


if __name__ == '__main__':
    main()