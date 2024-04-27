class Solution():
    def is_palindrome(self, word: str) -> bool:
        length = len(word)
        last_index = length - 1
        for i in range(length // 2):
            if word[i] != word[last_index] and last_index > i:
                return False
            
            last_index = last_index - 1

        return True
    
#Palindrome test cases
s = Solution()
input = "radar"
result = s.is_palindrome(input)
assert result, "Error!"
input = "level"
result = s.is_palindrome(input)
assert result, "Error!"
input = "racecar"
result = s.is_palindrome(input)
assert result, "Error!"
input = "civic"
result = s.is_palindrome(input)
assert result, "Error!"
input = "kayak"
result = s.is_palindrome(input)
assert result, "Error!"
input = "noon"
result = s.is_palindrome(input)
assert result, "Error!"
input = "rotor"
result = s.is_palindrome(input)
assert result, "Error!"
input = "deified"
result = s.is_palindrome(input)
assert result, "Error!"
input = "madam"
result = s.is_palindrome(input)
assert result, "Error!"
input = "refer"
result = s.is_palindrome(input)
assert result, "Error!"

#Non-palindrome test cases
input = "elephant"
result = s.is_palindrome(input)
assert not result, "Error!"
input = "banana"
result = s.is_palindrome(input)
assert not result, "Error!"
input = "computer"
result = s.is_palindrome(input)
assert not result, "Error!"
input = "house"
result = s.is_palindrome(input)
assert not result, "Error!"
input = "orange"
result = s.is_palindrome(input)
assert not result, "Error!"
input = "table"
result = s.is_palindrome(input)
assert not result, "Error!"
input = "network"
result = s.is_palindrome(input)
assert not result, "Error!"
input = "bottle"
result = s.is_palindrome(input)
assert not result, "Error!"
input = "window"
result = s.is_palindrome(input)
assert not result, "Error!"
input = "guitar"
result = s.is_palindrome(input)
assert not result, "Error!"
