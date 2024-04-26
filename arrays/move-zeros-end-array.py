# Move all zeroes to end of an Array

class Solution:
    def move_zeros(self, elements: list) -> list:
        index = 0
        number_of_zeros = 0
        length = len(elements)
        while(index < length):
            if  elements[index] == 0:
                del elements[index]
                number_of_zeros = number_of_zeros + 1
                length = length - 1
            else:
                index = index + 1
        
        if (number_of_zeros > 0):
            elements.extend(number_of_zeros * [0])

        return elements
    
    # This versions is a kind of bubble "sort"
    # We use XOR swap to swap values between two positions
    def move_zeros_v2(self, elements: list) -> list:
        j = 0
        for i in range(len(elements)):
            if elements[i] != 0 and elements[j] == 0:
                elements[i] = elements[i] ^ elements[j]
                elements[j] = elements[i] ^ elements[j]
                elements[i] = elements[i] ^ elements[j]
            
            if elements[j] != 0:
                j = j + 1

        return elements


input = [0, 1, 2, 0, 4, 0, 1]
result1 = Solution().move_zeros_v2(input)
result2 = Solution().move_zeros_v2(input)
print(result1)
print(result2)