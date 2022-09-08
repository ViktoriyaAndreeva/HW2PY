#Задание 1 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#Пример:
#6782 -> 23
#0,56 -> 11

number = input('Введите число:\t')
summa = 0
for i in number:
    if '0' <= i <= '9':
        summa += int(i)
print(f'Сумма цифр числа равна:{summa}') 

# Второй вариант
exit()
number = float(input('Введите число:\t'))
spisok = str(number)
spisok1 = list(spisok)
summa = 0
for i in spisok1:
    if '0' <= i <= '9':
        summa += int(i)
print(f'Сумма цифр числа равна:{summa}')