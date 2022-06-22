# rotated = []
# for i in range(0, len(a)):
#     rotated.insert(a[(i+r) % len(a)], a[i])


# [6, 7, 0, 1, 2, 3, 4, 5]
# rotation factor 2
# target = 6
def search_in_rotated(elements: list, target: int) -> int:
    list_size = len(elements)  # 8

    # it also gives the position of element 0
    rotation_factor = list_size - elements[0]  # 8 - 6 = 2

    left = -1
    right = len(elements)
    if target <= (list_size - rotation_factor - 1):  # 8 - 2 - 1 = 5
        left = rotation_factor
    else:
        left = 0
        right = rotation_factor - 1

    while (left <= right):
        mid = (left + right) // 2

        if elements[mid] == target:
            return mid
        elif target > elements[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return -1


our_list = [3, 4, 5, 6, 0, 1, 2]
index = search_in_rotated(our_list, 0)
print(index)
