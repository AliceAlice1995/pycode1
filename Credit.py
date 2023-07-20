# age = 48
# salary = 50000
# service = 18.5

# age = int(input("Введите возраст: "))
# salary = float(input("Введите зарплату: "))
# service = float(input("Введите сумму ежемесячных трат: "))
# loan_term = int(input("Срок нового кредита: "))
# sum_of_credit = float(input("Сумма ежемесячных трат по новому кредиту: "))
# age_verification = age + loan_term >= 50
# sum_verification = (salary - service) >= (salary / 2)

# # if (age + loan_term >= 50) and ((salary - service) >= (salary / 2)):
# if (age_verification) and ((salary - service) >= (salary / 2)):
#     print("Кредит одобрен")
# else:
#     print("Кредит не одобрен")


age = int(input("Введите ваш возраст: "))
salary = int(input("Введите ваш доход: "))
credits = int(input("Введите трату на обслуживание кредитов: "))
months = int(input("Введите предпочитаемый срок кредита: "))
creditSum = int(input("Введите желаемую сумму кредита: "))

ageMonths = age * 12
treshold = 50 * 12
duration = ageMonths + months > treshold
creditExpenses = credits + creditSum/months > salary / 2

if duration or creditExpenses:
    print("Отказ")
# elif  not duration and not creditExpenses:
else:
     print("Одобрено")