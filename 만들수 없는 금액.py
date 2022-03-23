def solution(n, num):
    #정렬된 리스트로 반복하며 더해나갈때 카운트보다 큰 값을 만들 수 있는지 확인하며 진행한다. 만들 수 없는순간 리턴...
    num.sort()#리스트 정렬
    count = 1
    for i in range(0, len(num)):
        if count < num[i]:
            return count
        count += num[i]



print(solution(5,[3,2,1,1,9]))#동전이 5개인걸 알아도 딱히 쓸모가 없었음..