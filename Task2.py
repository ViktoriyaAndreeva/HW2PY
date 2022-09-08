#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#Пример:
#пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

from math import factorial


number = int(input('Введите число N:\t'))
faktorial = 1
if number == 1 or number == 0:
    print(f'Факториал числа {number} равен: 1')
else: 
    for i in range(2, number+1):
        faktorial*=i
    print(f'Факториал числа {number} равен: {faktorial}')

# через рекурсию

exit()
n = int(input('Введите число N:\t'))
def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n-1)
print(faktorial(n))        

