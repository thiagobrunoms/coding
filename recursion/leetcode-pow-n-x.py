
# Not working for negative exponents
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        if n > 0:
            return x * self.myPow(x, n - 1)
        else:
            return 1 / x * self.myPow(x, n + 1)


s = Solution()
result = s.myPow(3, 0.03)
print(result)


# if (n == 0):
#             return 1
#         elif (int(n % 2) == 0):
#             return (self.myPow(x, int(n / 2)) *
#                     self.myPow(x, int(n / 2)))
#         else:
#             return (x * self.myPow(x, int(n / 2)) *
#                     self.myPow(x, int(n / 2)))
