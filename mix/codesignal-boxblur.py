from email.mime import image


def solution(image):
    result = []
    row = 0
    max_row = 3
    column = 0
    max_column = 3

    controller = 0
    shift_row = 0
    shift_column = 0

    new_point = []
    while max_row <= len(image):
        # print('starting')
        sum = 0

        for i in range(row, max_row):
            shift_row = i
            for j in range(column, max_column):
                # print(i, j)
                shift_column = j
                sum += image[i][j]

        new_average = sum // 9
        print('new_average', new_average)

        new_point.append(new_average)
        if shift_column < len(image[0]) - 1:
            column += 1
            row = shift_row - shift_column

            max_column += 1
            max_row = row + 3
        else:
            result.append(new_point)
            new_point = []

            row += 1
            column = 0

            max_column = column + 3
            max_row = max_row + 1

    return result


# image = [[7, 4, 0, 1], [5, 6, 2, 2], [6, 10, 7, 8], [1, 4, 2, 0]]
# image = [[1, 1, 1], [1, 7, 1], [1, 1, 1]]
# image = [[0, 18, 9], [27, 9, 0],  [81, 63, 45]]
# image = [[36, 0, 18, 9], [27, 54, 9, 0], [81, 63, 72, 45]]
image = [[36,0,18,9,9,45,27], [27,0,54,9,0,63,90], [81,63,72,45,18,27,0], [0,0,9,81,27,18,45], [45,45,27,27,90,81,72], [45,18,9,0,9,18,45], [27,81,36,63,63,72,81]]
s = solution(image)

print(s)
# def solution(image):
#     start = 0
#     end = 3
#     offset = 0
#     controller = 0

#     col_offset = 0
#     row_offset = 0

#     while controller < len(image):
#         print('restartnig col_offset=', col_offset, 'row_offset',
#               row_offset, 'start=', start, 'end=', end)
#         for i in range(start + row_offset, end - col_offset):
#             for j in range(start + col_offset, end):
#                 print(i, j)

#         if col_offset < len(image) - 3:
#             col_offset += 1
#             end += 1
#         else:
#             row_offset = 0
#             col_offset = 0
#             start += 1
#             end = 3

#         controller += 1


# s = solution([[7, 4, 0, 1],
#               [5, 6, 2, 2],
#               [6, 10, 7, 8],
#               [1, 4, 2, 0]],
#              )

# # 00 01 02       01 02 03
# # 10 11 12 ->    11 12 13
# # 20 21 22       21 22 23

# # 10 11 12     11 12 13
# # 20 21 22 -> 21 22 23
# # 30 31 32     31 32 33
