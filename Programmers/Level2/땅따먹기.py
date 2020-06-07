# https://programmers.co.kr/learn/courses/30/lessons/12913

# dp문제
# dp[i][0] = max(dp[i+1][1],dp[i+1][2],dp[i+1][3]) + land[i][0]


def solution(land):
    for i in range(1, len(land)):
        for j in range(4):
            land[i][j] += max(land[i-1][0:j] + land[i-1][j+1:])
    return max(land[-1])


print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))        #16
