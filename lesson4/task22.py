#Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
#Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
#Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. 
#Затем пользователь вводит сами элементы множеств.

n = int (input('Введите число n => '))
m = int (input('Введите число m => '))
list_n = []
list_m = []
for i in range(n):
    list_n.append(int (input ('Введите число множества n => ')))
for i in range(m):
    list_m.append(int (input ('Введите число множества m => ')))
print(list_n)
print(list_m)
set_n = set(list_n)
set_m = set (list_m)
u = set_n.union(set_m) 
u_list = list(u)
print(u)
print (u_list)
    
u_list.sorted()
print (u_list)
