#6. Вводиться число. Якщо це число додатне, знайти його квадрат, якщо від'ємне, збільшити його на 100, якщо дорівнює 0, не змінювати.
number =  int(input("Please, write your number:"))
if number > 0:
    number = number ** 2
    print(number)
if number < 0:
    number += 100
    print(number)
if number == 0:
    print(number)