from functools import reduce


def is_prime(number):
    for i in range(2, number // 2):
        if number % i == 0:
            return False

    return True


def solution(product):
    if product == 0:
        return 10

    if product == 1:
        return 1

    if is_prime(product):
        return -1

    for number in range(10, 5000):
        digits = []
        current_number = number
        previous_number = current_number
        while current_number > 0:
            digit = current_number % 10
            current_number = current_number // 10
            digits.append(digit)

        result = reduce(lambda a, b: a * b, digits)
        print('result', result)
        if result == product:
            return previous_number

    return -1


s = solution(600)
print(s)
