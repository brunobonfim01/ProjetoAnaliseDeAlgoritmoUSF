""" Algoritmo de Ordenação por Inserção
    É um algoritmo baseado em comparação no local.
    Para cada posição, troque o elemento atual à sua esquerda
    enquanto o elemento esquerdo é maior que o elemento atual."""

def sort(array):
    trocas = 0
    comparacoes = 0
    for i in range(0, len(array)):
        current_element = array[i]
        comparacoes += 1
        while i > 0 and array[i - 1] > current_element:
            array[i] = array[i - 1]
            i -= 1
            comparacoes += 1
            trocas += 1

        array[i] = current_element
        trocaecomp = "{} trocas foram feitas. {} comparações foram feitas.".format(trocas, comparacoes)
        print(trocaecomp)