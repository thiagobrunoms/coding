from dataclasses import replace

#length = 3
#real_length = 10
#letter = " "
#= M 
#= r
#= %20
class ReplaceWhiteSpace:
    def replace_white_spaces(self, content, length, real_length) -> str:
        pass

# We assume that the string does not start with more than 1 space
class SolutionRecursively(ReplaceWhiteSpace):
    def replace_white_spaces(self, content, length, real_length) -> str:
        print(content)
        if real_length == 0: 
            return ""

        length = length + 1
        letter = content[length] 

        if letter == " ":
            if length == 0 and content[0] == " ": 
                return "" + self.replace_white_spaces(content, length, real_length)
                 
            return "%20" + self.replace_white_spaces(content, length, real_length - 1)

        return content[length] + self.replace_white_spaces(content, length, real_length - 1)

s = SolutionRecursively()
result = s.replace_white_spaces("  Mr John Smith     ", -1, 13)
print(result)
print(len(result))

# s = Solution()
# result = s.replace_white_spaces("John Smith Ok    ", 10)
# print(result)