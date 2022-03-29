def solution(food_times, k):
    food = -1
    for k in range(k, 0, -1):
        food = food + 1
        if food == len(food_times):
            food = 0
        if food_times[food] == 0:
            food = food + 1
        food_times[food] -= 1
        print(food_times, food)\


    if food_times[food] == 0:
        food = food + 1
    if food == len(food_times):
        food = 0

    return food + 1




    answer = 0
    return answer



print(solution([3, 1, 2],5))