def solution(N, K):
    count = 0
    while N != 1:
        if N % K == 0:
            N = N / K
            count += 1
        else:
            N -= 1
            count += 1
    return count


print(solution(25, 5))