import math


class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x

        left = 0
        right = x

        while True:
            mid = (left + right) / 2

            square = mid * mid
            if int(square) == x:
                return int(mid)
            elif square > x:
                right = mid
            else:
                left = mid


solution = Solution()
sqrt = solution.mySqrt(16)
print(sqrt)
