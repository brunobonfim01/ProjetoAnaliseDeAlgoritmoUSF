""" Algoritmo de Ordenação por Seleção
    É um algoritmo conhecido por sua simplicidade.
    O algoritmo divide a entrada em duas partes: a sublista de itens
    já classificado, que é construído da esquerda para a direita na frente (esquerda)
    da lista e a sublista de itens restantes a serem classificados que ocupam o
    resto da lista.
    O algoritmo prossegue encontrando o menor elemento na sublista não classificada,
    trocando-o com o elemento não classificado mais à esquerda."""

def sort(array):
    trocas = 0
    comparacoes = 0
    for index in range(0, len(array)):
        min_index = index
        for right in range(index + 1, len(array)):
            comparacoes += 1
        trocas += 1
        if array[right] < array[min_index]:           
                min_index = right
        array[index], array[min_index] = array[min_index], array[index]
        trocaecomp = "{} trocas foram feitas. {} comparações foram feitas.".format(trocas, comparacoes)
        print(trocaecomp)
