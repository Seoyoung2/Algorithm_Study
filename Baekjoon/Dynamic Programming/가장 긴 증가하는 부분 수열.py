# 수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.
# 예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.


# data[i] : 수열의 i+1번째 값
# D[i] : i+1번째 수열이 포함된 가장 긴 증가하는 부분 수열의 길이
from sys import stdin

t = int(stdin.readline())
data = list(map(int, stdin.readline().split()))
D = [1] * t

for i in range(t):
    for j in range(i):
        if data[i] > data[j]:
            D[i] = max(D[i], D[j]+1)

print(max(D))
