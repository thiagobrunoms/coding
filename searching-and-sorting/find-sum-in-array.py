# Given a sorted array A (sorted in ascending order), having N integers, find if there exists any pair of elements (A[i], A[j]) such that their sum is equal to X.

# For this problem, let's use the two pointers technique, such that if array[i] + array[j] < X, then, let's move i plus 1. Otherwise, let's move j minus 1,
# while i < j. Return (i, j) as a tuple for their positions where array[i] + array[j] == X. Otherwise, let's return (-1, -1)

def solution(array, target):
    i = 0
    j = len(array) - 1

    while i < j:
        if array[i] + array[j] > target:
            j -= 1
        elif array[i] + array[j] < target:
            i += 1
        else:
            return (i, j)

    return (-1, -1)


array = [10, 20, 35, 50, 75, 80]
target = 70
s = solution(array, target)
print(s)
