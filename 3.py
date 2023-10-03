def power_recursive(a, b):
    # Базовый случай: если степень b равна 0, то результат всегда 1.
    if b == 0:
        return 1
    # Рекурсивный случай: вычисляем a в степени (b-1) и умножаем на a.
    else:
        return a * power_recursive(a, b - 1)

# Примеры использования:
result1 = power_recursive(3, 5)  # Результат: 243
result2 = power_recursive(2, 3)  # Результат: 8

print(result1)
print(result2)