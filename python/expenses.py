# Пет-проект: анализ расходов за неделю
# Запуск в терминале:  python3 expenses.py
#
# Что делает программа:
#   - хранит траты за 7 дней
#   - считает сумму, среднее, самый дорогой и самый дешёвый день
#   - показывает простой "график" из звёздочек
#
# Новое по сравнению с day01: список (list) и цикл (for). Не пугайся —
# ниже всё подписано.


# ---- 1. Данные ----
# Список — это пронумерованный набор значений в квадратных скобках.
# Тут трата (в рублях) на каждый день недели.
expenses = [450, 1200, 300, 0, 875, 1500, 620]
days = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]


# ---- 2. Базовые числа ----
total = sum(expenses)              # sum() складывает все элементы списка
average = total / len(expenses)    # len() — сколько элементов в списке

most = max(expenses)               # max() — самое большое число
least = min(expenses)              # min() — самое маленькое

# .index(x) находит, на каком месте стоит значение x.
# По этому месту берём название дня из списка days.
most_day = days[expenses.index(most)]
least_day = days[expenses.index(least)]


# ---- 3. Вывод результатов ----
print("=== Анализ расходов за неделю ===")
print(f"Всего потрачено: {total} ₽")
print(f"В среднем в день: {average:.0f} ₽")   # :.0f — округлить до целого
print(f"Самый дорогой день: {most_day} ({most} ₽)")
print(f"Самый дешёвый день: {least_day} ({least} ₽)")
print()


# ---- 4. Простой график из звёздочек ----
# Цикл for проходит по парам (день, трата) одновременно.
# zip() склеивает два списка в пары: ("Пн", 450), ("Вт", 1200), ...
print("График трат:")
for day, amount in zip(days, expenses):
    # одна звёздочка ≈ 100 ₽. // — деление без остатка (целое).
    bar = "*" * (amount // 100)
    print(f"{day}: {bar} {amount} ₽")
print()


# ---- 5. Дни, где потратил больше среднего ----
print("Дни выше среднего:")
for day, amount in zip(days, expenses):
    if amount > average:          # сравниваем трату со средним
        # round() округляет; на сколько именно превысили средний
        over = round(amount - average)
        print(f"{day}: {amount} ₽ (на {over} ₽ больше среднего)")
print()


# ---- 6. Бананомер 🍌 ----
# Сколько бананов можно купить на недельный бюджет?
banana_price = 25                 # цена одного банана в ₽
bananas = total // banana_price   # // — целые бананы, без "половинок"
print(f"На {total} ₽ можно купить {bananas} бананов по {banana_price} ₽ 🍌")
print()


# ---- 7. Счётчик: сколько было "дорогих" дней (> 1000 ₽) ----
count = 0              # счётчик дней
spent_big = 0          # накопитель: сколько всего потрачено в дорогие дни
for amount in expenses:
    if amount > 1000:
        count += 1          # +1 к числу дорогих дней
        spent_big += amount # прибавляем саму трату к накопителю
print(f"Дорогих дней (> 1000 ₽): {count}")
print(f"В них суммарно потрачено: {spent_big} ₽")
print()


# ---- 8. Счётчик дней без трат (ровно 0 ₽) ----
zero_days = 0
for amount in expenses:
    if amount == 0:        # == это сравнение "равно" (не путать с = )
        zero_days += 1
print(f"Дней без трат: {zero_days}")
print()


# ---- 9. То же самое, но через функции ----
# Функция принимает список и порог, возвращает число дней выше порога.
def count_above(numbers, limit):
    count = 0
    for n in numbers:
        if n > limit:
            count += 1
    return count


# Функция возвращает сумму трат выше порога.
def sum_above(numbers, limit):
    s = 0
    for n in numbers:
        if n > limit:
            s += n
    return s


# Теперь одну и ту же функцию вызываем с разными порогами — без копипасты!
print("Анализ через функции:")
for limit in [500, 800, 1000]:
    days_count = count_above(expenses, limit)
    money = sum_above(expenses, limit)
    print(f"Дней дороже {limit} ₽: {days_count}, на сумму {money} ₽")
print()


# ---- 10. Функция среднего ----
def average_of(numbers):
    return sum(numbers) / len(numbers)   # сумма делённая на количество


print(f"Среднее через функцию: {average_of(expenses):.0f} ₽")
