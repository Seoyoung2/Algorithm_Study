# coding=utf-8
# https://www.acmicpc.net/problem/1918

# A*(B+C) => ABC+* / (A-D)*(B+C) => AD-BC+*
# A+B*C+D*E+G => ABC*+DE*+G+
# A*(B+C*D) => ABCD*+* / A*(B*C+D) => ABC*D+*

# A+(B*C)*D*E+F => ABC*D*E*+F+

from sys import stdin

S = stdin.readline().rstrip()
stack = []
ans = ''

for ch in S:
    if 'A' <= ch <= 'Z':
        ans += ch
    elif ch == '(':
        stack.append(ch)
    elif ch == ')':
        # '('가 나올때까지 pop
        while stack[-1] != '(':
            ans += stack.pop()
        stack.pop()     # 남은 '(' 제거
    else:
        if ch == '*' or ch == '/':
            # stack에 *,/ 있으면 출력하고 push, 없으면 그냥 push
            if stack and (stack[-1] == '*' or stack[-1] == '/'):
                ans += stack.pop()
        else:       # ch == '+' or ch == '-'
            while stack and stack[-1] != '(':
                ans += stack.pop()
        stack.append(ch)

while stack:
    ans += stack.pop()

print(ans)


