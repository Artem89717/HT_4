#5. Написати функцію < fibonacci >, яка приймає один аргумент і виводить всі числа Фібоначчі, що не перевищують його.

def fibonacci(max_number):
    fib_1 = 0
    fib_2 = 1
    fib_3 = 0
    res_list = [0 ,1]
    while fib_3 <= max_number:
        fib_3 = fib_1 + fib_2
        fib_1 = fib_2
        fib_2 = fib_3
        if fib_3 <= max_number:
            res_list.append(fib_3)
    if max_number == 0:
        res_list = [0]
    print(res_list)

fibonacci(200)