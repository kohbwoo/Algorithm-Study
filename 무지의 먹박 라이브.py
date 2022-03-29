def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    food = -1

    for k in range(k, 0, -1):
        food = food + 1
        if food == len(food_times):
            food = 0
        if food_times[food] == 0:
            food = food + 1
        food_times[food] -= 1

    if food_times[food] == 0:
        food = food + 1
    if food == len(food_times):
        food = 0


    for i in range(0, len(food_times)):
        if food_times[i] != 0:
            break
        if i == len(food_times)-1:
            food = -2
    return food + 1


    answer = 0
    return answer

print(solution([3, 1, 2],5))
print(solution([10, 8, 4, 10, 6, 9, 2, 7, 6, 8], 48))
print(solution([7,8,3,3,2,2,2,2,2,2,2,2], 35))#답 2
print(solution([1,1,1,1], 4))