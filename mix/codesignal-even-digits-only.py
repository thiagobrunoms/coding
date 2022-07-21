
def solution(number):
    expo = 9
    started = False
    while expo >= 0:
        algarism = (number // (10 ** expo)) % 10
        if algarism == 0 and not started:
            expo -= 1
            continue
        else:
            started = True

        if algarism % 2 != 0:
            return False

        expo -= 1
    return True


s = solution(240602)
print(s)
