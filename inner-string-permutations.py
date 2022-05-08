s = "abbc"
b = "cbabadcbbabbcbabaabccbabc"

values = {}
s_sum = 0
letter_value = 2
max_substring_size = len(s)
results = []

for letter in s:
    if letter not in values:
        letter_value = letter_value ** 2
        values[letter] = letter_value
    
    s_sum += values[letter]

i = 0
while i + len(s) <= len(b):
    sum = 0
    substring = b[i:max_substring_size]
    for letter in substring:
        if letter not in values:
            break
        
        sum += values[letter]

    if sum == s_sum:
        results.append(substring)

    i = i + 1
    max_substring_size = max_substring_size + 1


print(results)


