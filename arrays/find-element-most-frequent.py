from cmath import e


class Solution:
    def find_highest_frequency(self, elements: list) -> int:
        frequencies_map = {}
        highest = -1
        current_frequency = -1
        found_element = -1

        for element in elements:
            if element not in frequencies_map:
                frequencies_map[element] = 1
                current_frequency = 1
            else:
                frequencies_map[element] += 1
                current_frequency = frequencies_map[element]

            if current_frequency > highest:
                highest = current_frequency
                found_element = element

        return found_element


s = Solution()
result = s.find_highest_frequency(
    [1, 1, 3, 3, 4, 4, 4, 4, 5, 6, 4, 4, 2, 3, 4, 4, 5, 5, 5, 1, 1, 5, 8, 9, 5, 5, 5, 5, 5, 5, 3, 2, 2])
print(result)


#1, 1, 3, 3, 4, 4, 4, 4, 5, 6, 4, 4, 2, 3, 4, 4
