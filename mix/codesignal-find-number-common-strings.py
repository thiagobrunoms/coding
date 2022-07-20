def solution(s1, s2):
    frequencies1 = [0] * 26
    frequencies2 = [0] * 26

    for letter in s1:
        frequencies1[ord(letter) - ord('a')] += 1

    print(frequencies1)

    for letter in s2:
        frequencies2[ord(letter) - ord('a')] += 1

    print(frequencies2)

    count = 0
    for i in range(26):
        count += min(frequencies1[i], frequencies2[i])

    return count


c = solution('abcd', 'abd')
print(c)
