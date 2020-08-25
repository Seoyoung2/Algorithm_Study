# https://www.acmicpc.net/problem/1406
# a b c d

from sys import stdin

left = list(stdin.readline().rstrip())
right = []
cursor = len(left)

M = int(stdin.readline())
for _ in range(M):
    op = stdin.readline().split()
    if op[0] == 'L' and cursor != 0:
        right.append(left.pop())
        cursor -= 1
    elif op[0] == 'D' and cursor != len(left) + len(right):
        left.append(right.pop())
        cursor += 1
    elif op[0] == 'B' and cursor != 0:
        left.pop()
        cursor -= 1
    elif op[0] == 'P':
        left.append(op[1])
        cursor += 1

for ch in left + right[::-1]:
    print(ch, end="")
