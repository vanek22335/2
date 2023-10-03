def sum(a, b):
    # Базовый случай: если одно из чисел равно 0, возвращаем другое число.
    if a == 0:
        return b
    elif b == 0:
        return a
    # Рекурсивный случай: уменьшаем одно из чисел на 1 и вызываем функцию снова.
    else:
        return sum(a - 1, b + 1)

# Пример использования:
result = sum(2, 2)
print(result)  # Результат: 4