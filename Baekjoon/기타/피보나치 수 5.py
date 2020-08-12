# https://www.acmicpc.net/problem/10870
# 재귀를 사용해보자

n = int(input())


def fibo(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibo(num-1) + fibo(num-2)


print(fibo(n))