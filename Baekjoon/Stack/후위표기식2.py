# https://www.acmicpc.net/problem/1935
# +(43) -(45) *(42) /(47)

from sys import stdin

N = int(stdin.readline())
S = stdin.readline().rstrip()
nums = [int(stdin.readline()) for _ in range(N)]

stack = []
for ch in S:
    if 'A' <= ch <= 'Z':
        stack.append(nums[ord(ch)-65])
    else:
        b, a = stack.pop(), stack.pop()
        if ch == '+':
            stack.append(a+b)
        elif ch == '-':
            stack.append(a-b)
        elif ch == '*':
            stack.append(a*b)
        else:
            stack.append(float(a)/b)
print("%0.2f" % stack[0])
