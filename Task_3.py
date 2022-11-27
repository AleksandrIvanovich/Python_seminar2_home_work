#3. Дан массив размера N. После каждого отрицательного элемента массива 
# вставьте элемент с нулевым значением.

#Пример:
#- пусть N = 4, тогда [28, -46, 14, -14] => [28, -46, 0, 14, -14, 0]
import random

def give_int(input_string):
    while True:
        try:
            num = int(input(input_string))
            return num
        except:
            print('Попробуйте еще раз. Вы ввели не число')
            
n = give_int("Введите число: \n") 
rand_list = []
new_list = []
for i in range(n):
    rand_list.append(random.randint(-100,100))
    if rand_list[i] >= 0:
       new_list.append(rand_list[i]) 
    else:
        new_list.append(rand_list[i])
        new_list.append(0)   
print(f'Сгенерированный массив:{rand_list}')      
print(f'Новый массив: {new_list}')
