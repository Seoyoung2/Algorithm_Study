# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRUN9KfZ8DFAUo

from sys import stdin

T = int(stdin.readline())
for t in range(T):
    N, K = map(int, stdin.readline().split())
    nums = list(stdin.readline().rstrip())
    case = set()
    for i in range(N//4):
        for j in range(0, N, N//4):
            case.add(int("".join(nums[j:j+N//4]), 16))
        nums.insert(0, nums.pop())
    ans = sorted(list(case), reverse=True)
    print("#{} {}".format(t+1, ans[K-1]))
