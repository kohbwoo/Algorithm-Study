def solution(num, level):
    level.sort(reverse=True)

    while True:
        count = 0
        for i in range(level[0]):
            del level[0]



            count += 1

    return level




print(solution(5, [2, 3, 1, 2, 2]))