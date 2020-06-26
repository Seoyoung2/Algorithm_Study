# https://www.acmicpc.net/problem/2225
# n이하의 수 k개를 더해서 n만드는 경우의 수
# n=10,k=3 -> [1,1,1,1,1,1,1,1,1,1,1]
#             [1,2,3,4,5,6,7,8,9,10,11]
#             [1,3,6,10,15,21,...]

from sys import stdin

n, k = map(int, stdin.readline().split())
dp = [1] * (n+1)
for _ in range(k-1):
    for i in range(1, n+1):
        dp[i] += dp[i-1]
        dp[i] %= 10**9
print(dp[-1])
