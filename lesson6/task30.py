#Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно 
#ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
#Каждое число вводится с новой строки.

def arithmetic_progression (first_num, step, count):
    list1 =[first_num]
    for i in range (2,count+1):
       num = first_num+(i-1)*step
       list1.append(num)
    return list1


first_num = int (input('Введите первый элемент прогрессии => '))
step = int (input('Введите разность => '))
count = int (input('Введите количество элементов => '))
print (arithmetic_progression(first_num, step, count))
