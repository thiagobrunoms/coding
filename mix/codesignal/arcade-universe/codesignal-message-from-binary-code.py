def solution(code):
    power = 7
    word = ""
    number = 0
    for i in range(0, len(code)):
        bit = int(code[i])
        decimal = bit * 2 ** power
        print(decimal)
        number += decimal
        power -= 1

        if power < 0:
            letter = chr(number)
            word += letter
            power = 7
            number = 0

    return word


s = solution('010010000110010101101100011011000110111100100001')
print(s)
