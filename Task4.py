#Задание 4 Задайте список из N элементов, заполненных числами из промежутка [-N, N].
#Найдите произведение элементов на позициях a и b.
#Значения N, a и b вводит пользователь с клавиатуры.

number = int(input('Введите положительое число N:\t'))
new_number = list(range(-number, number+1))
print(new_number)
a = int(input('Введите позицию а:\t'))
b = int(input('Введите позицию b:\t'))
if a >= len(new_number) or b >= len(new_number):
    print(f'Данные позиции отсутствуют в списке')
else:
    print(f'Произведение элементов на позиции {a} и {b} равно: {new_number[a-1]*new_number[b-1]}')
