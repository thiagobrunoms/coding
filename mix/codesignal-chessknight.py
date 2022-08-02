# ij -> (i-1, j-2), (i-2, j-1), (i-1, j+2), (i-2, j+1), (i+1, j+2), (i+2, j+1), (i+2, j-1), (i+1, j-2)

def from_cell_to_coords(cell):
    row = ord(cell[0]) % 97
    column = int(cell[1]) - 1

    return (row, column)


def solution(cell):
    knight_positions = [(-1, -2), (-2, -1), (-1, 2),
                        (-2, 1), (1, 2), (2, 1), (2, -1), (1, -2)]
    current_position = from_cell_to_coords(cell)

    possible_positions = 0
    for position in knight_positions:
        possible_position = (
            current_position[0] + position[0], current_position[1] + position[1])
        if (possible_position[0] >= 0 and possible_position[0] < 8 and possible_position[1] >= 0 and possible_position[1] < 8):
            possible_positions += 1

    return possible_positions
