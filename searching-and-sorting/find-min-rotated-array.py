
class Solution:
    def findMin(self, nums: list) -> int:
        left = 0
        right = len(nums) - 1

        while (left <= right):
            if (nums[left] <= nums[right]):
                return nums[left]

            mid = (left + right) // 2
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid


# return nums[mid]

# O(N)
# class Solution:
#     def findMin(self, nums) -> int:
#         if len(nums) == 1:
#             return nums[0]

#         found = float('INF')
#         j = len(nums) - 1
#         for i in range(j):
#             if nums[i] < nums[j] and nums[i] < found:
#                 found = nums[i]
#             elif nums[j] < found:
#                 found = nums[j]

#         return found


# [2, 2]  # [11, 13, 1, 3, 5, 7, 9]  # [11, 13, 15, 17]
# [2,3,4,5,1]
thelist = [3, 4, 5, 1, 2]
# [4, 5, 6, 7, 0, 1, 2]  # [3, 4, 5, 1, 2]
s = Solution()
result = s.findMin(thelist)
print(result)

left = 0
right = 1
# mid = 1/2 = 0, 5 = 0
