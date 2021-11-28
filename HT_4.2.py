# 2. Написати функцію < bank > , яка працює за наступною логікою: користувач робить вклад у розмірі < a > одиниць строком на < years > років під < percents > 
# відсотків (кожен рік сума вкладу збільшується на цей відсоток, ці гроші додаються до суми вкладу і в наступному році на них також нараховуються відсотки). 
# Параметр < percents > є необов'язковим і має значення по замовчуванню < 10 > (10%). Функція повинна принтануть і вернуть суму, яка буде на рахунку.

def bank():
    start_money = int(input("Write how much money you want to put: "))
    years = int(input("For how many years you want to put: "))
    percents = (input("If you do not know percents, only press 'Enter':"))
    if percents == "":
        percents = 10
    else:
        percents = int(percents)
    
    result_money = start_money*(1+percents/100)**years
    print(round(result_money, 2))
bank()