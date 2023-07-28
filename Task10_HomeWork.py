# Задача 10: На столе лежат n монеток. 
# Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальноe количество монет, которые нужно перевернуть
#  0 1 0 1 0 0

import random 

n = int(input("Введите кол-во монеток: "))
resh_or_gerb = []

for i in range(n):
    resh_or_gerb.append(random.randint(0, 1))

print(resh_or_gerb)        

count_min = 0
count = 0

for i in resh_or_gerb:  
    if i > 0:
        count += 1
    else:
        if count_min <= count:
            count_min = count

print(count)

