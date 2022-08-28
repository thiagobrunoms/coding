# Problem: You are given an integer m (1 � m � 1 000 000) and two non-empty, zero-indexed
# arrays A and B of n integers, a0, a1, . . . , an−1 and b0, b1, . . . , bn−1 respectively (0 � ai, bi � m).
# The goal is to check whether there is a swap operation which can be performed on these
# arrays in such a way that the sum of elements in array A equals the sum of elements in
# array B after the swap. By swap operation we mean picking one element from array A and
# one element from array B and exchanging them.

# NEEDS MORE CHECKS!!!



def solution(array1, array2):
    sum_a = sum(array1)
    sum_b = sum(array2)

    d = sum_a - sum_b if sum_a > sum_b else sum_b - sum_a
    for element in array2:
        if element == d // 2:
            return True


# array1 = [2, 4, 6, 8, 10, 0]
# array2 = [2, 3, 10, 10, 6, 1]

array1 = [5, 4, 6, 8, 10, 0]
array2 = [2, 6, 10, 10, 6, 1]

s = solution(array1, array2)
print(s)
