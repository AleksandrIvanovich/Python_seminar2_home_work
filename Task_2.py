# Напишите программу, которая принимает на вход число N 
# и выдает набор произведений (набор - это список) чисел от 1 до N.
def give_int(input_string):
    while True:
        try:
            num = int(input(input_string))
            return num
        except:
            print('Попробуйте еще раз. Вы ввели не число')

n = give_int("Введите число N: ")
numbers = []
for i in range(1, n+1):
    if i == 1:
        numbers.append(i)
    else:
        new_element = numbers[i-2]*i
        numbers.append(new_element)
print (numbers)