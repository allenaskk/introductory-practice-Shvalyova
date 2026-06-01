# Итоговая мини-программа
# Вариант 1. Калькулятор рентабельности

# =====================================================
# Функция для расчёта рентабельности
# =====================================================

def calculate_profitability(revenue, costs):
    """
    Рассчитывает прибыль и рентабельность.
    Прибыль = выручка - затраты
    Рентабельность = (прибыль / выручка) * 100%
    """
    profit = revenue - costs
    
    # Защита от деления на ноль
    if revenue > 0:
        profitability = (profit / revenue) * 100
    else:
        profitability = 0
    
    return profit, profitability


# =====================================================
# Функция для оценки рентабельности
# =====================================================

def get_rating(profitability):
    """
    Возвращает оценку рентабельности:
    > 20% - высокая
    10-20% - средняя
    < 10% - низкая
    """
    if profitability > 20:
        return "высокая"
    elif profitability >= 10:
        return "средняя"
    else:
        return "низкая"


# =====================================================
# Основная часть программы
# =====================================================

print("\n" + "="*50)
print("КАЛЬКУЛЯТОР РЕНТАБЕЛЬНОСТИ")
print("="*50)

# Ввод данных с проверкой
print("\nВведите данные для анализа:")

company_name = input("Название компании: ")

# Проверка на корректный ввод выручки
while True:
    try:
        revenue = float(input("Выручка (руб.): "))
        if revenue < 0:
            print("Выручка не может быть отрицательной! Попробуйте снова.")
            continue
        break
    except ValueError:
        print("Ошибка! Введите число. Попробуйте снова.")

# Проверка на корректный ввод затрат
while True:
    try:
        costs = float(input("Затраты (руб.): "))
        if costs < 0:
            print("Затраты не могут быть отрицательными! Попробуйте снова.")
            continue
        break
    except ValueError:
        print("Ошибка! Введите число. Попробуйте снова.")

# Расчёт
profit, profitability = calculate_profitability(revenue, costs)
rating = get_rating(profitability)

# Вывод отчёта
print("\n" + "="*50)
print(f"ОТЧЁТ ПО КОМПАНИИ: {company_name}")
print("="*50)
print(f"Выручка: {revenue:,.2f} руб.")
print(f"Затраты: {costs:,.2f} руб.")
print(f"Прибыль: {profit:,.2f} руб.")
print(f"Рентабельность: {profitability:.1f}%")
print(f"Оценка: {rating}")

# Дополнительный вывод в зависимости от результата
if profit > 0:
    print("\n▶ Компания работает ПРИБЫЛЬНО! ✅")
elif profit < 0:
    print("\n▶ Компания работает УБЫТОЧНО. ❌ Нужно оптимизировать расходы.")
else:
    print("\n▶ Компания работает БЕЗУБЫТОЧНО. ⚖️")

print("="*50)

# =====================================================
# Дополнительно: анализ нескольких периодов (цикл for)
# =====================================================

print("\n" + "="*50)
print("АНАЛИЗ НЕСКОЛЬКИХ ПЕРИОДОВ (для практики цикла)")
print("="*50)

num_periods = int(input("Сколько периодов хотите проанализировать? "))

print("\nРезультаты анализа:")
print("-" * 40)

for period in range(1, num_periods + 1):
    print(f"\nПериод {period}:")
    p_revenue = float(input(f"  Выручка: "))
    p_costs = float(input(f"  Затраты: "))
    p_profit, p_prof = calculate_profitability(p_revenue, p_costs)
    p_rating = get_rating(p_prof)
    
    if p_profit > 0:
        status = "✅ Прибыль"
    elif p_profit < 0:
        status = "❌ Убыток"
    else:
        status = "⚖️ Ноль"
    
    print(f"  Результат: {p_profit:.2f} руб. ({status})")
    print(f"  Рентабельность: {p_prof:.1f}% ({p_rating})")

print("\n" + "="*50)
print("Программа завершена. Спасибо за использование!")
print("="*50)