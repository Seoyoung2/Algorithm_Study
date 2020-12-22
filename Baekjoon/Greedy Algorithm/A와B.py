# https://www.acmicpc.net/problem/12904
# 앞에서부터 비교했더니 런타임에러(?) -> 뒤에서부터 비교함

S = list(input())
T = list(input())

while len(S) != len(T):
    x = T[-1]
    T.pop()
    if x == 'B':
        T.reverse()
print(1 if S == T else 0)
