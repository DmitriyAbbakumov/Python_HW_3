# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai . Последняя строка содержит число X
# 5 
# 1 2 3 4 5 
# 6
# -> 5

N = int(input("Введите кол-во элементов списка: "))
lst = [i for i in range(1, N + 1)]
print(lst)
X = int(input("Введите искомое число: "))

A_max = lst[0]
for i in range(1, len(lst)):
    if abs(X - lst [i]) < abs(X - A_max):
        A_max = lst[i]
print(A_max)