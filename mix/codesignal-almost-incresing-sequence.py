

# 1, 3, 2, 6, 7
# 1, 2, 5, 3, 5 -> 1, 2, 3, 5
# 10, 1, 2, 3, 4, 5 -> 1, 2, 3, 4, 5...
# [1, 3, 2, 1] -> 1, 2, 1
# [1, 2, 1, 2] -> 1, 1, 2
# [1, 2, 3, 4, 5, 3, 5, 6] -> [1, 2, 3, 4, 3, 5, 6]

def solution(sequence):
    # Stores the count of numbers that
    # are needed to be removed
    count = 0

    # Store the index of the element
    # that needs to be removed
    index = -1

    # Traverse the range [1, N - 1]
    for i in range(1, len(sequence)):

        # If arr[i-1] is greater than
        # or equal to arr[i]
        if (sequence[i - 1] >= sequence[i]):
            # Increment the count by 1
            count += 1

            # Update index
            index = i

    # If count is greater than one
    if (count > 1):
        print('false1')
        return False

    # If no element is removed
    if (count == 0):
        return True

    # If only the last or the
    # first element is removed
    if (index == len(sequence) - 1 or index == 1):
        print('aqui1')
        return True

    # If a[index] is removed
    if (sequence[index - 1] < sequence[index + 1]):
        print('aqui2')
        return True

    # If a[index - 1] is removed
    if (sequence[index - 2] < sequence[index]):
        print('aqui3')
        return True

    return False


s = solution([10, 20, 30, 40, 50, 60, 10, 20, 30])
print(s)
