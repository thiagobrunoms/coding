def solution(inputArray):
    moves = 0
    index = 1
    while index < len(inputArray):
        previous = inputArray[index - 1]
        current = inputArray[index]

        if current <= previous:
            diff = current - previous if current >= previous else previous - current
            previous_moves = moves
            moves = diff + 1
            inputArray[index] = current + moves
            moves += previous_moves

        index += 1

    return moves


# [1, 2, 3, 4] -> 0
# [4, 2, 2, 1] -> 3 + 4 + 5 = 12
# []
