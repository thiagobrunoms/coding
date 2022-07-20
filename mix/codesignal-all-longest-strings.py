def solution(inputArray):
    highest_strings = {}
    highest_len = -1

    for word in inputArray:
        word_len = len(word)
        if word_len >= highest_len:
            highest_len = word_len

            if highest_len not in highest_strings:
                highest_strings[highest_len] = [word]
            else:
                highest_strings[highest_len].append(word)

    return highest_strings[highest_len]
