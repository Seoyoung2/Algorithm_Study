# https://www.acmicpc.net/problem/11047


from sys import stdin

n, k = map(int, stdin.readline().split())
coins = []
answer = 0
for _ in range(n):
    coins.append(int(stdin.readline()))
for coin in reversed(coins):
    answer += k//coin
    k %= coin
print(answer)
