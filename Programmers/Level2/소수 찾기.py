# 완전탐색 (https://programmers.co.kr/learn/courses/30/lessons/42839)

from itertools import permutations
from math import sqrt

def solution(numbers):
    temp = set()
    for j in range(len(numbers)):
        for i in permutations(numbers, j+1):
            temp.add(int("".join(i)))
    # 소수 찾기
    answer = list(temp - {0, 1})
    for num in temp:
        for i in range(2, int(sqrt(num))+1):
            if num % i == 0:
                answer.remove(num)
                break
    return len(answer)


print(solution("17"))       #3
print(solution("011"))      #2