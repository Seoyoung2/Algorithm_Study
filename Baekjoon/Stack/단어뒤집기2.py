# https://www.acmicpc.net/problem/17413

from sys import stdin

S = stdin.readline().rstrip()
ans = ""


def reverse_word(x, y):
    global ans
    words = S[x:y+1].split(" ")
    for word in words:
        ans += (word[::-1] + " ")


flag = True
start = 0
for i in range(len(S)):
    if S[i] == '<':
        reverse_word(start, i-1)
        ans = ans[:-1]
        flag = False
        start = i
    elif S[i] == '>':
        flag = True
        ans += S[start:i+1]
        start = i+1
    if flag:
        if i == len(S)-1:
            reverse_word(start, i)
print(ans)
