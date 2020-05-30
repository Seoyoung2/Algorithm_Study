# 아래와 같이 5와 사칙연산만으로 12를 표현할 수 있습니다.
#
# 12 = 5 + 5 + (5 / 5) + (5 / 5)
# 12 = 55 / 5 + 5 / 5
# 12 = (55 + 5) / 5
#
# 5를 사용한 횟수는 각각 6,5,4 입니다. 그리고 이중 가장 작은 경우는 4입니다.
# 이처럼 숫자 N과 number가 주어질 때, N과 사칙연산만 사용해서 표현 할 수 있는 방법 중 N 사용횟수의 최솟값을 return 하도록 solution 함수를 작성하세요.
#
# 제한사항 :
# N은 1 이상 9 이하입니다.
# number는 1 이상 32,000 이하입니다.
# 수식에는 괄호와 사칙연산만 가능하며 나누기 연산에서 나머지는 무시합니다.
# 최솟값이 8보다 크면 -1을 return 합니다.

# --------------------------------------------------------------------------
# dp[n] : 숫자(1-9) n개로 만들수 있는 수들의 집합
# 5,12 => dp[1]=1(5), dp[2]=5(55, 5+5, 5-5, 5*5, 5//5)
#         dp[3]=21(555, 55+5, 55-5, 55*5, 55//5, 5+5+5, 5+5-5, (5+5)*5, (5+5)//5, ...)
# dp[4]부터는 5555, dp[3]에 dp[1] 사칙연산, dp[2]에 dp[2] 사칙연산,

def solution(N, number):
    dp = [set() for _ in range(8)]
    for idx, x in enumerate(dp, start=1):
        x.add(int(str(N) * idx))
    for i in range(1, 8):
        for j in range(i):
            for x in dp[j]:
                for y in dp[i-j-1]:
                    dp[i].add(x + y)
                    dp[i].add(x - y)
                    dp[i].add(x * y)
                    if y != 0:
                        dp[i].add(x // y)
        if number in dp[i]:
            return i+1
    return -1


print(solution(5, 12))      #4
print(solution(2, 11))      #3


# BEST
def solution_best(N, number):
    S = [{N}]
    for i in range(2, 9):
        lst = [int(str(N)*i)]
        # 사용된 숫자는 중복을 없애기 위해 전체 길이의 반까지만 확인
        for X_i in range(int(i / 2)):
            # x는 N이 (X_i+1)번 쓰인 경우
            for x in S[X_i]:
                # y는 N이 (i-X_i-1)번 쓰인 경우
                for y in S[i - X_i - 2]:
                    # x와 y를 이용했기 때문에 전체 N이 i번 쓰인 경우
                    lst.append(x + y)
                    lst.append(x - y)
                    lst.append(y - x)
                    lst.append(x * y)
                    if x != 0: lst.append(y // x)
                    if y != 0: lst.append(x // y)
        if number in set(lst):
            return i
        S.append(lst)
    return -1


print(solution_best(5, 12))      #4
print(solution_best(2, 11))      #3