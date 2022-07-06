class Solution:
    def __init__(self):
        self.cache = {}

    def fib(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2

        if n in self.cache:
            return self.cache[n]

        new_element = self.fib(n-1) + self.fib(n-2)
        self.cache[n] = new_element

        return new_element


s = Solution()
result = s.fib(5)
print(result)

0, 1, 1, 2, 3, 5, 8
