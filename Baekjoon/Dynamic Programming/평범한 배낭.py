# 이 문제는 아주 평범한 배낭에 관한 문제이다. 준서가 최대한 가치 있게 배낭을 싸려고 한다.
# 준서가 여행에 필요하다고 생각하는 N개의 물건이 있다.
# 각 물건은 무게 W와 가치 V를 가지는데, 해당 물건을 배낭에 넣어서 가면 준서가 V만큼 즐길 수 있다. 아직 행군을 해본 적이 없는 준서는 최대 K무게까지의 배낭만 들고 다닐 수 있다.
# 준서가 최대한 즐거운 여행을 하기 위해 배낭에 넣을 수 있는 물건들의 가치의 최댓값을 알려주자.


# w[i] : i+1번째 물품의 무게
# v[i] : i+1번째 물품의 가치
# dp[i][j] : i+1번째 물품까지 남은 무게 j의 최대 가치
# dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]] + v[i])

from sys import stdin

n, k = map(int, stdin.readline().split())

w, v = [0] * (n+1), [0] * (n+1)
for i in range(1, n+1):
    tmp = list(map(int, stdin.readline().split()))
    w[i], v[i] = tmp[0], tmp[1]

dp = [[0] * (k+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, k+1):
        if j >= w[i]:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i]] + v[i])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[-1][-1])


# knapsack문제,, 어렵다
