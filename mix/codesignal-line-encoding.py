# Given a string, return its encoding defined as follows:

# First, the string is divided into the least possible number of disjoint substrings consisting of identical characters
# for example, "aabbbc" is divided into ["aa", "bbb", "c"]
# Next, each substring with length greater than one is replaced with a concatenation of its length and the repeating character
# for example, substring "bbb" is replaced by "3b"
# Finally, all the new strings are concatenated together in the same order and a new string is returned.

def solution(s):
    previous = s[0]
    index = 1
    count = 1
    result = ''
    while index <= len(s):
        current = s[index] if index < len(s) else ''
        if current == previous:
            count += 1
        else:
            count = str(count) if count > 1 else ''
            result += count + previous
            previous = current
            count = 1

        index += 1

    return result
