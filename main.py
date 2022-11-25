import numpy as np
import sys
import time

start = time.time()
sys.setrecursionlimit(1000001)

def bubblesort(A):
    l = lambda x, y, random: [x, y, random] if x < y else [y, x, False]
    comp = 0
    trocas = 0
    for i in range(len(A) - 1):
        comp += 1
        random = True
        for j in range(len(A) - i - 1):
            trocas +=1
            A[j], A[j + 1], random = l(A[j], A[j + 1], random)
        if random:
            break
    print(A)
    print("Foram realizadas {} trocas e {} comparações".format(comp,trocas))
    return A


A = np.array([x for x in range(0,100000,1)])
lista_inversa = A[::-1]
#np.random.shuffle(A)
bubblesort(lista_inversa)
end = time.time()
print("Tempo de execução! ", end-start)