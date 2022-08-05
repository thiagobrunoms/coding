def solution(inputArray):
    highest_product = -float('INF')

    for i in range(1, len(inputArray)):
        product = inputArray[i] * inputArray[i-1]
        if product > highest_product:
            highest_product = product

    return highest_product


s = solution([3, 6, -2, -5, 7, 3])
print(s)
