from random import randint




sp = [5, 8, 1, 3, 10, 0]
# s2 = sp[::]
# print(s2)
# sp.append(888)
# print(s2)

# найти все элементы больше 4, далее получить 
# новый список с квадратами таких элементов

def find_and_square(spisok):
    result = []
    for item in sp:
        if item > 4:
            result.append(item**2)
        return result

sp = [5, 8, 1, 3, 10, 0]
print(find_and_square(sp))
print([x**2 for x in sp if x > 4])
rsp = [randint(0, 11) for _ in range(10)]
print(rsp)
