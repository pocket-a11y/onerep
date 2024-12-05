from math import pow

print('№1')

def factorial_recursive(n):
    """Рекурсивная функция для вычисления факториала."""
    if n == 0:
        return 1
    elif n < 0:
        return None  # Обработка ошибки: факториал не определен для отрицательных чисел
    else:
        return n * factorial_recursive(n - 1)

def f(x, n):
    """Вычисляет x**n / n! используя рекурсивный факториал."""
    fact = factorial_recursive(n)
    if fact is None:
        return None  # Передаем ошибку из factorial_recursive
    return pow(x, n) / fact

a = int(input())
b = int(input())
result = f(a, b)
if result is None:
    print("Ошибка: факториал не определен для отрицательных чисел.")
else:
    print(result)


