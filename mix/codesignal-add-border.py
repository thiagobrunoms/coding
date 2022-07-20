def solution(picture):
    for i in range(len(picture)):
        picture[i] = "*" + picture[i] + "*"

    times = len(picture[i])
    additional_borders = "*" * times
    picture.insert(0, additional_borders)
    picture.insert(len(picture), additional_borders)

    return picture


s = solution(["abc", "ded"])
print(s)
