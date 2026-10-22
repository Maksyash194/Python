def month_to_season(месяц):
    if месяц in (1,2,12):
        return "Зима"
    elif месяц <= 5:
        return "Весна"
    elif месяц <= 8:
        return "Лето"
    elif месяц <= 11:
        return "Осень"
num = int(input("Введите число"))
result = month_to_season(num)
print(result)