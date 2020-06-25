# https://www.acmicpc.net/problem/1904
# dp[n] : 크기가 n인 이진수열, [1,2,3,5,8,...]
# dp[n] = dp[n-1] + dp[n-2]

from sys import stdin

n = int(stdin.readline())
a, b = 1, 2
ans = 0
for _ in range(n-2):
    a, b = b, (a+b) % 15746
print(b if n != 1 else 1)