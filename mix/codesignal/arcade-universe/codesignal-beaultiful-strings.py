def get_map_ocurrences(inputString):
    letter_ocurrences = {}
    for element in inputString:  # O(n)
        if element not in letter_ocurrences:
            letter_ocurrences[element] = 1
        else:
            letter_ocurrences[element] += 1

    return letter_ocurrences

# Time complexity: O(n) + O(n) = O(2n) = O(n)


def solution(inputString):
    letter_ocurrences = get_map_ocurrences(inputString)  # O(n)

    for letter in letter_ocurrences.keys():  # O(n)
        previous_letter_value = ord(letter) - 1 if ord(letter) - 1 > 97 else 97
        if chr(previous_letter_value) not in letter_ocurrences:
            return False

        if letter_ocurrences[letter] > letter_ocurrences[chr(previous_letter_value)]:
            return False

    return True
