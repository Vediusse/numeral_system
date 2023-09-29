import math

ROUND_CONST = 5


def decimal_to_fibonacci(decimal: int) -> str:
    if decimal == 0:
        return "0"
    elif decimal == 1:
        return "1"
    else:
        fib_sequence = [1, 1]
        while fib_sequence[-1] < decimal:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

        fib_representation = ""
        for fib_num in reversed(fib_sequence[:-1]):
            if decimal >= fib_num:
                fib_representation += "1"
                decimal -= fib_num
            else:
                fib_representation += "0"
        return fib_representation


def fibonacci_to_decimal(fibonacci: str) -> int:
    result = 0
    fibonacci = fibonacci[::-1]
    fib_value = 1
    fib_prev = 0
    for digit in fibonacci:
        if digit == "1":
            result += fib_value

        fib_value, fib_prev = fib_value + fib_prev, fib_value
    return result


def factorial_to_decimal(factorial_num: str) -> int:
    decimal_num = 0
    for i, digit in enumerate(reversed(factorial_num), start=1):
        decimal_num += int(digit) * math.factorial(i)
    return decimal_num


# Функция для перевода числа из десятичной системы счисления в факториальную
def decimal_to_factorial(decimal_num) -> str:
    factorial_num = ""
    i = 1
    while decimal_num > 0:
        remainder = decimal_num % i
        factorial_num = str(remainder) + factorial_num
        decimal_num //= i
        i += 1
    return factorial_num[:-1]




def convert_base(number, current, base):
    if isinstance(number, str):
        n = int(number, current)
    else:
        n = int(number)
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < base:
        return alphabet[n]

    return convert_base(n // base, current, base) + alphabet[n % base]


def convert_base_with_float_number(number: str, current: int, base: int) -> str:
    integer_part, fractional_part = number.split('.') if '.' in number else (number, '0')
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    integer_result = int(convert_base(str(integer_part), current, base))
    fractional_result = ""
    fractional_n = 0
    fractional_base = -1
    for digit in fractional_part:
        fractional_n += int(digit) * (current ** fractional_base)
        fractional_base -= 1
    n = integer_result + fractional_n
    fractional_part = n - int(n)
    for _ in range(ROUND_CONST):
        fractional_part *= base
        digit = int(fractional_part)
        fractional_result += alphabet[digit]

        fractional_part -= digit

    return f"{integer_result}.{fractional_result}"



