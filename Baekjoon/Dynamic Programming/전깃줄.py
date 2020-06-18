# D[i] : i+1번째 전깃줄까지 생각했을 때, 없애야 하는 전깃줄의 최소 개수
# 각 전봇대로 tuple을 만들어서 정렬을 한 후, 남은 값으로 LIS를 적용하였다.


from sys import stdin

t = int(stdin.readline())
data = []
D = [0] * t
for _ in range(t):
    data.append(tuple(map(int, stdin.readline().split())))
data.sort()

for i in range(t):
    for j in range(i):
        if data[i][1] > data[j][1]:
            D[i] = max(D[i], D[j] + 1)

print(t - max(D) - 1)
