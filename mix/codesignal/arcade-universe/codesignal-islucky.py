# Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.

# Given a ticket number n, determine if it's lucky or not.
import math


def solution(n):
    count = 0
    sum_left_half = 0
    sum_right_half = 0

    index = int(math.log(n, 10))
    for index in range(index, -1, -1):
        algarism = (n // (10 ** index)) % 10

        if index > count:
            sum_left_half += algarism
        else:
            sum_right_half += algarism

        count += 1

    return sum_left_half == sum_right_half
