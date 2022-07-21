def solution(inputArray, elemToReplace, substitutionElem):
    for i in range(len(inputArray)):
        if inputArray[i] == elemToReplace:
            inputArray[i] = substitutionElem

    return inputArray


s = solution([1, 2, 1], 1, 3)
print(s)
