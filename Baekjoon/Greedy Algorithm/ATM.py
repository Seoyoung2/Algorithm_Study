# https://www.acmicpc.net/problem/11399


from sys import stdin

n = int(stdin.readline())
times = [*map(int, stdin.readline().split())]
answer = 0
temp = 0
for i in sorted(times):
    temp += i
    answer += temp
print(answer)
