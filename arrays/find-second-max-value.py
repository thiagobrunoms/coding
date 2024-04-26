# Find the second highest value in an array

class Solution:
    def find_second_max_value(self, elements: list) -> int:
        target = -1
        highest = -1
        for element in elements:
            if element > highest:
                target = highest
                highest = element
            elif element > target and element < highest:
                target = element

        return target


# input = [12, 34, 2, 34, 33, 1] #33
# input = [12, 34, 2] #12
input = [12, 34, 2, 34, 33, 1, 50] # 34
result = Solution().find_second_max_value(input)
print(result)