def string_permutations(string):
    from itertools import permutations
    return [''.join(p) for p in permutations(string)]

# Использование
string = input("Введите строку: ")
print("Перестановки строки:")
for perm in string_permutations(string):
    print(perm)