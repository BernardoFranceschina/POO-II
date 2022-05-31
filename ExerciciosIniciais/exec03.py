def main():
    nome = ''
    idade = -1
    salario = -1
    sexo = ''
    estadoCivil = ''

    while len(nome) < 3:
        nome = input('Informe seu nome (minimo 3 caracteres)')

    while idade < 0 | idade > 150:
        idade = int(input('Informe sua idade (0 - 150)'))

    while salario < 0:
        salario = int(input('Informe seu salário (> 0)'))

    while sexo not in ['f', 'm']:
        sexo = input('Informe seu sexo (f ou m)')

    while estadoCivil not in ['s', 'c', 'v', 'd']:
        estadoCivil = input('Informe seu estado civil (s, c, v, d)')

if __name__ == '__main__':
    main()