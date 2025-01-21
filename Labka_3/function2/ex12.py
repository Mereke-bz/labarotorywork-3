def histogram(lst):
    for num in lst:
        print('*' * num)

# Использование
lst = list(map(int, input("Введите числа через пробел: ").split()))
print("Гистограмма:")
histogram(lst)
