# class Solution:
# def isEven(self, number) -> bool:
#     return number % 2 == 0

#     def findPeakElement(self, nums: list) -> int:
#         if len(nums) == 1:
#             return 0
#         elif len(nums) == 2:
#             if nums[0] > nums[1]:
#                 return 0
#             elif nums[1] > nums[0]:
#                 return 1
#             else:
#                 return -1
#         elif nums[len(nums) - 1] > nums[len(nums) - 2]:
#             return len(nums) - 1
#         elif nums[0] > nums[1]:
#             return 0

#         if self.isEven(len(nums)):
#             right = len(nums)
#         else:
#             right = len(nums) - 1

#         left = 0
#         looking_left = True
#         looking_right = True

#         while (looking_left or looking_right):
#             if left >= right:
#                 if looking_left:
#                     looking_left = False
#                     left = len(nums) // 2
#                     right = len(nums) - 1
#                 elif looking_right:
#                     return -1

#             mid = (left + right) // 2
#             print('left', left, 'right', right, 'mid', mid)

#             if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
#                 return mid
#             elif looking_left:
#                 right = mid
#             elif looking_right:
#                 left = mid

#             break


# s = Solution()
# result = s.findPeakElement([3, 2, 1])
# print(result)

# class Solution:
#     def isEven(self, number) -> bool:
#         return number % 2 == 0

#     def findPeakElement(self, nums: list) -> int:
#         if len(nums) == 1:
#             return 0
#         elif len(nums) == 2:
#             if nums[0] > nums[1]:
#                 return 0
#             elif nums[1] > nums[0]:
#                 return 1
#             else:
#                 return -1

#         left = 0
#         right = len(nums)
#         looking_left = True
#         looking_right = True

#         while (looking_left or looking_right):
#             if left >= right:
#                 if looking_left:
#                     looking_left = False
#                     left = len(nums) // 2
#                     right = len(nums)
#                 elif looking_right:
#                     return -1

#             mid = (left + right) // 2
#             print('left', left, 'right', right, 'mid', mid)
#             if mid == 0:
#                 if nums[0] > nums[1]:
#                     return 0
#             elif mid == len(nums)-1 and nums[mid] > nums[mid - 1]:
#                 return mid

#             if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
#                 return mid
#             elif looking_left:
#                 right = mid
#             elif looking_right:
#                 left = mid

class Solution():
    def findPeakElement(self, nums):
        if len(nums) == 1:
            return 0
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid+1]:
                right = mid
            else:
                left = mid + 1

        return left


s = Solution()
thelist = [2, 3, 4, 3, 2, 1]
# thelist = [1, 2, 3]
result = s.findPeakElement(thelist)
print(result)
