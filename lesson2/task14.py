#Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = int (input('Введите число n => '))
k = 0
number = 2
numbers = []

while number < n:
      number = 2**k
      if number < n:
         numbers.append(number)
      k = k+1
print (numbers)

