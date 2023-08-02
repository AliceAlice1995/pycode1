# Задача №3. Решение в группах
# В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть
# два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее
# число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32

# firstClass = int (input("Введите кол-во учеников 1 класса: "))
# secondClass = int (input("Введите кол-во учеников 2 класса: "))
# thirdClass = int (input("Введите кол-во учеников 3 класса: "))


# # print(f"Наименьшее количество парт: {round((firstClass + secondClass + thirdClass) / 2)}")
# print(f"Наименьшее количество парт: {(firstClass // 2 + firstClass % 2) + (secondClass // 2 + secondClass % 2) + (thirdClass // + thirdClass % 2)}")


for X in range(2):
    for Y in range(2):
        for Z in range(2):
            result = (not (X or Y or Z) == (not X and not Y and not Z))
            print(result)