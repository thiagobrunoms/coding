n = 50

results = {}
for i in range(1, n+2):
    for j in range(1, n+2):
        result = i**3 + j**3
        if result in results:
            results[result].append((i,j))
        else:
            results[result] = [(i, j)]


for item, value_list in results.items():
    for pair1 in value_list:
        for pair2 in value_list:
            print(pair1, pair2)