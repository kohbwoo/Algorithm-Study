def solution(food_times, k):
    count = 0
    for i in range(len(food_times)):
        for j in range(0,food_times[i]):

            if k == 0:
                return food_times,k,count
            else:
                count = count + 1
                k = k - 1


    answer = 0
    return answer



print(solution([3, 1, 2],5))