# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

# Example 1:

# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

class MainSolution:
    def calculate_area(self, input):
        i = 0
        j = len(input) - 1
        area = 0
        while i < j:
            base = j - i
            height = min(input[i], input[j])
            area = max(area, base * height)
            if input[i] < input[j]:
                i = i + 1
            else:
                j = j - 1
                
        return area

s = MainSolution()
result = s.calculate_area([1,8,6,2,5,4,8,3,7])
print(result)
assert result == 49, 'Failed'

class Solution:
    def __init__(self, input):
        self.input = input

    def calculate_area(self):
        base = len(self.input)
        i = 0
        j = len(self.input) - 1
        area = 0
        while base > 1:
            base = j - i
            height = self.get_height(self.input[i], self.input[j])
            if (self.get_area(base, height) > area):
                area = self.get_area(base, height)

            i = i + 1
            base = j - i
            height = self.get_height(self.input[i], self.input[j])
            if (self.get_area(base, height) > area):
                area = self.get_area(base, height)

            i = i - 1
            j = j - 1
            base = j - i
            height = self.get_height(self.input[i], self.input[j])
            if (self.get_area(base, height) > area):
                area = self.get_area(base, height)

            i = i + 1

        return area

    def get_height(self, value1, value2):
        return value1 if value1 <= value2 else value2

    def get_area(self, base, height):
        return base * height

input = [1,8,6,2,5,4,8,3,7]
s = Solution(input)
result = s.calculate_area()
print(result)
assert result == 49, 'Failed'