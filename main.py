import random

rules = {"камень": ["ножницы", "ящерица"],
        "ножницы": ["бумага", "ящерица"],
        "бумага": ["камень", "спок"],
        "ящерица": ["бумага", "спок"],
        "спок": ["камень", "ножницы"]}

while True:
    tim = input("Тимур выбрал: ").lower()

    if tim not in rules:
        print("Тимур выбрал несуществующий объект")
        continue

    pit = random.choice(list(rules.keys()))
    print(f"Петя выбрал: {pit}")

    if tim == pit:
        print("Ничья!")
    elif pit in rules[tim]:
        print("Тимур победил!")
    else:
        print("Петя победил!")

    play_again = input("Хотите сыграть еще раз? (да/нет): ").lower()
    if play_again != "да":
        break
