jump_minus = 5
jump_plus = 4


def solution(text):
    print('input', text)
    result = ""
    index = 0

    while index < len(text):
        if text[index] == "m":
            result += "-"
            index += jump_minus
        else:
            result += "+"
            index += jump_plus

    return result


# input = "minusplusminus"
input = "plusminusminusplus"
s = solution(input)
print('Result', s)
