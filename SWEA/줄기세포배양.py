
T = int(input())
for idx in range(1, T+1):
    N, M, K = map(int, input().split())
    grid = [list(map(int, input().split())) + [0] * K for _ in range(N)] + [[0] * (M + K) for _ in range(K)]

    active = ['null'] + [[] for _ in range(10)]  # 생명력 1 ~ 10
    result = 0
    # active 채워 넣기 (좌표+생명령)
    for i in range(N):
        for j in range(M):
            if grid[i][j]:
                active[grid[i][j]].append([i, j, grid[i][j]])

    # K만큼 시간 지남
    for _ in range(K):
        for power in range(10, 0, -1):  # 생명력이 높은 순으로 번식(10->1)
            cells = active[power]
            new, old = [], []
            for i in range(len(cells)-1, -1, -1):
                cells[i][2] -= 1  # HP 감소
                y, x, HP = cells[i]
                if HP == -1:  # 활성 시작, 번식
                    for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                        ny, nx = (y + dy) % (N + K), (x + dx) % (M + K)
                        if not grid[ny][nx]:
                            grid[ny][nx] = power
                            new.append([ny, nx, power])
                if HP == - power:  # 비활성
                    old.append(i)

            for o in old:  # 비활성 셀 삭제
                cells.pop(o)
            cells += new  # 번식 셀 추가

    # 활성 셀 개수 세기
    result = 0
    for i in range(1, 11):
        result += len(active[i])

    print('#{} {}'.format(idx, result))
