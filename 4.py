# Задача HARD необязательная Имеется список чисел. Создайте список,в который попадают числа, описывающие максимальную 
# возрастающую последовательность. Порядок элементов менять нельзя. Одно число - это не последовательность.
# Пример:
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 7]
# [1, 5, 2, 3, 4, 1, 7, 8 , 15 , 1 ] => [1, 5]
# [1, 5, 3, 4, 1, 7, 8 , 15 , 1 ] => [3, 5]
from random import randint
lst = [randint(1, 20) for i in range(randint(2, 30))]
temp_lst = []
for i in range(len(lst)):
    temp1_lst=[]
    b = lst[i]
    temp1_lst.append(b)
    count = 1
    for i in range(len(lst)):
        if b + 1 in lst:
            count = count + 1
            b = b + 1
    temp1_lst.append(b)
    temp_lst.append(temp1_lst)

a_max=temp_lst[0][1]-temp_lst[0][0]
k = 0
for i in range(1, len(temp_lst)):
    if temp_lst[i][1]-temp_lst[i][0] > a_max:
        a_max = temp_lst[i][1]-temp_lst[i][0]
        k = i
print(f'Исходный список: {lst}')
if a_max == 0:
    print('Нет возрастающей последовательности')
else:
    print(f'Максимальная возрастающая последовательность: {temp_lst[k]}')
        
    


        
    


