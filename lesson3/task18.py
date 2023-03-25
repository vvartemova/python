#Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
#Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

n = int (input('Введите число n => '))
a = []
for i in range (n):
    a.append(int (input (f'Введите a[{i}] => ')))
x = int (input('Введите число x => '))

for i in range (len(a)-1):
        if abs(a[i] - x) <= abs(a[i+1] - x):
           closest_number = a[i]
        else:
           closest_number = a[i+1]
print (closest_number)