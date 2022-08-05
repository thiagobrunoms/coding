def is_palindrome(st):
    length = len(st) - 1
    for i in range(len(st)):
        if st[i] != st[length - i]:
            return False

    return True


def solution(st):
    trailing = ''
    new_word = st
    index = 0
    while not is_palindrome(new_word):
        letter = st[index]
        trailing = letter + trailing
        new_word += trailing
        if is_palindrome(new_word):
            return new_word
        else:
            new_word = st

        index += 1

    return st
