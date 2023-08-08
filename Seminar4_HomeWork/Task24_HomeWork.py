# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. 
# Она растёт на круглой грядке, причём кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. 
# Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора 
# на них выросло различное число ягод — на i-ом кусте выросло a[i] ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, 
# которое может собрать за один заход собирающий модуль, находясь 
# перед некоторым кустом заданной во входном списке урожайности грядки.

import random

bushes = int(input("Введите кол-во кустов "))
berries = []
result = []
sum = 0

for i in range(bushes):
    berries.append(random.randint(0, 10))

print(berries)

for i in range(bushes):
    if (i == bushes - 1):
        sum = berries[i - 1] + berries[i] + berries[0]
    else:
        sum = berries[i - 1] + berries[i] + berries[i + 1]
    result.append(sum)

for i in range(len(result)):
    for j in range(len(result) - 1):
        if result[j] > result[j+1]:
            result[j+1], result[j] = result[j], result[j+1]

print(f"Максимальное кол-во ягод: {result[-1]}")