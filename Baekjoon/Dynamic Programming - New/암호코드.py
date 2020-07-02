# https://www.acmicpc.net/problem/2011

from sys import stdin

secret = stdin.readline().rstrip()
l = len(secret) + 1
dp = [0] * l
dp[0] = 1
for i in range(1, l):
    if 1 <= int(secret[i-1]) <= 9:
        dp[i] += dp[i-1]
    if i == 1:
        continue
    if secret[i-2] == '1' or (secret[i-2] == '2' and 0 <= int(secret[i-1]) <= 6):
        dp[i] += dp[i-2]
print(dp[-1] % 1000000)