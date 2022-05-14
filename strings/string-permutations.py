input = "thiago"  
permutations = set() 
substring = []
substring.append(input[0])
permutations.add(tuple(substring))

for next_letter_index in range(1, len(input)):     
    next_letter = input[next_letter_index]

    for i in range(len(substring)+1):
        temp = substring.copy()
        temp.insert(i, next_letter)
        print("Nova permuta ", temp)
        permutations.add(tuple(temp))

    substring = [letter for letter in input[0:next_letter_index+1]]

print(permutations)
print(len(permutations))