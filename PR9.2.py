import math

def is_prime_recursive(n, divisor=2):
    """
    Рекурсивно проверяет, является ли n простым числом 

    Args:
        n: Число, которое нужно проверить на простоту.
        divisor: Текущий делитель, который проверяется.

    Returns:
        "YES", если n простое, "NO" в противном случае.
    """
    if n <= 1:
        return "NO"  # Числа меньше или равны 1 не являются простыми
    if divisor > int(math.sqrt(n)):
        return "YES"  # Если делителей не найдено до квадратного корня, число простое
    if n % divisor == 0:
        return "NO"  # Если n делится на divisor без остатка, оно не простое
    return is_prime_recursive(n, divisor + 1)  # Рекурсивный вызов для следующего делителя


n = int(input("Введите целое число больше 1: "))
result = is_prime_recursive(n)
print(result)

