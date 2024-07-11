def solution(k, score):
    answer = []
    honor_3 = []
    for i in range(len(score)):
        honor_3.append(score[i])
        if len(honor_3) == k+1:
            honor_3.remove(min(honor_3))
        answer.append(min(honor_3))
    return answer

#1 함수 입력시 변수 지정 필요없음
#2 .remove로 리스트 내 element 제거 가능
