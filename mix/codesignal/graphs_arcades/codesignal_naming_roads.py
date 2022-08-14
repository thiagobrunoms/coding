def find_neigbors_and_names(roads, node, row):
    result = []
    for i in range(len(roads)):
        if roads[i] != row:
            if roads[i][0] == node:
                result.append((roads[i][1], roads[i][2]))
            elif roads[i][1] == node:
                result.append((roads[i][0], roads[i][2]))

    return result


def solution(roads):
    visited_nodes = set()
    for i in range(len(roads)):
        node1 = roads[i][0]
        if node1 not in visited_nodes:
            name = roads[i][2]
            node1_neigbors_and_names = find_neigbors_and_names(
                roads, node1, roads[i])

            if len(node1_neigbors_and_names) > 0:
                for each_neigbor in node1_neigbors_and_names:
                    if abs(name - each_neigbor[1]) == 1:
                        return False

            visited_nodes.add(node1)

    return True


input = [
    [
        11,
        4,
        30
    ],
    [
        11,
        13,
        13
    ],
    [
        2,
        6,
        47
    ],
    [
        14,
        13,
        15
    ],
    [
        13,
        1,
        25
    ],
    [
        6,
        12,
        19
    ],
    [
        7,
        0,
        29
    ],
    [
        11,
        1,
        43
    ],
    [
        13,
        4,
        45
    ],
    [
        1,
        10,
        40
    ],
    [
        2,
        1,
        0
    ],
    [
        7,
        5,
        42
    ],
    [
        9,
        4,
        10
    ],
    [
        11,
        9,
        4
    ],
    [
        8,
        9,
        44
    ],
    [
        3,
        11,
        11
    ],
    [
        3,
        9,
        14
    ],
    [
        11,
        2,
        34
    ],
    [
        8,
        4,
        9
    ],
    [
        1,
        0,
        5
    ],
    [
        0,
        4,
        3
    ],
    [
        6,
        4,
        20
    ],
    [
        7,
        2,
        12
    ],
    [
        10,
        6,
        46
    ],
    [
        8,
        0,
        8
    ],
    [
        10,
        4,
        17
    ],
    [
        11,
        5,
        38
    ],
    [
        14,
        0,
        37
    ],
    [
        0,
        5,
        21
    ],
    [
        7,
        3,
        39
    ],
    [
        14,
        8,
        24
    ],
    [
        0,
        3,
        26
    ],
    [
        5,
        10,
        48
    ],
    [
        14,
        11,
        27
    ],
    [
        12,
        5,
        22
    ],
    [
        12,
        2,
        23
    ],
    [
        6,
        8,
        1
    ],
    [
        3,
        13,
        33
    ],
    [
        14,
        5,
        36
    ],
    [
        14,
        3,
        6
    ],
    [
        1,
        14,
        41
    ],
    [
        10,
        9,
        28
    ],
    [
        4,
        5,
        32
    ],
    [
        11,
        0,
        7
    ],
    [
        7,
        12,
        2
    ],
    [
        4,
        12,
        18
    ],
    [
        5,
        8,
        31
    ],
    [
        10,
        14,
        35
    ],
    [
        8,
        1,
        16
    ]
]

s = solution(input)
print(s)
