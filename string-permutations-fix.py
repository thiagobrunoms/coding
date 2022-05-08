input = "thiago"  
input = set(input)
input_copy = input.copy()
permutations = set()

for next_letter in input_copy: 
    print("NEXT LETTER ", next_letter)
    input.remove(next_letter)
    content = [letter for letter in input]

    for i in range(len(input)+1):
        temp = content.copy()
        temp.insert(i, next_letter)
        print("Nova permuta ", temp)
        permutations.add(tuple(temp))

    
    input.add(next_letter)

print(permutations)
print(len(permutations))