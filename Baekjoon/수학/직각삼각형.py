# https://www.acmicpc.net/problem/4153

from sys import stdin

while True:
    num = list(map(int, stdin.readline().split()))
    if sum(num) == 0:
        break
    num.sort()
    ans = (num[2]**2 == num[0]**2 + num[1]**2)
    print("right") if ans else print("wrong")