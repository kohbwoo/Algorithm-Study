def solution(num_String):
    count = 0
    for i in range(0,len(num_String)-1):
        if num_String[i] != num_String[i+1]:
            count += 1
    return (count+1)//2



a = input()
print(solution(a))

# print(solution("0001100"))
# print(solution("11111"))
# print(solution("0000001"))
# print(solution("11001100110011000001"))
# print(solution("11101101"))
#
#
# print(solution("0"))
# print(solution(("1")))