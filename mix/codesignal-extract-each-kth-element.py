# Given array of integers, remove each kth element from it.

# Example

# For inputArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] and k = 3, the output should be
# solution(inputArray, k) = [1, 2, 4, 5, 7, 8, 10].


def solution(inputArray, k):
    count = 0
    index = 0
    while index < len(inputArray):
        count = (count % k) + 1
        if count == k:
            inputArray.pop(index)
        else:
            index += 1

    return inputArray


s = solution([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)
print(s)

# cleaner solution
# [item for i, item in enumerate(a) if (i+1) % 3 != 0]
