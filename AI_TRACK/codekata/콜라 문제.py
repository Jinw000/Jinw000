def solution(a, b, n):
    answer = 0
    temp = 0
    while n >= a:
        temp = (n//a * b)
        answer += temp
        n = (n % a) + temp
    return answer
