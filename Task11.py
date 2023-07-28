# Задача №11. Решение в группах
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6
# 0 1 1 2 3 5 8 13 21

A = int(input("Введите число: "))

f_elem, s_elem, current = 0, 1, 1
count = 2

while current < A:
    current = f_elem + s_elem  
    f_elem = s_elem 
    s_elem = current 
    count += 1

if current == A:
    print(count)
else:
    print(-1)




# if num == 0:
#     print(1)
# else:
#     prev, next = 0, 1
#     n = 2
#     while next <= num:
#         if next == num:
#             print(n)
#             break
#         prev, next = next, prev + next
#         n += 1
#     else:
#         print(-1)
        

    