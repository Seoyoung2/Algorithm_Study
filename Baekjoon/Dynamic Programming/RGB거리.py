# RGB거리에 사는 사람들은 집을 빨강, 초록, 파랑중에 하나로 칠하려고 한다.
# 또한, 그들은 모든 이웃은 같은 색으로 칠할 수 없다는 규칙도 정했다. 집 i의 이웃은 집 i-1과 집 i+1이다.
#
# 각 집을 빨강으로 칠할 때 드는 비용, 초록으로 칠할 때 드는 비용, 파랑으로 드는 비용이 주어질 때, 모든 집을 칠할 때 드는 비용의 최솟값을 구하는 프로그램을 작성하시오.


# cost[i][j] : i+1번째 집에 j색을 칠할 때 드는 비용
from sys import stdin

t = int(stdin.readline())
cost = [[int(x) for x in stdin.readline().strip().split()] for i in range(t)]

for i in range(1, t):
    for j in range(3):
        if j == 0:
            cost[i][j] = min(cost[i - 1][j + 1], cost[i - 1][j + 2]) + cost[i][j]
        elif j == 1:
            cost[i][j] = min(cost[i - 1][j - 1], cost[i - 1][j + 1]) + cost[i][j]
        else:
            cost[i][j] = min(cost[i - 1][j - 2], cost[i - 1][j - 1]) + cost[i][j]

print(min(cost[-1]))



