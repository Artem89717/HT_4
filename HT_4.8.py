# 8. Написати функцію, яка буде реалізувати логіку циклічного зсуву елементів в списку. Тобто, функція приймає два аргументи: список і величину зсуву 
# (якщо ця величина додатня - пересуваємо з кінця на початок, якщо від'ємна - навпаки - пересуваємо елементи з початку списку в його кінець).
#   Наприклад:
#       fnc([1, 2, 3, 4, 5], shift=1) --> [5, 1, 2, 3, 4]
#       fnc([1, 2, 3, 4, 5], shift=-2) --> [3, 4, 5, 1, 2]

def sort_func(example_list, step):
    if step > 0:
        result_list = example_list[-step:]
        result_list = result_list[::-1]
        result_list += example_list[:(len(example_list)-step)]
    
    if step < 0:
        step *= (-1)
        result_list = example_list[step:] + example_list[:step]

    print(result_list)

        
sort_func([1, 2, 3, 4, 5], 1)