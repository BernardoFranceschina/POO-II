def main():
    tabuada = -1
    while tabuada < 1 or tabuada > 10:
        tabuada = int(input('Informe o numero da tabua que deseja ver (1 - 10)'))

    for i in range(1, 11):
        print(tabuada, "X", i, '=', tabuada*i)

if __name__ == '__main__':
    main()