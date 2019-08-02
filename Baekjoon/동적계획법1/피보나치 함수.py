# N이 주어졌을 때, fibonacci(N)을 호출했을 때, 0과 1이 각각 몇 번 출력되는지 구하는 프로그램을 작성하시오.

from sys import stdin
import operator

t = int(stdin.readline())

data = [[1, 0], [0, 1]]
for i in range(2, 41):
    data.append(list(map(operator.add, data[i-2], data[i-1])))

for _ in range(t):
    n = int(stdin.readline())
    print(*data[n])
