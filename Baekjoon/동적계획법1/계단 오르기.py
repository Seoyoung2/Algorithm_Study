# v[i] = i번째 계단에 쓰여 있는 점수
# score[i] : i까지 도착한 계단 오르기 게임에서 최고 점수
# score[i] = max(score[i-3]+v[i-1]+v[i], score[i-2]+v[i])

from sys import stdin

t = int(stdin.readline())
v = [0]
for _ in range(t):
    v.append(int(stdin.readline()))

score = v[0:2]
score.append(v[1] + v[2])
for i in range(3, t+1):
    score.append(max(score[i - 3] + v[i - 1] + v[i], score[i - 2] + v[i]))

print(score[-1])