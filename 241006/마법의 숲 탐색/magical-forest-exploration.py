from collections import deque

#R-행, C-열, K-정령의 수
#R, C, K = 0, 0, 0

# 숲
#MAX_L = 70
#A = [[0] * MAX_L for _ in range(MAX_L + 3)] # 실제 숲을 [3~R+2][0~C-1]로 사용하기위해 행은 3만큼의 크기를 더 갖습니다
#A = [[0] * C for _ in range(R+3)]

# 이동 (북 동 남 서)
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

#isExit = [[False] * MAX_L for _ in range(MAX_L + 3)] # 골렘의 출구인지 저장
# isExit = [[False] * C for _ in range(R + 3)] # 골렘의 출구인지 저장
# answer = 0 # 각 정령들이 도달할 수 있는 최하단 행의 총합을 저장합니다

# (y, x)가 숲의 범위 안에 있는지 확인하는 함수
def inRange(y, x):
    return 3 <= y < R+3 and 0 <= x < C

# 숲에 있는 골렘들을 모두 없앰
def resetMap():
    for i in range(R+3):
        for j in range(C):
            A[i][j] = 0
            isExit[i][j] = False

# 골렘의 중심이 y, x에 위치할 수 있는지 확인
# 북쪽에서 남쪽으로 내려와야하므로 중심이 (y, x)에 위치할 때의 범위와 (y-1, x)에 위치할 때의 범위 모두 확인해야 함
def canGo(y, x):
    # 현재 골렘이 y, x에 있을 때 좌+우+아래가 유효한 범위 내에 있는지 확인
    flag = 0 <= x-1 and x+1 < C and y+1 < R+3
    
    # 골렘의 '위쪽범위'의 공간이 모두 빈공간 (== 0)인지 확인
    # 골렘이 북 > 남으로 내려오는 형태로 위쪽 공간도 안전하게 비어있어야만 골렘이 이동할 수 있다는 조건을 반영
    flag = flag and (A[y-1][x-1]    == 0)
    flag = flag and (A[y-1][x]      == 0)
    flag = flag and (A[y-1][x+1]    == 0)

    # 골렘의 '아래범위'의 공간이 모두 빈공간 (== 0)인지 확인
    # 북 > 남으로 이동할 경우 골렘이 위치할 수 있는 현재 위치ㅏ와 그 아래쪽 범위가 모두 빈 공간인지
    flag = flag and (A[y][x-1]      == 0) 
    flag = flag and (A[y][x]        == 0)
    flag = flag and (A[y][x+1]      == 0)
    flag = flag and (A[y+1][x]      == 0)

    #골렘의 현재 위치와 그 주변, 
    # 특히 위쪽과 남쪽 방향에 있는 칸들이 모두 비어 있는지 확인하는 과정입니다. 
    # 골렘이 남쪽으로 내려오기 때문에, 위쪽 칸들도 비어 있어야 골렘이 움직일 수 있는 조건이 성립됩니다.

    return flag

# 정령 이동
# 정령이 움직일 수 있는 모든 범위를 확인하고 도달할 수 있는 최하단 행을 반환
def bfs(y, x):
    result = y
    q = deque([(y, x)])
    visit = [[False] * C for _ in range(R+3)]
    visit[y][x] = True

    while q:
        cur_y, cur_x = q.popleft()
        # cur_y, cur_x > 골렘 내부의 정령 위치 + 정령의 중앙
        for k in range(4):
            ny, nx = cur_y + dy[k], cur_x + dx[k]
            # cur_y, cur_x위치에 정령이 있고
            # 정령의 중앙의 dy, dx (북동남서) > ny, nx는 골렘의 구역

            # 정령의 움직임은 골렘의 내부이거나
            # 골렘의 탈출구에 위치하고 있다면 다른 골렘으로 올겨 갈 수 있음
            if inRange(ny, nx) and not visit[ny][nx] and (A[ny][nx] == A[cur_y][cur_x] or (A[ny][nx] != 0 and isExit[cur_y][cur_x])):
                # inRange(ny, nx) - 정령이 움직일 공간(골렘의 내부)이 숲의 유효범위 안에 있는지 확인
                # not visit[ny][nx] - 각 위치를 방문했는지 확인 > bfs (이미 방문한 좌표는 다시 방문할 필요가 없음)
            
                # A[ny][nx] == A[cur_y][cur_x] - 같은 골렘이 놓인 곳에서만 움직일 수 있음 (A[][] = id > 골렘의 id값이 들어가 있음)
                # OR
                # A[ny][nx] != 0 - 0이 아니라는 건 > 해당 위치 (= 정령이 이동한 위치)에 어떠한 골렘이 있다는 의미
                # isExit[cur_y][cur_x] > 해당 위치 (= 정령이 이동한 위치)에 어떠한 골렘의 출구가 있다는 의미
                q.append((ny, nx))
                visit[ny][nx] = True
                result = max(result, ny)

    return result

# 골렘 이동
# 골렘id가 중심 (y, x), 출구의 방향이 d일때 규칙에 따라 움직임을 취하는 함수
# 1. 남쪽으로 한칸 이동
# 2. (1)이 안되는 경우 > 서쪽방향으로 회전하면서 내려간다
# 3. (2)가 안되는 경우 > 동쪽방향으로 회전하면서 내려간다
def down(y, x, d, id):
    
    # 아래로 내려갈 수 있는 경우 
    if canGo(y+1, x):
        down(y+1, x, d, id)

    # 왼쪽 아래로 내려갈 수 있는 경우
    elif canGo(y+1, x-1):
        down(y+1, x-1, (d+3)%4, id)

    # 오른쪽 아래로 내려갈 수 있는 경우
    elif canGo(y+1, x+1):
        down(y+1, x+1, (d+1)%4, id)

    else:
        # 1, 2, 3의 움직임을 모두 취할 수 없을 때
        if not inRange(y-1, x-1) or not inRange(y+1, x+1):
            # 숲을 벗어나는 경우 모든 골렘이 숲을 빠져나간다
            resetMap()
        else:
            # 골렘이 숲 안에 정착
            A[y][x] = id
            for k in range(4):
                A[y+dy[k]][x+dx[k]] = id
            
            # 골렘의 출구를 기록
            isExit[y+dy[d]][x+dx[d]] = True

            global answer
            # bfs를 통해 정령이 최대로 내려갈 수 있는 행을 계산하여 누적
            answer += bfs(y, x) - 3 + 1

def main():
    global R, C, K  
    #R-행, C-열, K-정령의 수
    R, C, K = map(int, input().split())

    global A
    A = [[0] * C for _ in range(R+3)]

    global isExit, answer
    isExit = [[False] * C for _ in range(R + 3)] # 골렘의 출구인지 저장
    answer = 0 # 각 정령들이 도달할 수 있는 최하단 행의 총합을 저장합니다

    for id in range(1, K+1): # 골렘번호 id
        x, d = map(int, input().split()) # 골렘의 출발 x좌표, 방향 d를 입력

        down(0, x-1, d, id)

    print(answer)

if __name__ == "__main__":
    main()