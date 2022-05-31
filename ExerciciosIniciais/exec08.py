def main():
    soma = 0
    for i in range(5):
        numero = int(input('Informe um numero'))
        soma += numero

    print('soma', soma, 'media', soma/5)

if __name__ == '__main__':
    main()