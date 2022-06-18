def insertion_sorting_it(elements: list) -> list:
    for i in range(1, len(elements)):
        j = i

        while j > 0 and elements[j-1] > elements[j]:
            print('comparando ', elements[j-1], " com ", elements[j])
            temp = elements[j-1]
            elements[j-1] = elements[j]
            elements[j] = temp

            j = j - 1
        print('próximo!')

    return elements


elements = [7, 1, 2, 3, 9, 5, 1]
result = insertion_sorting_it(elements)
print(result)
