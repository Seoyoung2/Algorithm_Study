# https://www.acmicpc.net/problem/1912

from sys import stdin

n = int(stdin.readline())
number = list(map(int, stdin.readline().split()))
dp = [number[0]]
for i in range(1, n):
    dp.append(max(number[i], dp[i-1] + number[i]))
print(max(dp))