# Заданные входные данные
var1 = '5 4'
var2 = '1 3 5 7 9'
var3 = '2 3 4 5'
# Разбиваем входные данные на списки
n, m = map(int, var1.split())
set1 = set(map(int, var2.split()))
set2 = set(map(int, var3.split()))
# Находим пересечение множеств и сортируем его элементы
intersection = sorted(set1.intersection(set2))
# Выводим результат
result = ' '.join(map(str, intersection))
print(result)