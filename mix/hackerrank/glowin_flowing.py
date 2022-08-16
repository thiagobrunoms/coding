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
    time = 1
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

        time += 1
        all_overflows_at = time
        remainder = 0

    return (last_overflows_at, all_overflows_at - 1)


s = solution(1, 4, [30, 3, 7, 20])
print('last overflows at', s[0])
print('all overflows at', s[1])
