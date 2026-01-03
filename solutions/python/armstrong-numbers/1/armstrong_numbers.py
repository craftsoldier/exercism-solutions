def is_armstrong_number(number):
    digits = []
    temp = number

    while temp > 0:
        digits.append(temp % 10)
        temp //= 10

    total = sum(d ** len(digits) for d in digits)
    return total == number
