# 2019 카카오 개발자 겨울 인턴십

def solution(board, moves):
    answer = 0
    bucket = [0]
    for i in moves:
        for j in board:
            if j[i-1] == 0:
                continue
            else:
                if j[i-1] == bucket[-1]:
                    answer += 2
                    bucket.pop()
                else:
                    bucket.append(j[i-1])
                j[i-1] = 0
                break
    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))   #4

