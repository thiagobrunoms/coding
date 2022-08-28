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

from curses import start_color
from tabnanny import check


def solution(matrix, input):
    checked = 2
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):

            if matrix[row][column] == input[0]:
                print('row', row, 'column', column)
                if matrix[row][column+1] == input[1]:  # left-to-right
                    print('left-to-right')
                    k = 2
                    start = column + 2
                    for temp_column in range(start, start + (len(input)-2)):
                        if matrix[row][temp_column] == input[k]:
                            checked += 1
                            k += 1
                        else:
                            checked = 2
                            break

                # read top to bottom
                elif row + 1 < len(matrix) and matrix[row+1][column] == input[1]:
                    print('top to bottom')
                    k = 2
                    start = row + 2
                    for temp_row in range(start, start + (len(input)-2)):
                        if matrix[temp_row][column] == input[k]:
                            checked += 1
                            k += 1
                        else:
                            checked = 2
                            break

                # read top-right to bottom-left
                elif row + 1 < len(matrix) and matrix[row+1][column-1] == input[1]:
                    print('top-right to bottom-left')
                    k = 2
                    start_row = row + 2
                    start_column = column - 2
                    while start_row < len(input):
                        if matrix[start_row][start_column] == input[k]:
                            checked += 1
                            k += 1
                        else:
                            checked = 2
                            break

                        start_row += 1
                        start_column -= 1

                # read top-let to bottom-right
                elif row + 1 < len(matrix) and column + 1 < len(matrix[row+1]) and matrix[row+1][column+1] == input[1]:
                    print('top-let to bottom-right')
                    k = 2
                    start_row = row + 2
                    start_column = column + 2
                    end_at = start_row + 2
                    while start_row < end_at:
                        if matrix[start_row][start_column] == input[k]:
                            checked += 1
                            k += 1
                        else:
                            checked = 2
                            break

                        start_row += 1
                        start_column += 1

            elif matrix[row][column] == input[-1]:  # REVERSE ORDER
                print('found reverse')
                print('row', row, 'column', column)
                # right to left
                if column+1 < len(matrix[row]) and matrix[row][column+1] == input[-2]:
                    print('right to left')
                    k = -3
                    start_column = column + 2
                    end_column = start_column + 2
                    while start_column < end_column:
                        if matrix[row][start_column] == input[k]:
                            checked += 1
                            k -= 1
                            start_column += 1
                        else:
                            checked = 2
                            break

            if checked == len(input):
                return True

    return False


# left-to-right
# matrix = [['E', 'K', 'F', 'W', 'N', 'U', 'I'],
#           ['A', 'X', 'I', 'K', 'F', 'W', 'N'],
#           ['W', 'Q', 'E', 'Z', 'L', 'W', 'X'],
#           ['T', 'L', 'A', 'X', 'Q', 'E', 'R'],
#           ['Y', 'Z', 'X', 'E', 'Z', 'L', 'W'],
#           ['U', 'B', 'E', 'R', 'I', 'O', 'Q']]

# top to bottom
# matrix = [['E', 'K', 'F', 'W', 'N', 'U', 'I'],
#           ['A', 'X', 'X', 'K', 'F', 'W', 'N'],
#           ['W', 'Q', 'U', 'Z', 'L', 'W', 'X'],
#           ['T', 'L', 'B', 'X', 'Q', 'E', 'R'],
#           ['Y', 'Z', 'E', 'E', 'Z', 'L', 'W'],
#           ['U', 'Q', 'R', 'R', 'I', 'O', 'Q']]

# top-right to bottom-left
# matrix = [['E', 'K', 'F', 'W', 'N', 'U', 'I'],
#           ['A', 'X', 'X', 'K', 'B', 'W', 'N'],
#           ['W', 'Q', 'U', 'E', 'L', 'W', 'X'],
#           ['T', 'L', 'R', 'Y', 'Q', 'E', 'R'],
#           ['Y', 'Z', 'E', 'E', 'Z', 'L', 'W'],
#           ['U', 'Q', 'R', 'R', 'I', 'O', 'Q']]

# top-let to bottom-right
# matrix = [['E', 'K', 'X', 'E', 'B', 'U', 'I'],
#           ['A', 'U', 'R', 'X', 'B', 'W', 'N'],
#           ['E', 'Q', 'B', 'K', 'V', 'W', 'X'],
#           ['T', 'R', 'E', 'E', 'U', 'E', 'R'],
#           ['Y', 'Z', 'E', 'E', 'R', 'X', 'R'],
#           ['U', 'Q', 'R', 'R', 'I', 'O', 'Q']]

# REVERSE - right to left
# matrix = [['E', 'X', 'R', 'C', 'D', 'U', 'I'],
#           ['A', 'U', 'T', 'K', 'F', 'W', 'N'],
#           ['W', 'X', 'Y', 'J', 'L', 'X', 'P'],
#           ['R', 'E', 'F', 'H', 'K', 'E', 'S'],
#           ['Y', 'R', 'X', 'E', 'Z', 'L', 'W'],
#           ['C', 'B', 'U', 'R', 'E', 'B', 'U']]

# matrix = [['E', 'X', 'X', 'R', 'R', 'U', 'I'],
#           ['A', 'R', 'T', 'K', 'F', 'W', 'N'],
#           ['W', 'E', 'Y', 'J', 'L', 'X', 'P'],
#           ['T', 'B', 'A', 'W', 'K', 'E', 'S'],
#           ['Y', 'U', 'X', 'E', 'Z', 'L', 'W'],
#           ['C', 'B', 'U', 'R', 'I', 'O', 'Q']]

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
