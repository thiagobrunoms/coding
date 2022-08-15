def rotate(row):
    new_row = [None for i in range(len(row))]
    for i in range(len(row)):
        new_row[(i+1) % len(row)] = row[i]

    return new_row


def solution(roadRegister):
    new_road = [None for i in range(len(roadRegister))]
    i = 0
    while i < len(roadRegister):
        rotated_row = rotate(roadRegister[i])
        new_road[(i + 1) % len(roadRegister)] = rotated_row
        i += 1

    return new_road
