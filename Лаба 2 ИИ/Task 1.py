money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 1.05  # Ежемесячный рост цен
count = 1

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

while money_capital >= spend:
    count += 1
    money_capital += salary - spend
    spend *= increase

print("Количество месяцев, которое можно протянуть без долгов:", count)
