def spy_game(nums):
    code = [0, 0, 7]
    for num in nums:
        if num == code[0]:
            code.pop(0)
        if not code:
            return True
    return False

# Использование
nums = list(map(int, input("Введите числа через пробел: ").split()))
print("Список содержит 007 в порядке." if spy_game(nums) else "Список не содержит 007 в порядке.")