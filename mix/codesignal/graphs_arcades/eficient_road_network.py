# Once upon a time, in a kingdom far, far away, there lived a King Byteasar III. As a smart and educated ruler, he did everything in his (unlimited) power to make every single system within his kingdom efficient. The king went down in history as a great road builder: during his reign a great number of roads were built, and the road system he created was the most efficient during those dark times.

# When you started learning about Byteasar's III deeds in your history classes, a creeping doubt crawled into the back of your mind: what if the famous king wasn't so great after all? According to the most recent studies, there were n cities in Byteasar's kingdom, connected by two-way roads. You managed to get information about these roads from the university library, so now you can write a function that will determine whether the road system in Byteasar's kingdom was efficient or not.

# A road system is considered efficient if it is possible to travel from any city to any other city by traversing at most 2 roads.

# Example

# For n = 6 and

# roads = [[3, 0], [0, 4], [5, 0], [2, 1],
#           [1, 4], [2, 3], [5, 2]]
# the output should be
# solution(n, roads) = true.

# For n = 6 and

# roads = [[0, 4], [5, 0], [2, 1],
#           [1, 4], [2, 3], [5, 2]]
# the output should be
# solution(n, roads) = false.

# As you can see, it's only possible to travel from city 3 to city 4 by traversing at least 3 roads.

# Input/Output

# [execution time limit] 7 seconds (py3)

# [input] integer n

# The number of cities in the kingdom.

# Guaranteed constraints:
# 1 ≤ n ≤ 250.

# [input] array.array.integer roads

# Array of roads in the kingdom. Each road is given as a pair [cityi, cityj], where 0 ≤ cityi, cityj < n and cityi ≠ cityj. It is guaranteed that no road is given twice.

# Guaranteed constraints:
# 0 ≤ roads.length ≤ 35000,
# roads[i].length = 2,
# 0 ≤ roads[i][j] < n.

# [output] boolean

# true if the road system is efficient, false otherwise.

# == MY APPROACH ==
# First, create the whole map based on the input connections
# Second, node by node, check which node A it is directed connected to. Otherwise, look up
# for its neighbors to check if each neighbor is connected to A. Otherwise, return False
# If it is possible to reach each other node based on the set of directed connected node or base on the node each neighor is connected to, return True

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
