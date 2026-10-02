TAX_RATE = 0.13
annual_income = float(input("Введите ваш годовой доход: "))
tax_amount = annual_income * TAX_RATE
net_income = annual_income - tax_amount
print(f"Общая сумма дохода: {annual_income:,.2f}".replace(",", " ") + " руб.")
print(f"Сумма рассчитанного налога: {tax_amount:,.2f}".replace(",", " ") + " руб.")
print(f"Сумма «на руки» после вычета налога: {net_income:,.2f}".replace(",", " ") + " руб.")
