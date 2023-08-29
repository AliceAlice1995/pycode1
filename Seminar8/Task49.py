# Задача №49. Решение в группах
# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной


# def new_contact (list_names, list_phone_numbers):
#     new_info_name = input('Введите ФИО: ')
#     new_info_phone = int(input('Введите номер телефона: '))
#     print('Контакт успешно добавлен')
#     list_names.append(new_info_name)
#     list_phone_numbers.append(new_info_phone)
#     with open('phone_book.txt', 'a', encoding = "utf-8") as phonebook:
#         phonebook.write(f'{new_info_name}, ')
#         phonebook.write(f'{new_info_phone}\n')


# def find_contact():
#     contact_to_find = input('Введите имя, фамилию или телефонный номер для поиска: ')
#     phonebook = open('phone_book.txt', encoding = 'utf-8').readlines()
#     contact_found = False
#     for i in iter(phonebook):
#         if contact_to_find in i:
#             contact_found = True
#             print(f'Найден абонент {i}')
#         if contact_found == False:
#             print('Абонент не найден')

import json

phonebook = {"Дядя Петя": {"phone_numbers": ["12345", '23445'], "birthday": "01.05.1995", "e-mail": "petya@gmail.com"} }

with open("phonebook.json", "w", encoding = "utf-8") as phonebookjson:
    phonebookjson.write(json.dumps(phonebook, ensure_ascii = False))

def add_phone_nimber(file_name):
    info = ' '.join(get_new_nimber())
    with open(file_name, 'a', encoding = 'utf-8') as file:
        file.write(f'{info}\n')

def get_new_number():
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    patronimic = input("Введите отчество: ")
    phone_number = input("Введите номер телефона: ")
    return last_name, first_name, patronimic, phone_number



if __name__ == '__main__':
    file = 'phonebook.json'
    phonebook(file)


# phone_book_names = ['Иванов Иван Иванович', 'Петров Пётр Петрович', 'Сергеев Сергей Сергеевич']
# phone_book_numbers = [88005553535, 89999999, 89220010103]
# print('1 - Добавить контакт, 2 - найти контакт')
# choice = int(input('Введите номер своего выбора: '))
# if choice == 1:
#     new_contact(phone_book_names, phone_book_numbers)
# elif choice == 2:
#     find_contact()
# else:
#     print('Ошибка ввода')