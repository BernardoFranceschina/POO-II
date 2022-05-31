def main():
    nota = -1
    while nota < 0 or nota > 10:
        nota = int(input("Informe a nota do usuário"))
        if nota < 0 or nota > 10:
            print('Nota inválida')
        else:
            print('Nota válida')

if __name__ == '__main__':
    main()