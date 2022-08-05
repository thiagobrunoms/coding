def create(filename, names_dict: list):
    count = 1
    while True:
        temp_file = filename + "(" + str(count) + ")"
        if temp_file not in names_dict:
            names_dict.append(temp_file)
            break
        else:
            count += 1


def solution(names):
    names_dict = []
    for name in names:
        if name in names_dict:
            create(name, names_dict)
        else:
            names_dict.append(name)

    return names_dict


s = solution(["dd",
              "dd(1)",
              "dd(2)",
              "dd",
              "dd(1)",
              "dd(1)(2)",
              "dd(1)(1)",
              "dd",
              "dd(1)"])

print(s)
