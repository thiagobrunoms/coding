
# [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

# 1 2  3  4
# 5 6  7  8
# 9 10 11 12

# a[0, 1] = 0
# a[1, 1] = 6
# a[2, 1] = 10

# if any j = 0, all i,j+1 must be 0

def solution(matrix):
    haunted_j_rooms = {}
    sum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print('trying', matrix[i][j], 'i=', i, 'j=', j)
            print('haunted rooms', haunted_j_rooms)
            if matrix[i][j] == 0:
                if j not in haunted_j_rooms:
                    haunted_j_rooms[j] = True

            elif j not in haunted_j_rooms:
                print('somando', matrix[i][j])
                sum += matrix[i][j]
                print('resuktado', sum)

    return sum


matrix = [[0, 1, 1, 2], [0, 5, 0, 0], [2, 0, 3, 3]]
s = solution(matrix)
print(s)
