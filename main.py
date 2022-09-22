
"""1926 그림
 1. 아이디어
 - 2중 For문 돌리며 값이 1이고 방문하지 않은 경우 BFS를 실행한다.
 - BFS 돌면서 그림 개수 +1, 최대값을 갱신한다.

 2. 자료구조
 - 그래프 전체 지도 : int[][]
 - 방문 : bool[][]
 - Queue(BFS)

역시나 BFS 예제로 외워야할 부분은 외우면서 진행하였다.
DFS와 마찬가지로 계속 연습하면서 내것으로 만들어야 겠다."""

import sys
input = sys.stdin.readline

n,m = map(int, input().split())

map = [list(map(int, input().split())) for _ in range(n)]
chk = [[False] * m for _ in range(n)]

dy = [0,1,0,-1]
dx = [1,0,-1,0]


def bfs(y,x):
    result = 1
    q = [(y,x)]
    #Queue에 값이 없을 때 까지
    while q:
        #Queue에 있는 값을 꺼내
        ey, ex = q.pop()
        for k in range(4):
            # 이동할 y좌표와 x좌표 값을 구해
            ny = ey + dy[k]
            nx = ex + dx[k]
            # 그림의 크기를 넘어가서는 안돼
            if 0<=ny<n and 0<=nx<m:
                # 이동 할 좌표가 1이고 방문한 적이 없다면
                if map[ny][nx] == 1 and chk[ny][nx] == False:
                    # 그림의 크기 +1 해줌
                    result += 1
                    # 방문 표시 해줌
                    chk[ny][nx] = True
                    # Queue에 현재 값을 넣어준다.
                    q.append((ny,nx))
    return result


cnt = 0
maxv = 0

for j in range(n):
    for i in range(m):
        # map에서 1이며 방문하지 않은 경우
        if map[j][i] == 1 and chk[j][i] == False:
            # 방문처리
            chk[j][i] = True
            # 그림의 개수
            cnt += 1
            # 현재 가장 큰 그림과 BFS로 지금 탐색할 그림을 비교하여
            # 둘 중에 가장 큰 값이 가장 큰 그림이 된다.
            maxv = max(maxv, bfs(j,i))

print(cnt)
print(maxv)

















