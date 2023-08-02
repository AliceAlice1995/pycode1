# Задача №19. Решение в группах
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

current_list = []

for i in range(10):
    current_list.append(i)

k = int(input("Enter K:"))
print(current_list)      

# current_list = current_list[k:] + current_list[:k]
# ИЛИ
for _ in range(k):
    current_list.insert(0, current_list.pop())
                                               
print(current_list)                         
