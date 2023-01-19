# Задача 15. Група запалянковци решили да си закупят билети за Евро 2016. Цената на
# билета се определя спрямо две категории:
# VIP – 499.99 лева
# Normal – 249.99 лева
# Запалянковците имат определен бюджет, a броят на хората в групата определя какъв процент от бюджета трябва да се задели за транспорт:
# От 1 до 4 – 75% от бюджета
# От 5 до 9 – 60% от бюджета
# От 10 до 24 – 50% от бюджета
# От 25 до 49 – 40% от бюджета
# 50 или повече – 25% от бюджета
# да си купят билети за избраната категория, както и колко пари ще им останат или ще са им нужни.
# Входни данни
# Входът се чете от конзолата и съдържа точно 3 реда:
# На първия ред е бюджетът – реално число в интервала [1 000.00 … 1 000 000.00.
# На втория ред е категорията – "VIP" или "Normal".
# На третия ред е броят на хората в групата – цяло число в интервала [1 … 200].
# Изходни данни
# Да се отпечата на конзолата един ред:
# Ако бюджетът е достатъчен:
# "Yes! You have {N} leva left." – където N са останалите пари на групата.
# Ако бюджетът НЕ Е достатъчен:
# "Not enough money! You need {М} leva." – където М е сумата, която не достига.
# Сумите трябва да са форматирани с точност до два символа след десетичния знак

while True:
    try:
        budget = int(input("Our budget is: "))
        if budget in range(1000, 1000001):
            category = input("Please choose 'VIP' or 'Normal': ")
            n_part = int(input("Please choose participants:"))
            if n_part in range(1, 201):
                if n_part in range(1, 5):
                    spendings = (75 * budget) / 100
                    rem_transport = budget - spendings  # 1000 - 750 = 250
                    if category == "Normal":
                        price_ticket = 249.99
                        remaining_ticket = price_ticket * n_part
                        if rem_transport > remaining_ticket:
                            left = rem_transport - remaining_ticket
                            print(f"Yes! You have {round(left, 2)} leva left.")
                            break
                        else:
                            left = remaining_ticket - rem_transport
                            print(f"Not enough money! You need {round(left, 2)} leva.")
                            break
                    elif category == "VIP":
                        price_ticket = 499.99
                        remaining_ticket = price_ticket * n_part  # for 1 pers:499.99
                        if rem_transport > remaining_ticket:
                            left = rem_transport - remaining_ticket
                            print(f"Yes! You have {round(left, 2)} leva left.")
                            break
                        else:
                            left = remaining_ticket - rem_transport
                            print(f"Not enough money! You need {round(left, 2)} leva.")
                            break
                    else:
                        print("Please choose 'Normal' or 'VIP'")
                elif n_part in range(5, 10):
                    spendings = (60 * budget) / 100
                    rem_transport = budget - spendings  # 1000 - 750 = 250
                    if category == "Normal":
                        price_ticket = 249.99
                        remaining_ticket = price_ticket * n_part
                        if rem_transport > remaining_ticket:
                            left = rem_transport - remaining_ticket
                            print(f"Yes! You have {round(left, 2)} leva left.")
                            break
                        else:
                            left = remaining_ticket - rem_transport
                            print(f"Not enough money! You need {round(left, 2)} leva.")
                            break
                    elif category == "VIP":
                        price_ticket = 499.99
                        remaining_ticket = price_ticket * n_part  # for 1 pers:499.99
                        if rem_transport > remaining_ticket:
                            left = rem_transport - remaining_ticket
                            print(f"Yes! You have {round(left, 2)} leva left.")
                            break
                        else:
                            left = remaining_ticket - rem_transport
                            print(f"Not enough money! You need {round(left, 2)} leva.")
                            break
                    else:
                        print("Please choose 'Normal' or 'VIP'")
                elif n_part in range(10, 25):
                    spendings = (50 * budget) / 100
                    rem_transport = budget - spendings
                    if category == "Normal":
                        price_ticket = 249.99
                        remaining_ticket = price_ticket * n_part
                        if rem_transport > remaining_ticket:
                            left = rem_transport - remaining_ticket
                            print(f"Yes! You have {round(left, 2)} leva left.")
                            break
                        else:
                            left = remaining_ticket - rem_transport
                            print(f"Not enough money! You need {round(left, 2)} leva.")
                            break
                    elif category == "VIP":
                        price_ticket = 499.99
                        remaining_ticket = price_ticket * n_part  # for 1 pers:499.99
                        if rem_transport > remaining_ticket:
                            left = rem_transport - remaining_ticket
                            print(f"Yes! You have {round(left, 2)} leva left.")
                            break
                        else:
                            left = remaining_ticket - rem_transport
                            print(f"Not enough money! You need {round(left, 2)} leva.")
                            break
                    else:
                        print("Please choose 'Normal' or 'VIP'")
                elif n_part in range(25, 50):
                    spendings = (40 * budget) / 100
                    rem_transport = budget - spendings
                    if category == "Normal":
                        price_ticket = 249.99
                        remaining_ticket = price_ticket * n_part
                        if rem_transport > remaining_ticket:
                            left = rem_transport - remaining_ticket
                            print(f"Yes! You have {round(left, 2)} leva left.")
                            break
                        else:
                            left = remaining_ticket - rem_transport
                            print(f"Not enough money! You need {round(left, 2)} leva.")
                            break
                    elif category == "VIP":
                        price_ticket = 499.99
                        remaining_ticket = price_ticket * n_part  # for 1 pers:499.99
                        if rem_transport > remaining_ticket:
                            left = rem_transport - remaining_ticket
                            print(f"Yes! You have {round(left, 2)} leva left.")
                            break
                        else:
                            left = remaining_ticket - rem_transport
                            print(f"Not enough money! You need {round(left, 2)} leva.")
                            break
                    else:
                        print("Please choose 'Normal' or 'VIP'")
                else:
                    spendings = (25 * budget) / 100
                    rem_transport = budget - spendings  # 1000 - 250 = 750
                    if category == "Normal":
                        price_ticket = 249.99
                        remaining_ticket = price_ticket * n_part
                        if rem_transport > remaining_ticket:
                            left = rem_transport - remaining_ticket
                            print(f"Yes! You have {round(left, 2)} leva left.")
                            break
                        else:
                            left = remaining_ticket - rem_transport
                            print(f"Not enough money! You need {round(left, 2)} leva.")
                            break
                    elif category == "VIP":
                        price_ticket = 499.99
                        remaining_ticket = price_ticket * n_part  # for 1 pers:499.99
                        if rem_transport > remaining_ticket:
                            left = rem_transport - remaining_ticket
                            print(f"Yes! You have {round(left, 2)} leva left.")
                            break
                        else:
                            left = remaining_ticket - rem_transport
                            print(f"Not enough money! You need {round(left, 2)} leva.")
                            break
                    else:
                        print("Please choose 'Normal' or 'VIP'")
            else:
                print("Participants need to be between 1 and 200")
        else:
            print("Not enough money. Budget must be between 1000.00 and 1 000 000.00 leva.")
            break
    except ValueError:
        print("Only NUMERICAL entry is allowed.")
