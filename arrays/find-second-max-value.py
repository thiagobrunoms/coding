import math
# Find the second highest value in an array

class Solution:
    def find_second_max_value(self, elements: list) -> int:
        target = float('-inf')
        highest = float('-inf')
        for element in elements:
            if element > highest:
                target = highest
                highest = element
            elif element > target and element < highest:
                target = element

        if math.isinf(target):
            raise Exception('Not found')

        return target


# input = [12, 34, 2, 34, 33, 1] #33
# input = [12, 34, 2] #12
# input = [12, 34, 2, 34, 33, 1, 50] # 34

# Array with unique elements:
input = [1, 2, 3, 4, 5]
# Expected output: 4
# Array with duplicate elements:
# input = [2, 5, 3, 5, 7, 2]
# Expected output: 5
# Array with negative numbers:
# input = [-5, -2, -9, -3, -7]
# Expected output: -3
# Array with mixed positive and negative numbers:
# input = [10, -5, 3, -8, 7]
# Expected output: 7
# Array with repeated highest value:
# input = [2, 5, 9, 5, 7, 9]
# Expected output: 7
# Array with only one unique value:
# input = [3, 3, 3, 3, 3]
# Expected output: No second highest value (some implementations may return None or raise an exception)
try:
    result = Solution().find_second_max_value(input)
    print(result)
except Exception as e:
    print(e)
