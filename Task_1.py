#1. Напишите программу, которая принимает на вход вещественное 
#число и показывает сумму его цифр. Учтите, что числа могут быть отрицательными.
#Пример:
# 67.82 -> 23
# (-0.56) -> 11

def give_int(input_string):
    while True:
        try:
            num = float(input(input_string))
            return num
        except:
            print('Попробуйте еще раз. Вы ввели число некорректно!')

num = give_int('Введите десятичное число (через точку):\n')
numbers_string = str(num)
minus_index = numbers_string.find("-")
point_index = numbers_string.find(".")
numbers_list = list(numbers_string)

if minus_index == -1:
    numbers_list.pop(point_index)
else:
    numbers_list.pop(minus_index)  
    numbers_list.pop(point_index-1)
    
"".join(numbers_list)
numbers_int = list(map(int, numbers_list))

summ_numbers = 0
for i in numbers_int:
    summ_numbers = summ_numbers + i   
print(f'Сумма цифр введенного числа равна {summ_numbers}.')