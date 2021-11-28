# 4. Написати функцію < prime_list >, яка прийматиме 2 аргументи - початок і кінець діапазона, і вертатиме список простих чисел всередині цього діапазона.

def prime_list(start, finish):
    res_list = []
    for i in range(start, finish + 1):
        check = True
        for b in range(2, i):
            if i % b == 0 and b != i:
                check = False
        if check:
            res_list.append(i)
    print(res_list)
            
prime_list(1, 100)