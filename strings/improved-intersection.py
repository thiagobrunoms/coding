# This solution requires that the tow given arrays are sorted and have the same length.

class Solution:
    def intersection(self, arrayA: list, arrayB: list) -> list:
        intersected_array = []
        j = 0
        for i in range(len(arrayA)):
            element = arrayA[i]
            while j < len(arrayB):
                if element == arrayB[j]:
                    intersected_array.append(element)
                    j = j + 1
                    break
                elif element < arrayB[j]:
                    break
                else:
                    j = j + 1

        return intersected_array


arrayA = [13, 27, 35, 40, 49, 55, 59]
arrayB = [17, 35, 39, 40, 55, 58, 60]
s = Solution()
intersection = s.intersection(arrayA, arrayB)
print(intersection)
