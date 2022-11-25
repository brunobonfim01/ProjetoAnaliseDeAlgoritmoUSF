import contextlib
import random
import time

from sorting import (
    selection_sort,
)

@contextlib.contextmanager
def timeit(name):
    start = time.time()
    yield
    end = time.time()
    took = end - start
    print(f"O {name} levou {took:.4f}s")


def nearly_sorted_array(tamanho):
    array = [i for i in range(0, tamanho + 1)]

    for i in range(10, tamanho, 10):
        array[i], array[i - 1] = array[i - 1], array[i]

    return array


if __name__ == '__main__':
    tamanho = 100000

    normal_array = [random.randint(0, tamanho)
                    for i in range(tamanho)]
    random.shuffle(normal_array)

    nearly_sorted = nearly_sorted_array(tamanho)
    reversed_array = sorted(normal_array, reverse=True)
    sorted_array = sorted(normal_array)

    algorithms = {
        "selection_sort": selection_sort.sort,
    }


    print("\n\nMelhor Caso")
    print("-" * 50)
    for name, sort in algorithms.items():
        copy_array = list(nearly_sorted)
        
        with timeit(name):
            sort(copy_array)
        


    '''print("\n\nCaso Médio")
    print("-" * 50)
    for name, sort in algorithms.items():
        copy_array = list(normal_array)

        with timeit(name):
            sort(copy_array)'''


    '''print("\n\nPior Caso")
    print("-" * 50)
    for name, sort in algorithms.items():
        copy_array = list(reversed_array)

        with timeit(name):
            sort(copy_array)'''