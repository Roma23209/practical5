USD_TO_RUB = 83.57
def convert_usd_to_rub(amount_usd):
    return amount_usd * USD_TO_RUB
if __name__ == "__main__":
    try:
        usd_input = float(input("Введите сумму в долларах (USD): "))
        rub_result = convert_usd_to_rub(usd_input)
        print(f"Сумма в рублях: {rub_result:.2f} руб. (по курсу {USD_TO_RUB})")
    except ValueError:
        print("Ошибка: пожалуйста, введите корректное число.")
