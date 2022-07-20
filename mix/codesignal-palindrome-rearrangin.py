def solution(inputString):
    letters_number = {}
    for letter in inputString:
        if letter not in letters_number:
            letters_number[letter] = 1
        else:
            letters_number[letter] += 1

    if len(inputString) % 2 == 0:
        for value in letters_number.values():
            if value % 2 != 0:
                return False

        return True

    number_of_odds = 0
    for value in letters_number.values():
        if value % 2 != 0:
            number_of_odds += 1

    if number_of_odds == 1:
        return True

    return False
