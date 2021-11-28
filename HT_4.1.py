# 1. Написати функцію < square > , яка прийматиме один аргумент - сторону квадрата, і вертатиме 3 значення (кортеж): периметр квадрата,
# площа квадрата та його діагональ.

def square():
    side = int(input("Write side of square: "))
    perimeter = side * 4
    area = side ** 2
    diagonal =  1.4 * side
    result_tuple = (perimeter, area, diagonal)
    print (result_tuple)
    
square()