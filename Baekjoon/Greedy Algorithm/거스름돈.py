# https://www.acmicpc.net/problem/5585


from sys import stdin

n = 1000 - int(stdin.readline())
coins = [500, 100, 50, 10, 5, 1]
answer = 0

for coin in coins:
    while n >= coin:
        n -= coin
        answer += 1
    if n == 0:
        break

print(answer)
