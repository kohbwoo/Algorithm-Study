#0이 아닌경우는 무조건 곱하고 0인경우는 더하도록 생각함
def solution(num):
    answer = 0
    for i in num:
        if i == "0": #현재 위치가 0 이면 더함
            answer = answer + 0
        else:#0이 아니면
            if answer == 0: #현재 answer 가 0인경우 곱할때 0이 되지 않도록 1로 바꿈
                answer = 1
            answer = answer * int(i)#기존 answer 랑 곱해서 저장
    return answer


print(solution("02984"))
print(solution("576"))