def solution(obstacles: list):
    obstacles.sort()
    a = 0
    temp = 0
    print(obstacles)
    while temp <= obstacles[-1]:
        temp = temp + 1
        a = temp
        print('new temp', temp)
        while a not in obstacles and a <= obstacles[-1] + 1:
            print('init para temp', temp, 'a = ', a)
            a = a + temp
            print('after para temp', temp, 'a = ', a)

        if a > obstacles[-1]:
            return temp


s = solution([2, 3])
print(s)
