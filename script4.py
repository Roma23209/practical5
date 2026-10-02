def atm_simulation():
    denominations = [5000, 2000, 1000, 500, 200, 100]
    try:
        amount = int(input("Введите сумму для снятия (кратную 100): "))
    except ValueError:
        print("Ошибка: введено не целое число.")
        return
    if amount <= 0:
        print("Ошибка: сумма должна быть больше нуля.")
        return
    if amount % 100 != 0:
        print("Ошибка: банкомат выдает только суммы, кратные 100.")
        return

    print(f"\nОтчет о выдаче для суммы {amount} руб.:")
    for bill in denominations:
        if amount >= bill:
            count = amount // bill
            amount = amount % bill
            print(f"Купюры {bill} руб.: {count} шт.")
if __name__ == "__main__":
    atm_simulation()
