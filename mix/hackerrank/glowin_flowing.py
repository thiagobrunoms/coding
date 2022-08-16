import math


def fill_and_get(amount, content_in_tanks, pos, capacity):
    content_in_tanks[pos] += amount
    if content_in_tanks[pos] > capacity:
        additional = content_in_tanks[pos] - capacity
        content_in_tanks[pos] -= additional
        return additional

    return 0


def solution(k, n_tanks, capacities):
    is_full = False
    content_in_tanks = [0] * n_tanks
    last_overflows_at = 0
    all_overflows_at = 0
    time = 1/10
    k = k / 10
    remainder = 0
    while not is_full:
        for i in range(len(content_in_tanks)):
            remainder = fill_and_get(
                k + remainder, content_in_tanks, i, capacities[i])

        if content_in_tanks[n_tanks - 1] == capacities[n_tanks - 1] and last_overflows_at == 0:
            last_overflows_at = time

        is_full = True
        for i in range(len(content_in_tanks)):
            if content_in_tanks[i] < capacities[i]:
                is_full = False
                break

        if not is_full:
            time += 0.1

        all_overflows_at = time
        remainder = 0

    if last_overflows_at - int(last_overflows_at) <= 0.6:
        last_overflows_at = math.floor(last_overflows_at)
    else:
        last_overflows_at = math.ceil(last_overflows_at)

    if all_overflows_at - int(all_overflows_at) <= 0.6:
        all_overflows_at = math.floor(all_overflows_at)
    else:
        all_overflows_at = math.ceil(all_overflows_at)

    return (last_overflows_at, all_overflows_at)


# s = solution(2, 2, [4, 6])
s = solution(1, 4, [30, 3, 7, 20])
print('last overflows at', s[0])
print('all overflows at', s[1])
