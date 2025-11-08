import itertools

# Все сочетания из 3 элементов по 2
for c in itertools.combinations([1, 2, 3], 2):
    print(c)

# Все перестановки из 3 элементов
for p in itertools.permutations('abc', 2):
    print(p)

# Декартово произведение двух списков
for prod in itertools.product([1, 2], ['a', 'b']):
    print(prod)
