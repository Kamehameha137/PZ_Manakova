# Вариант 30 Номер 2
# Дано целое число N (>0). С помощью операций деления нацело и взятия остатка от деления определить,
# имеется ли в записи числа N цифра «2». Если имеется, то вывести TRUE, если нет — вывести FALSE.

a = False

def findNum(num):
    while num>0:
        if num % 10 == 2:
            a = True
            break
        else:
            a = False
        num //= 10
        #print(num) # для проверки
    if(a == True):
        print("В числе есть цифра 2")
    else:
        print("В числе нет цифры 2")


while True:
    N = int(input("Введите значение N > 0: "))
    if N > 0:
        findNum(N)
        break
    else:
        print("Пожалуйста, введите число больше 0.")
        continue