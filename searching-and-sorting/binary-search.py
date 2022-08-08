from re import M


class BinarySearch:
    def iteractive_binary_search(self, elements: list, target):
        left = 0
        right = len(elements) - 1
        while left <= right:
            # This option can lead to an interger overflow, since left + right can overflow 32-bit.
            # In order to avoid it, left + (right - left) // 2 would be safer.
            mid = (left + right) // 2

            print('mid', mid)
            if elements[mid] == target:
                return (elements[mid], mid)
            elif target < elements[mid]:
                right = mid - 1
            elif target > elements[mid]:
                left = mid + 1

        return -1

    def recursive_binary_search(self, elements: list, left, right, target):
        if left > right:
            return False

        mid = (left + right) // 2
        if target == elements[mid]:
            return (elements[mid], mid)
        elif target < elements[mid]:
            return self.recursive_binary_search(elements, left, mid - 1, target)
        else:
            return self.recursive_binary_search(elements, mid + 1, right, target)


elements = [1, 2, 3, 4, 5, 6, 7, 8]
bs = BinarySearch()
result = bs.iteractive_binary_search(elements, 8)
# result = bs.recursive_binary_search(elements, 0, len(elements), 10)
print(result)
