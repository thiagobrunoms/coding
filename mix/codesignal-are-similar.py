def solution(a, b):
    number_of_differences = 0
    pairs_of_differences = []

    for i in range(len(a)):
        if a[i] != b[i]:
            number_of_differences += 1
            pairs_of_differences.append((a[i], b[i]))

    if number_of_differences > 2:
        return False

    if number_of_differences == 2:
        pair1 = pairs_of_differences[0]
        pair2 = pairs_of_differences[1]

        if pair1[0] != pair2[1] or pair1[1] != pair2[0]:
            return False

    if number_of_differences == 1:
        if pairs_of_differences[0][0] not in b or pairs_of_differences[0][1] not in a:
            return False

    return True


#[1, 2, 3, 4, 5, 6, 7, 8, 9]

# test case: one difference, but one of the elements not in the other array
s = solution([1, 1, 1, 2, 2], [1, 1, 1, 2, 3])
print(s)
