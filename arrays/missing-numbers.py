class Solution:            
    def missing_numbers(self, elements: list) -> int:
        n = len(elements) + 1
        sum = (n * (n + 1)) / 2
        for element in elements:
            sum = sum - element
            
        return sum

input = [1, 2, 3, 5] #4
result = Solution().missing_numbers(input)
print(result)
