class Solution:
    def reverseString(self, s: list) -> None:
        temp = s[::-1]
        s.clear()
        s += temp

# "thiag" -> "thia" -> "thi" -> "th" -> "t" ->


s = Solution()
s.reverseString(['T', 'h', 'i', 'a', 'g', 'o'])
