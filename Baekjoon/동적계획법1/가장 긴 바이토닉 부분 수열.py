# 수열 S가 어떤 수 Sk를 기준으로 S1 < S2 < ... Sk-1 < Sk > Sk+1 > ... SN-1 > SN을 만족한다면, 그 수열을 바이토닉 수열이라고 한다.
# 예를 들어, {10, 20, 30, 25, 20}과 {10, 20, 30, 40}, {50, 40, 25, 10} 은 바이토닉 수열이지만,  {1, 2, 3, 2, 1, 2, 3, 2, 1}과 {10, 20, 30, 40, 20, 30} 은 바이토닉 수열이 아니다.
#
# 수열 A가 주어졌을 때, 그 수열의 부분 수열 중 바이토닉 수열이면서 가장 긴 수열의 길이를 구하는 프로그램을 작성하시오.


# max(up[i] + down[i] - 1)
# up[i] : i+1번째 까지의 증가하는 부분수열의 최대 길이 / down[i] : 그 반대

from sys import stdin
import operator

t = int(stdin.readline())
data = list(map(int, stdin.readline().split()))
rdata = list(reversed(data))
up = [1] * t
down = [1] * t

for i in range(t):
    for j in range(i):
        if data[i] > data[j]:
            up[i] = max(up[i], up[j]+1)
        if rdata[i] > rdata[j]:
            down[i] = max(down[i], down[j] + 1)

down.reverse()
print(max(list(map(operator.add, up, down))) - 1)


# 가장 긴 증가하는 부분 수열 문제를 가지고서 풀었다.
# 꼭짓점을 정해서 그 인덱스까지 증가하는 부분 수열과 그 인덱스부터 감소하는 부분 수열을 구했다.
