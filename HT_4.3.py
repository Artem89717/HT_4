# 3. Написати функцию < is_prime >, яка прийматиме 1 аргумент - число від 0 до 1000, и яка вертатиме True, якщо це число просте, и False - якщо ні.

def prime(number):
    result = True
    for i in range(2, number):
        if number % i == 0 and i != number:
            result = False
    if number == 0 or number == 1:
        result = True
    print(result)

prime(23)