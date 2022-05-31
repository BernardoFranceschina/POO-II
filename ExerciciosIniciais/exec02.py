def main():
    nome = input('Informe seu nome')
    senha = input('Informe sua senha')
    while senha == nome:
        senha = input('Informe uma senha válida')

if __name__ == '__main__':
    main()