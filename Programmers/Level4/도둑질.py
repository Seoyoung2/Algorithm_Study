# 도둑이 어느 마을을 털 계획을 하고 있습니다. 이 마을의 모든 집들은 동그랗게 배치되어 있습니다.
# 각 집들은 서로 인접한 집들과 방범장치가 연결되어 있기 때문에 인접한 두 집을 털면 경보가 울립니다.
#
# 각 집에 있는 돈이 담긴 배열 money가 주어질 때, 도둑이 훔칠 수 있는 돈의 최댓값을 return 하도록 solution 함수를 작성하세요.
#
# 제한사항 :
# 이 마을에 있는 집은 3개 이상 1,000,000개 이하입니다.
# money 배열의 각 원소는 0 이상 1,000 이하인 정수입니다.

# < dynamic programming >
# dp[n] : n번째 집까지 고려했을 때 훔칠 수 있는 돈의 최댓값
# dp[n] = max(dp[n-1], dp[n-2]+money[n]) :집들이 일자로 있을 경우
# 처음집과 마지막집이 연결되어 있다고 생각하면 1.처음집을 털고 마지막집을 안터는 경우, 2.마지막집을 털고 처음집을 안터는 경우 이렇게 두가지가 있다.


def solution(money):
    if len(money) <= 3:
        return max(money)
    start0 = [money[0], money[0], money[0] + money[2]]  #0번째 집부터 터는 경우
    start1 = [0, money[1], max(money[1], money[2])]     #1번째 집부터 터는 경우

    for i in range(3, len(money)):
        start0.append(max(start0[-1], start0[-2] + money[i]))
        start1.append(max(start1[-1], start1[-2] + money[i]))
    return max(start0[-2], start1[-1])


print(solution([1, 2, 3, 1]))               #4
print(solution([3, 3, 3, 3, 3, 3]))         #9
print(solution([3, 3, 3, 3, 3]))            #6
print(solution([3, 1, 1, 3, 1, 3, 1]))      #9