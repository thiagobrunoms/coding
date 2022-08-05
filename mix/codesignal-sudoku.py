def get_i_j_square_position(point):
    if point >= 0 and point <= 2:
        return 0
    elif point >= 3 and point <= 5:
        return 1
    else:
        return 2


def solution(grid):
    row_col_mapping = {}
    for i in range(9):
        for j in range(9):
            number_ij = grid[i][j]
            number_ji = grid[j][i]

            key_row = 'row' + str(i)
            if key_row not in row_col_mapping:
                row_col_mapping[key_row] = [number_ij]
            elif number_ij not in row_col_mapping[key_row]:
                row_col_mapping[key_row].append(number_ij)
            else:
                return False

            key_col = 'col' + str(i)
            if key_col not in row_col_mapping:
                row_col_mapping[key_col] = [number_ji]
            elif number_ji not in row_col_mapping[key_col]:
                row_col_mapping[key_col].append(number_ji)
            else:
                return False

            i_square = get_i_j_square_position(i)
            j_square = get_i_j_square_position(j)

            if (i_square, j_square) not in row_col_mapping:
                row_col_mapping[(i_square, j_square)] = [number_ij]
            elif number_ij not in row_col_mapping[(i_square, j_square)]:
                row_col_mapping[(i_square, j_square)].append(number_ij)
            elif i_square != j_square:
                return False

    return True
