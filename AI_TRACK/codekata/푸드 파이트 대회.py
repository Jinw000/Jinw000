def solution(food):
    answer = ''
    fooddiv2 = []
    for i in range(len(food)):
        fooddiv2.append(food[i] // 2)
        if fooddiv2[i] != 0:
            answer += str(i) * fooddiv2[i]
    answer = answer + "0" + answer[::-1]
    return answer

#1 7번줄에서 .join 함수는 불가능
