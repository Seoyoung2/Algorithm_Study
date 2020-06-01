# Dynamic Programming (https://programmers.co.kr/learn/courses/30/lessons/42899)

# 서울에서 경산까지 여행을 하면서 모금 활동을 하려 합니다. 여행은 서울에서 출발해 다른 도시를 정해진 순서대로 딱 한 번 방문한 후 경산으로 도착할 예정입니다.
# 도시를 이동할 때에는 도보 혹은 자전거를 이용합니다. 이때 도보 이동에 걸리는 시간, 도보 이동 시 얻을 모금액, 자전거 이동에 걸리는 시간, 자전거 이동 시 얻을 모금액이 정해져 있습니다.
# K시간 이내로 여행할 때 모을 수 있는 최대 모금액을 알아보려 합니다.

# knapsack 문제인가 :(
# dp[i][j] = i번째 도시까지 걸린시간 j에서의 최대 모금액,,,
def solution(K, travel):
    dp = [[0 for _ in range(K+1)] for _ in range(len(travel))]      #구간별로 배열 하나씩
    dp[0][travel[0][0]] = travel[0][1]
    dp[0][travel[0][2]] = travel[0][3]
    for i in range(1, len(travel)):
        t_walk, v_walk, t_bike, v_bike = travel[i]
        for j in range(K):
            if j+t_walk <= K:     #도보
                dp[i][j+t_walk] = max(dp[i][j+t_walk], dp[i-1][j]+v_walk)
            if j+t_bike <= K:     #자전거
                dp[i][j+t_bike] = max(dp[i][j+t_bike], dp[i-1][j]+v_bike)
    return max(dp[i])


# BEST ANSWER
def solution(K, travel):
    n = len(travel)
    memo = [[0 for _ in range(K+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        t_walk, v_walk, t_bike, v_bike = travel[i-1]
        for j in range(K+1):
            walk = memo[i-1][j-t_walk]+v_walk if j>=t_walk and memo[i-1][j-t_walk]!=-1 else -1
            bike = memo[i-1][j-t_bike]+v_bike if j>=t_bike and memo[i-1][j-t_bike]!=-1 else -1
            memo[i][j]=max(walk, bike)
    return memo[n][K]


# [도보 시간, 도보 모금액, 자전거 시간, 자전거 모금액]
print(solution(1650, [[500, 200, 200, 100], [800, 370, 300, 120], [700, 250, 300, 90]]))    #660
print(solution(3000, [[1000, 2000, 300, 700], [1100, 1900, 400, 900], [900, 1800, 400, 700], [1200, 2300, 500, 1200]])) #5900
print(solution(100, [[1, 1, 1, 1], [99, 1000, 1, 1], [1, 1, 1, 1]]))    #3