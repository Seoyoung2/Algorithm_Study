# 완전탐색 (https://programmers.co.kr/learn/courses/30/lessons/42842)

from math import sqrt

def solution(brown, yellow):
    sum = brown + yellow
    tmp = []
    for i in range(2, int(sqrt(sum)) + 1):
        if sum % i == 0:
            tmp.append((i, sum//i))
    for a, b in tmp:
        if a + b == (brown+4)//2 and (a-2)*(b-2) == yellow:
            return [b, a]

print(solution(10, 2))      # [4, 3]
print(solution(8, 1))       # [3, 3]
print(solution(24, 24))     # [8, 6]
