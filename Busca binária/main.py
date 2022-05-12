def buscaBinaria(palheiro, agulha):
    inicio = 0
    fim = len(palheiro) - 1

    while inicio <= fim:
        meio = int((inicio + fim) / 2)

        if palheiro[meio] == agulha:
            return meio

        if palheiro[meio] < agulha:
            inicio = meio + 1

        if palheiro[meio] > agulha:
            fim = meio - 1

    else:
        return -1


listaOrdenada = [0, 10, 20, 30, 50, 80]

print(buscaBinaria(listaOrdenada, 10))
print(buscaBinaria(listaOrdenada, 30))
print(buscaBinaria(listaOrdenada, 50))
print(buscaBinaria(listaOrdenada, 80))
print(buscaBinaria(listaOrdenada, 90))

