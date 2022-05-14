# String Compression: Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. If the
# "compressed" string would not become smaller than the original string, your method should return
# the original string. You can assume the string has only uppercase and lowercase letters (a - z).
# Hints: #92, # 11 0

class Solution:
    def compress_string(self, content: str) -> str:
        compressed = ""
        count_letter = 0

        for i in range(len(content)):
            count_letter += 1

            if i + 1 >= len(content) or content[i] != content[i + 1]:
                compressed = compressed + content[i] + str(count_letter)
                count_letter = 0

        return compressed if len(compressed) < len(content) else content

s = Solution()
result = s.compress_string("abcccrcccaarraabbddddce")
print(result)

result = s.compress_string("abcccrcccaarraabbdddd")
print(result)
