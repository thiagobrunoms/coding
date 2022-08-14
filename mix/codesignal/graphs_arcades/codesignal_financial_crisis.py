
def solution(roadRegister):
    road_len = len(roadRegister)
    new_road_len = road_len - 1

    number_of_new_roads = 0
    result_list: list = []
    while number_of_new_roads < road_len:
        new_road = [[False for j in range(new_road_len)]
                    for i in range(new_road_len)]

        i = 0
        while i < new_road_len:
            j = 0
            while j < new_road_len:
                if number_of_new_roads == 0:
                    new_road[i][j] = roadRegister[i+1][j+1]
                elif number_of_new_roads == road_len - 1:
                    new_road[i][j] = roadRegister[i][j]
                else:
                    if i < number_of_new_roads:
                        if j < number_of_new_roads:
                            new_road[i][j] = roadRegister[i][j]
                        else:
                            new_road[i][j] = roadRegister[i][j+1]
                    else:
                        if j < number_of_new_roads:
                            new_road[i][j] = roadRegister[i+1][j]
                        else:
                            new_road[i][j] = roadRegister[i+1][j+1]

                j += 1

            i += 1

        result_list.append(new_road)
        number_of_new_roads += 1

    return result_list


s = solution([[False, True,  True,  False],
              [True,  False, True,  False],
              [True,  True,  False, True],
              [False, False, True,  False]])

print(s)
