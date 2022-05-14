# Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palin-
# drome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation
# is a rea rrangement of letters. The palindrome does not need to be limited to just dictionary words.
# EXAMPLE
# Input: Tact Coa
# Output: True (permutations: "taco cat". "atco cta". etc.)

class Solution:
    def is_palindrome_permutation(self, content) -> bool:
        structure = {}

        for letter in content:
            letter = letter.lower()
            structure[letter] = 1 if letter not in structure else structure[letter] + 1 

        found_odd_number = False
        for letter in content:
            if structure[letter.lower()] % 2 != 0:
                if found_odd_number:
                    return True
                else:
                    found_odd_number = True

        return True

s = Solution()
result = s.is_palindrome_permutation("Arara")
print(result)


            