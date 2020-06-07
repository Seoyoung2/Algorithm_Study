# https://programmers.co.kr/learn/courses/30/lessons/12905


def solution(board):
    for i in range(len(board)-1):
        for j in range(len(board[i])-1):
            if board[i+1][j+1] == 1:
                board[i+1][j+1] += min(board[i][j+1], board[i][j], board[i+1][j])
    return max([n for i in range(len(board)) for n in board[i]])**2


print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))  #9
print(solution([[0,0,1,1],[1,1,1,1]]))  #4
print(solution([[0]]))  #0