# https://www.acmicpc.net/problem/11055

from sys import stdin

n = int(stdin.readline())
num = list(map(int, stdin.readline().split()))
# i번째 수 포함 : [1, 101, 3, 53, 113, 6, 11, 16, 23, 31] -> 이걸로!
# i번째 수 포함X: [1, 101, 101, 101, 101, 101, 101, 101, 101, 101]
dp = num[:]
for i in range(1, n):
    for j in range(i):
        if num[i] > num[j]:
            dp[i] = max(dp[i], dp[j]+num[i])
print(max(dp))