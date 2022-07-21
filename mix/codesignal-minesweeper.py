
def get_my_neighbors(i, j):
    neighbors = []
    start_row = i - 1 if i > 0 else 0
    start_column = j - 1 if j > 0 else 0

    for row in range(start_row, i + 2):
        for column in range(start_column, j + 2):
            if row != i or column != j:
                neighbors.append((row, column))

    return neighbors


def solution(matrix):
    new_matrix = []
    for i in range(len(matrix)):
        new_row = []
        for j in range(len(matrix[i])):
            neighbors = get_my_neighbors(i, j)
            count = 0
            for each_neighbor in neighbors:
                neighbor_row = each_neighbor[0]
                neighbor_col = each_neighbor[1]
                if neighbor_row < len(matrix) and neighbor_col < len(matrix[i]) and matrix[neighbor_row][neighbor_col]:
                    count += 1

            new_row.append(count)

        new_matrix.append(new_row)

    return new_matrix


matrix = [[True, False, False],
          [False, True, False],
          [False, False, False]]

s = solution(matrix)
print(s)


#[(1, 0), (1, 1), (1, 2), (2, 0), (2, 2), (3, 0), (3, 1), (3, 2)]
