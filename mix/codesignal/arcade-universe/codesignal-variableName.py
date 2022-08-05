import re


def solution(variable):
    regex = "[a-zA-Z_][a-zA-Z0-9_]*"
    pat = re.compile(regex)
    if re.fullmatch(pat, variable):
        return True

    return False


s = solution("2w2")
print(s)
