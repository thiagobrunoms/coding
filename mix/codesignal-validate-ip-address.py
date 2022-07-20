def solution(inputString):
    numbers_list = inputString.split('.')
    if len(numbers_list) != 4:
        return False

    for octecto in numbers_list:
        if len(octecto) > 1 and octecto[0] == '0':
            print(len(octecto))
            print('en')
            return False

        try:
            octecto = int(octecto)
            if octecto < 0 or octecto > 255:
                return False
        except ValueError:
            return False

    return True


s = solution('0.254.255.0')
print(s)
