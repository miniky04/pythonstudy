def solution(num):
    answer = ""
    if num % 2 == 0:
        answer = "Even"
    elif num % 2 == 1:
        answer = "Odd"
    return answer


num2 = 3
print(solution(num2))