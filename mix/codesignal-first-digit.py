import re

s = "var_1__Int"
s = 'q2q-q'
s = '0ss'

result = re.findall(r'\d', s)  # adds + for more digits
print(result[0])
