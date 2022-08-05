# def reverse(word, inner=False, index=0):
#     if word[index] == ")":
#         return ""

#     result = reverse(word, True if word[index]
#                      == '(' or inner else False, index + 1)

#     current_letter = word[index]
#     current_letter_condition = current_letter != '(' and current_letter != ')'

#     if inner:
#         return result + (current_letter if current_letter_condition else '')
#     else:
#         return (current_letter if current_letter_condition else '') + result


# s = reverse('foo(bar(baz))blim')
# print(s)

def solution(inputString):
    my_stack: list = []

    start = -1
    end = -1
    i = 0
    while i < len(inputString):
        if inputString[i] == '(':
            my_stack.append(i)
        elif inputString[i] == ')':
            start = my_stack.pop() + 1
            end = i - 1

            the_len = len(inputString)
            inputString = inputString[:start] + \
                inputString[end-the_len:start-the_len-1:-1] + \
                inputString[end+1:]

        i += 1

    text = ''
    for l in inputString:
        if l != '(' and l != ')':
            text += l

    return text


s = solution('foo(bar(baz))blim')
print(s)
