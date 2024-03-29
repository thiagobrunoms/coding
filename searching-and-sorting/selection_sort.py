
# WORST CASE: O(n^2)

def selection_sort_it(elements: list) -> list:
    for i in range(len(elements)):
        min_index = i
        for j in range(i+1, len(elements)):
            if elements[j] < elements[min_index]:
                min_index = j

        elements[i], elements[min_index] = elements[min_index], elements[i]

    return elements


unorded_list = selection_sort_it([73, 62, 61, 69, 10, 25, 100, 50])
print(unorded_list)
