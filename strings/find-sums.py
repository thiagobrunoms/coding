numbers = [1, 7, 5, 9, 2, 12, 3]
seen_numbers = {}
pairs = {}

for n in numbers:
    find_n1 = n - 2
    find_n2 = n + 2

    if find_n1 in seen_numbers and ((n, find_n1) not in pairs and (find_n1, n) not in pairs):
        pairs[(n, find_n1)] = True
    elif find_n2 in numbers and ((n, find_n2) not in pairs and (find_n2, n) not in pairs):
        pairs[(n, find_n2)] = True

    seen_numbers[n] = True

print(pairs)
    
