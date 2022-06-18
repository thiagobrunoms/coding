
#WORST CASE: O(n^2)
def bubble_sort_it(elements: list) -> list:
    for i in range(len(elements)-1):
        for j in range(len(elements) - i - 1):
            if elements[j] > elements[j+1]:
                temp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = temp

    return elements


elements = [5, 3, 8, 4, 6]
sorted = bubble_sort_it(elements)
print(sorted)