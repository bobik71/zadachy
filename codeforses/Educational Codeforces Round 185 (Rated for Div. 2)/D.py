def value_of_char(c, next_c):
    if c == 'X':
        return 10
    if c == 'V':
        return 5
    if c == 'I':
        if next_c in ('X', 'V'):
            return -1
        else:
            return 1
    return 0

def calculate_string_value(s):
    val = 0
    n = len(s)
    for i in range(n):
        next_c = s[i+1] if i+1 < n else None
        val += value_of_char(s[i], next_c)
    return val

def solve_case(n, q, s, queries):
    n = len(s)
    # Преобразуем строку в список для удобной замены
    arr = list(s)

    # Предварительно считаем сколько каждой буквы уже есть
    countX = arr.count('X')
    countV = arr.count('V')
    countI = arr.count('I')
    countQ = arr.count('?')

    # Чтобы минимизировать значение, анализируем знак для 'I' в каждой позиции '?'

    # Для каждого '?' вычисляем возможные последствия выбора 'X', 'V', 'I'
    # Нужно учитывать влияние на предыдущий символ, если он 'I'.

    # Однако, чтобы быстро отвечать на запросы, можно для каждого '?' вычислить
    # предпочтительный порядок выбора букв для минимизации значения.

    # Подход:
    # 1. Для каждой '?' позиция предопределяем "потенциал" при замене на 'I', 'V', 'X'
    # 2. Отсортируем '?' по выгоде замены на буквы с минимальным приращением
    # 3. На запросе распределяем доступные буквы по '?' с минимальной стоимостью

    # Вычислим для каждого '?' позицию и оценочные затраты для каждой буквы
    q_positions = [i for i, ch in enumerate(arr) if ch == '?']

    cost_list = []
    for pos in q_positions:
        next_c = arr[pos+1] if pos+1 < n else None
        prev_c = arr[pos-1] if pos-1 >= 0 else None

        # Стоимость выбора 'X', 'V', 'I' с учётом влияния на 'I' около позиции
        # Также учтём эффект, если предыдущий символ 'I', значение которого может измениться

        # Значения при выборе буквы на позиции pos
        val_X = 10
        val_V = 5
        val_I = 1 if (next_c not in ('X', 'V')) else -1

        # Если предыдущий символ 'I', его стоимость может зависеть от текущ символа
        if prev_c == 'I':
            # если выбираем 'X' или 'V' на текущем месте, предыдущий I будет -1
            # если выбираем 'I', предыдущий I зависит от следующ символа = 'I' -> next_c='I' => prev 'I' = 1
            # но здесь проще учесть отдельно

            # 'I' слева стоит 1 если справа не X/V, иначе -1
            # Сейчас меняется только текущ символ, который правее 'I' слева
            # Поэтому если выбираем 'X' или 'V' текущий символ - prev 'I' становится -1 (выгодно для минимизации)
            # Если выбираем 'I' текущий символ, prev 'I' стоит 1, если не X/V

            val_X += -1 - 1  # prev I изменится с 1 на -1 => уменьшение на 2
            val_V += -1 - 1
            val_I += 1 - (-1) if (next_c not in ('X', 'V')) else 0  # Влияет на текушую I

        cost_list.append((pos, val_X, val_V, val_I))

    results = []
    for cX, cV, cI in queries:
        # Проверяем сколько уже есть и учитываем доступные буквы
        availableX = cX - countX
        availableV = cV - countV
        availableI = cI - countI

        # Создадим массив для замены '?' с указанием минимальных затрат
        # Выбираем для каждого '?' минимальную стоимость и меняем буквы в порядке увеличения стоимости

        # Для каждой '?' определим минимальный выбор по стоимости
        # Будем сортировать '?' по разнице стоимости для разных букв для выбора оптимальной комбинации

        replacements = []
        for (pos, val_X, val_V, val_I) in cost_list:
            options = []
            if availableX > 0:
                options.append(('X', val_X))
            if availableV > 0:
                options.append(('V', val_V))
            if availableI > 0:
                options.append(('I', val_I))

            if not options:
                # Для ситуации, когда не осталось доступных букв (должно не происходить из условий)
                options = [('I', val_I), ('V', val_V), ('X', val_X)]
            # Выбираем минимальное значение
            chosen_letter, chosen_cost = min(options, key=lambda x: x[1])
            replacements.append((pos, chosen_letter, chosen_cost))

            # Уменьшаем доступные количества исходя из выбранной буквы
            if chosen_letter == 'X':
                availableX -= 1
            elif chosen_letter == 'V':
                availableV -= 1
            elif chosen_letter == 'I':
                availableI -= 1

        # Формируем итоговую строку для подсчёта значения
        final_str = arr[:]
        for pos, letter, _ in replacements:
            final_str[pos] = letter

        val = calculate_string_value(final_str)
        results.append(val)
    return results

# Пример чтения входных данных и вызова функции решения
import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    s = input().strip()
    queries = [tuple(map(int, input().split())) for __ in range(q)]
    res = solve_case(n, q, s, queries)
    print('\n'.join(map(str, res)))
