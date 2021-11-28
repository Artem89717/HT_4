# 7. Написати функцію, яка приймає на вхід список і підраховує кількість однакових елементів у ньому.
input_str = input("Write your number using comma: ")
repeat_list = []
list_of_numbers = []
for i in input_str.split(","):
    list_of_numbers.append(int(i))

for i in list_of_numbers:
    if list_of_numbers.count(i) != 1 and i not in repeat_list:
        print(str(i) + " in list repeat " + str(list_of_numbers.count(i)) + " times")
        repeat_list.append(i)

