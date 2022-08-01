import functools

# Given array of integers, find the maximal possible sum of some of its k consecutive elements.

# Example

# For inputArray = [2, 3, 5, 1, 6] and k = 2, the output should be
# solution(inputArray, k) = 8.
# All possible sums of 2 consecutive elements are:

# 2 + 3 = 5;
# 3 + 5 = 8;
# 5 + 1 = 6;
# 1 + 6 = 7.
# Thus, the answer is 8.


def solution(inputArray, k):
    max = functools.reduce(lambda a, b: a + b, inputArray[0:k])
    print('max', max)
    cur = max
    for i in range(k, len(inputArray)):
        print('inputArray[i]', inputArray[i],
              'inputArray[i-k]', inputArray[i-k])
        cur = cur + inputArray[i] - inputArray[i-k]
        print('cur', cur)
        if cur > max:
            max = cur
            print('newmax', max)

    return max


s = solution([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)
print(s)
