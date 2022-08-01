def solution(bishop, pawn):
    bishop_column = ord(bishop[0])
    pawn_column = ord(pawn[0])
    bishop_row = int(bishop[1])
    pawn_row = int(pawn[1])

    return abs(bishop_column - pawn_column) == abs(pawn_row - bishop_row)

# def to_coords(cell):
#     col = ord(cell[0]) % 97
#     row = int(cell[1]) - 1
#     return (row, col)

# def solution(bishop, pawn):
#     bishop = to_coords(bishop)
#     pawn = to_coords(pawn)

#     i = bishop[0]
#     j = bishop[1]
#     if bishop[0] < pawn[0]:
#         while i < 8:
#             if i == pawn[0] and j == pawn[1]:
#                 return True

#             i += 1
#             if bishop[1] < pawn[1]:
#                 j += 1   #down towards right columns
#             else:
#                 j -= 1   #down towards left columns

#         return False
#     else:
#         while i >= 0:
#             if i == pawn[0] and j == pawn[1]:
#                 return True

#             i -= 1
#             if j < pawn[1]:
#                 j += 1 #up towards right columns
#             else:
#                 j -= 1 #up towards left columns

#         return False

#     return False
