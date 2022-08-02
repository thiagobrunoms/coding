import re


def solution(text):
    words = s = re.findall('[a-zA-Z]+', text)
    result = ''
    for word in words:
        if len(word) > len(result):
            result = word

    return result


s = solution("Ready, steady, go!")
print(s)
