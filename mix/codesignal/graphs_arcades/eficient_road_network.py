def solution(n, roads):
    map = [[False for j in range(n)] for i in range(n)]
    neibors = {}
    for i in range(len(roads)):
        for j in range(len(roads[i]) - 1):
            row = roads[i][j]
            col = roads[i][j+1]
            map[row][col] = True
            map[col][row] = True

            if row not in neibors:
                new_set = set()
                new_set.add(col)
                neibors[row] = new_set

                if col not in neibors:
                    new_set = set()
                    new_set.add(row)
                    neibors[col] = new_set
                else:
                    neibors[col].add(row)

            else:
                neibors[row].add(col)
                if col not in neibors:
                    new_set = set()
                    new_set.add(row)
                    neibors[col] = new_set
                else:
                    neibors[col].add(row)

    for i in range(n):
        visited_cities = set()
        visited_cities.add(i)

        for j in range(n):
            if i != j:
                if map[i][j]:
                    visited_cities.add(j)
                else:
                    if i in neibors:
                        i_neibors = neibors[i]
                        for i_neibor in i_neibors:
                            if j in neibors[i_neibor]:
                                visited_cities.add(j)

        if len(visited_cities) != n:
            return False

    return True


s = solution(12, [[8, 9],
                  [0, 11],
                  [5, 3],
                  [11, 6],
                  [5, 7],
                  [7, 6],
                  [6, 4],
                  [10, 8],
                  [11, 2],
                  [1, 9],
                  [7, 3],
                  [7, 8],
                  [11, 8],
                  [1, 11],
                  [4, 9],
                  [6, 2],
                  [4, 3],
                  [3, 2],
                  [0, 7],
                  [10, 4],
                  [10, 0]])

print('result', s)

# map = [[False, False, False, True, True, True],
#        [False, False, True, False, True, False],
#        [False, True, False, True, False, True],
#        [True, False, True, False, False, False],
#        [True, True, False, False, False, False],
#        [True, False, True, False, False, False]
#        ]
# for i in range(n):
#     for j in range(n):
#         if i != j:
#             if not map[i][j]:

# print(visited_cities)


# x x x v v x
# x x v x v x
# x v x v x v
# v x v x x x
# v v x x x x
# v x v x x x

# 0, 4, 5, 1, 2, 3,
