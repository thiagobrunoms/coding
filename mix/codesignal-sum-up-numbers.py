import re


def solution(inputString):
    numbers = re.findall(r'\d+', inputString)
    total = 0
    for n in numbers:
        total += int(n)

    return total


input = '2 apples, 1.2 oranges'
s = solution(input)
print(s)
