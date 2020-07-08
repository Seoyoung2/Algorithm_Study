# https://www.acmicpc.net/problem/1931

from sys import stdin

n = int(stdin.readline())
L = []
for _ in range(n):
    L.append(tuple(map(int, stdin.readline().split())))
# 끝나는 시간이 같다면 시작시간을 기준으로 정렬하기 위해
L.sort(key=lambda x: x[0])
# 결과적으로는 끝나는 시간을 기준으로 정렬
L.sort(key=lambda x: x[1])

cnt = 1
end = L[0][1]
for time in L[1:]:
    if time[0] >= end:
        cnt += 1
        end = time[1]
print(cnt)