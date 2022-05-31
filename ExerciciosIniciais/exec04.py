def main():
    populacaoA = int(input('Informe os habitantes da população A'))
    taxaA = float(input('Informe a taxa de crescimento da população A'))
    populacaoB = int(input('Informe os habitantes da população B'))
    taxaB = float(input('Informe a taxa de crescimento da população B'))

    while populacaoA >= populacaoB:
        print('População A deve ser menor que população B')
        populacaoA = input('Informe os habitantes da população A')
        populacaoB = input('Informe os habitantes da população B')

    while taxaB >= taxaA:
        print('Taxa de crescmento da população B deve ser menor que população A')
        taxaA = input('Informe a taxa de crescimento da população A')
        taxaB = input('Informe a taxa de crescimento da população B')

    anos = 0
    while populacaoA < populacaoB:
        populacaoA = populacaoA + (populacaoA * (taxaA / 100))
        populacaoB = populacaoB + (populacaoB * (taxaB / 100))
        anos += 1

    print('Anos:', anos)
    continuar = input('Deseja calcular novamente? (s/n)')

    if continuar.upper() == 'S':
        main()

if __name__ == '__main__':
    main()