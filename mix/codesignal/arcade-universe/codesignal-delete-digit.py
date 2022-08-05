def solution(n):
    digits = []
    while n > 0:
        digit = n % 10
        n = n // 10
        digits.insert(0, digit)

    power = len(digits) - 2
    result = 0
    number = 0
    for remove_index_at in range(len(digits)):
        for each_digit_index in range(len(digits)):
            if remove_index_at != each_digit_index:
                number += digits[each_digit_index] * (10 ** power)
                power -= 1

        if number > result:
            result = number

        power = len(digits) - 2
        number = 0

    return result
