# // Given a two dimensional array of letters, find a given word written in any of the 8 directions.
# // I.e.
# //
# // EXAMPLE
# // Input: UBER
# //
# // Input:
# // Z  A  X  R  N  U  I
# // A  U  I  K  F  W  N
# // W  Q  B  O  L  X  P
# // T  L  A  E  R  E  S
# // Y  Z  X  E  R  L  W
# // C  B  U  R  I  O  Q
# // Output: true

# // In this case, in the first row with the second column (arr[0][1]) we have a “U” which, in diagonal to bottom-right direction, we can find entirely “UBER”, so the output should be true. Return false if “UBER” (the input word) could not be found.

# // The possible directions are:

# // 1.- left to right (and reverted, right to left)
# // 2.- top to bottom (and reverted, bottom to top)
# // 3.- diagonal top-left to bottom-right like in the example (and reverted, bottom-right to top-left)
# // 4.- diagonal top-right to bottom-left (and reverted, bottom-left to top-right)

def horizontal_search(matrix, row, column, k, input):
    checked = 2
    start_column = column + 2
    end_column = start_column + 2
    while start_column < end_column:
        if matrix[row][start_column] == input[k]:
            checked += 1
            k = k + 1 if k > 0 else k - 1
            start_column += 1
        else:
            break

    return checked == len(input)


def vertical_search(matrix, row, column, k, input):
    checked = 2
    start_row = row + 2
    end_row = start_row + (len(input)-2)
    while start_row < end_row:
        if matrix[start_row][column] == input[k]:
            checked += 1
            k = k + 1 if k > 0 else k - 1
            start_row += 1
        else:
            break

    return checked == len(input)


def diagonal_top_right_bottom_left_search(matrix, row, column, k, input):
    checked = 2
    start_row = row + 2
    start_column = column - 2
    while start_row < len(input):
        if matrix[start_row][start_column] == input[k]:
            checked += 1
            k = k + 1 if k > 0 else k - 1
            start_row += 1
            start_column -= 1
        else:
            break

    return checked == len(input)


def diagonal_top_left_bottom_right_search(matrix, row, column, k, input):
    checked = 2
    start_row = row + 2
    start_column = column + 2
    end_at = start_row + 2
    while start_row < end_at:
        if matrix[start_row][start_column] == input[k]:
            checked += 1
            k = k + 1 if k > 0 else k - 1
            start_row += 1
            start_column += 1
        else:
            break

    return checked == len(input)


def solution(matrix, input):
    result: int = 0
    checked = 2
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):

            if matrix[row][column] == input[0] or matrix[row][column] == input[-1]:
                print('row', row, 'column', column,
                      'letter', matrix[row][column])

                # left-to-right or right-to-left
                if column + 1 < len(matrix[row]):
                    if matrix[row][column+1] == input[1]:
                        print('left-to-right')
                        result = horizontal_search(
                            matrix, row, column, 2, input)
                    elif matrix[row][column+1] == input[-2]:
                        print('right-to-left')
                        result = horizontal_search(
                            matrix, row, column, -3, input)

                # top-to-bottom or bottom-to-top
                if row + 1 < len(matrix):
                    if matrix[row+1][column] == input[1]:
                        print('top to bottom')
                        result = vertical_search(matrix, row, column, 2, input)
                    elif matrix[row+1][column] == input[-2]:
                        print('bottom to top')
                        result = vertical_search(
                            matrix, row, column, -3, input)

                # top-right to bottom-left or bottom-left to top-right
                if row + 1 < len(matrix):
                    if matrix[row+1][column-1] == input[1]:
                        print('top-right to bottom-left')
                        result = diagonal_top_right_bottom_left_search(
                            matrix, row, column, 2, input)
                    elif matrix[row+1][column-1] == input[-2]:
                        print('bottom-left to top-right')
                        result = diagonal_top_right_bottom_left_search(
                            matrix, row, column, -3, input)

                    if result:
                        return True
                # top-let to bottom-right or bottom-right to top-left
                if row + 1 < len(matrix) and column + 1 < len(matrix[row+1]):
                    if matrix[row+1][column+1] == input[1]:
                        print('top-let to bottom-right')
                        result = diagonal_top_left_bottom_right_search(
                            matrix, row, column, 2, input)
                    elif matrix[row+1][column+1] == input[-2]:
                        print('bottom-right to top-let')
                        result = diagonal_top_left_bottom_right_search(
                            matrix, row, column, -3, input)

                if result:
                    return True

    return False


# left-to-right
matrix = [['E', 'U', 'B', 'E', 'R', 'U', 'I'],
          ['A', 'X', 'I', 'K', 'F', 'W', 'N'],
          ['W', 'Q', 'E', 'Z', 'L', 'W', 'X'],
          ['T', 'L', 'A', 'X', 'Q', 'E', 'R'],
          ['Y', 'Z', 'X', 'E', 'Z', 'L', 'W'],
          ['U', 'B', 'E', 'R', 'I', 'O', 'Q']]

# right-to-left
# matrix = [['E', 'F', 'G', 'D', 'B', 'U', 'I'],
#           ['A', 'X', 'I', 'K', 'F', 'W', 'N'],
#           ['W', 'Q', 'R', 'E', 'B', 'U', 'X'],
#           ['T', 'L', 'A', 'X', 'Q', 'E', 'R'],
#           ['Y', 'Z', 'X', 'E', 'Z', 'L', 'W'],
#           ['D', 'F', 'S', 'R', 'I', 'O', 'Q']]

# top to bottom
# matrix = [['U', 'K', 'F', 'W', 'N', 'U', 'I'],
#           ['B', 'X', 'X', 'K', 'F', 'W', 'N'],
#           ['E', 'Q', 'U', 'Z', 'L', 'W', 'X'],
#           ['R', 'L', 'B', 'X', 'Q', 'E', 'R'],
#           ['Y', 'Z', 'E', 'E', 'Z', 'L', 'W'],
#           ['U', 'Q', 'R', 'R', 'I', 'O', 'Q']]

# bottom to top
# matrix = [['R', 'K', 'F', 'W', 'N', 'U', 'I'],
#           ['E', 'X', 'X', 'K', 'F', 'W', 'N'],
#           ['B', 'Q', 'U', 'Z', 'L', 'W', 'X'],
#           ['U', 'L', 'B', 'X', 'Q', 'E', 'R'],
#           ['Y', 'Z', 'E', 'E', 'Z', 'L', 'W'],
#           ['U', 'Q', 'R', 'R', 'I', 'O', 'Q']]

# top-right to bottom-left
# matrix = [['E', 'K', 'F', 'W', 'N', 'U', 'I'],
#           ['A', 'X', 'X', 'K', 'B', 'W', 'N'],
#           ['W', 'Q', 'U', 'E', 'L', 'W', 'X'],
#           ['T', 'L', 'R', 'Y', 'Q', 'E', 'R'],
#           ['Y', 'Z', 'E', 'E', 'Z', 'L', 'W'],
#           ['U', 'Q', 'R', 'R', 'I', 'O', 'Q']]

# bottom-left to top-right
# matrix = [['E', 'K', 'F', 'W', 'N', 'R', 'I'],
#           ['A', 'X', 'X', 'K', 'E', 'W', 'N'],
#           ['W', 'Q', 'U', 'B', 'L', 'W', 'X'],
#           ['T', 'L', 'U', 'Y', 'Q', 'E', 'R'],
#           ['Y', 'Z', 'E', 'E', 'Z', 'L', 'W'],
#           ['U', 'Q', 'R', 'R', 'I', 'O', 'Q']]

# top-left to bottom-right
# matrix = [['E', 'K', 'X', 'E', 'B', 'U', 'I'],
#           ['A', 'U', 'R', 'X', 'B', 'W', 'N'],
#           ['E', 'Q', 'B', 'K', 'V', 'W', 'X'],
#           ['T', 'R', 'E', 'E', 'U', 'E', 'R'],
#           ['Y', 'Z', 'E', 'E', 'R', 'X', 'R'],
#           ['U', 'Q', 'R', 'R', 'I', 'O', 'Q']]

# bottom-right to top-left
# matrix = [['E', 'K', 'X', 'E', 'B', 'U', 'I'],
#           ['A', 'R', 'R', 'X', 'B', 'W', 'N'],
#           ['E', 'Q', 'E', 'K', 'V', 'W', 'X'],
#           ['T', 'R', 'E', 'B', 'U', 'E', 'R'],
#           ['Y', 'Z', 'E', 'E', 'U', 'X', 'R'],
#           ['U', 'Q', 'R', 'R', 'I', 'O', 'Q']]


s = solution(matrix, 'UBER')
print('result', s)

# print(found_letters_at)
# checked = 1
# while len(found_letters_at) > len(input):
#     first_tuple_letter = found_letters_at[0]
#     if first_tuple_letter[0] == input[0]:
#         previous_row = first_tuple_letter[1]
#         previous_column = first_tuple_letter[2]

#         for index in range(1, len(found_letters_at)):
#             if input[index] == found_letters_at[index][0]:
#                 row = found_letters_at[index][1]
#                 column = found_letters_at[index][2]
#                 if (row == previous_row and column == previous_column + 1) or \
#                         (row == previous_row + 1 and (column == previous_column or column == previous_column + 1)):
#                     checked += 1
#                     continue
#                 else:
#                     del found_letters_at[index]
#                     break
#             else:
#                 del found_letters_at[index]
#                 break

#     # word is in reverse order?
#     elif first_tuple_letter[0] == input[-1]:
#         pass

#     else:
#         del found_letters_at[0]

#     if checked == len(input):
#         return True

# return False

# for tuple_letter in found_letters_at:
