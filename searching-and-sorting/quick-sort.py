def swap(elements: list, i: int, j: int):
    temp = elements[i]
    elements[i] = elements[j]
    elements[j] = temp


def partition(elements: list, left, right) -> int:
    pivot = elements[left]
    i = left

    for j in range(left + 1, right + 1):
        if elements[j] < pivot:
            i += 1
            swap(elements, i, j)

    swap(elements, left, i)

    return i


def quick_sort(elements, left, right):
    if (left < right):
        pivot_index = partition(elements, left, right)
        quick_sort(elements, left, pivot_index - 1)
        quick_sort(elements, pivot_index + 1, right)


unsorted = [7, 8, 1, 2, 90, 4, 65, 32]
quick_sort(unsorted, 0, len(unsorted)-1)
print(unsorted)
# position = partition(unsorted, 0, len(unsorted)-1)
# print('pivot position ' + str(position))
# print('after ', unsorted)
