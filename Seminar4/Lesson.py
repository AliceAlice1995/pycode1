# x: int = 3
# y: int = 5
# print(x + y)


# x: int = 10
# y: int = ' hello '
# print(x * y)


# Функции

def summa(spisok):
    s = 0
    for item in spisok:
        s += item
    print(s)

summa([5, 8, 13, 12])
    

def summa2(spisok):
    s = 0
    for item in spisok:
        s += item
    return s

summa([5, 8, 13, 12])
print(summa2([5, 8, 13, 12]))



def summa2(spisok: list) -> int:
    s: int =  0
    for item in spisok:
        s += item
    return s




summa([5, 8, 13, 12])
print(summa2([5, 8, 13, 12]))