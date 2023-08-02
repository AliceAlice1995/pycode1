# ; Задача №17. Решение в группах
# ; Дан список чисел. Определите, сколько в нем
# ; встречается различных чисел.
# ; Input: [1, 1, 2, 0, -1, 3, 4, 4]
# ; Output: 6


# sp = [1, 1, 2, 0, -1, 3, 4, 4]
# print(len.sp)

import random

first_list = []

for _ in range(10):
    first_list.append(random.randint(0, 5))

second_list = []

for i in first_list:
    if not (i in second_list):
        second_list.append(i)


print(first_list)
print(len(second_list))

print(len(first_list))