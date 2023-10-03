def max_berry_harvest(arr):
    n = len(arr)
    max_harvest = 0

    for i in range(n):
        # Начинаем сбор с левого куста (i-1) и двух соседних кустов (i-2 и i)
        left_harvest = arr[i]
        if i > 0:
            left_harvest += max(0, arr[i - 1])
        if i > 1:
            left_harvest += max(0, arr[i - 2])

        # Начинаем сбор с правого куста (i+1) и двух соседних кустов (i+2 и i)
        right_harvest = arr[i]
        if i < n - 1:
            right_harvest += max(0, arr[i + 1])
        if i < n - 2:
            right_harvest += max(0, arr[i + 2])

        # Выбираем максимальное количество ягод из двух случаев
        max_harvest = max(max_harvest, max(left_harvest, right_harvest))

    return max_harvest

arr = [5, 8, 6, 4, 9, 2, 7, 3]
result = max_berry_harvest(arr)
print(result)  