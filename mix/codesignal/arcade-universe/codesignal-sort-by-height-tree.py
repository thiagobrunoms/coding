from calendar import c
from unicodedata import numeric


def solution(list_lines: list) -> list:
    numbers = []
    for element in list_lines:
        if element != -1:
            numbers.append(element)

    numbers.sort()
    count = 0
    for index in range(len(list_lines)):
        if list_lines[index] != -1:
            del list_lines[index]
            list_lines.insert(index, numbers[count])
            count += 1

    return list_lines


#[-1, 150, 160, 170, -1, -1, 180, 190]
s = solution([-1, 150, 190, 170, -1, -1, 160, 180])

print(s)
