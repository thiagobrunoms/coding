import re


def solution(inputString):
    return re.sub("[^0-9]+.*", '', inputString)

# def solution(inputString):
#     longest = ''
#     word = ''
#     checked = False
#     for i in range(len(inputString)):
#         if inputString[i].isdigit():
#             word += inputString[i]
#         else:
#             checked = True
#             before_word = inputString[i-len(word)-1]
#             after_word = inputString[i]
#             print('after', after_word)
#             if before_word != ' ' and after_word != ' ':
#                 if len(word) > len(longest):
#                     longest = word

#             word = ''

#     if not checked:
#         longest = word

#     return longest
