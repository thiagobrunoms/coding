class Solution:
    def compress_string(self, content: str) -> str:
        compressed = ""

        previous_letter = content[0]
        count_letter = 0
        for i in range(1, len(content)):
            current_letter = content[i]
            
            if current_letter == previous_letter:
                count_letter += 1
            else:
                count_letter += 1
                compressed = compressed + previous_letter + str(count_letter)
                count_letter = 0
                    
            previous_letter = current_letter


        if count_letter > 0 or previous_letter == current_letter:
            count_letter += 1
            compressed = compressed + current_letter + str(count_letter)

        return compressed

s = Solution()
result = s.compress_string("abcccrcccaarraabbddddce")
print(result)
