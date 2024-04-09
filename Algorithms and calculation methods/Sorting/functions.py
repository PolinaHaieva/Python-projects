from time import time
from random import randint


def selection_sort(arr: list) -> list:
    begin = time()
    for i in range(len(arr) - 1):
        least = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[least]:
                least = j
        arr[i], arr[least] = arr[least], arr[i]
    sort_time = time() - begin
    return arr, sort_time*(10**3)


def random_arr(n: int) -> list:
    rand_arr = []
    for i in range(n+1):
        rand_arr.append(randint(-1234, 5678))
    return rand_arr


print(type(selection_sort(random_arr(782))[1]))
