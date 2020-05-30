# t = int(input())
#
# for i in range(0, t):
#     mylist = [1,1,1]
#     n = int(input())
#     for j in range(3, n):
#         mylist.append(mylist[j-3] + mylist[j-2])
#     print(mylist[-1])

import sys

p = [1, 1, 1, 2, 2]
for i in range(4, 101):
    p.append(p[i]+p[i-4])
for i in range(int(sys.stdin.readline())):
    print(p[int(sys.stdin.readline()) - 1])


# 파이썬에서 input() 사용은 최대한 피해야 한다. 상당한 시간 차가 난다고 한다.
# 대용량의 입력이 들어갈 것을 생각하면 ==stdin.sys.readline()==을 쓰는 것을 추천한다.
# 이 경우엔 뒤의 \n까지 같이 들어가버리니 strip() 혹은 rstrip()을 사용해주면 개행문자가 제외된 입력값을 얻을 수 있다.
# 단, 이는 공백값까지 전부 날려버리니 상황을 잘 보고 사용해야 한다.
