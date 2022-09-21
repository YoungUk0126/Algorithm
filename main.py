
"""2667번 단지번호붙이기
1. 아이디어
 - 2중 for, 값 1 && 방문X => DFS
 - DFS를 통해 찾은 값을 저장 후 정렬 해서 출력
 
2. 자료구조
 - 그래프 저장 : int[][]
 - 방문여부 : bool[][]
 - 결과값 : int[]
 
 map 만들고 visited를 만드는건 알고 있었지만
 위아래로 움직이는 값의 배열을 따로 만들어 4방향을 탐색하고
 이어지는 모든 숫자들을 탐색 후 그 값을 result 배열에 넣고
 하는 과정들을 상상하기가 어려워 유튜브 강의 영상을 참고 하였다.
 DFS,BFS는 특히나 어려운 것 같다.
"""
#이거는 습관화 하자
import sys
input = sys.stdin.readline


N = int(input())

map = [list(map(int, input().strip())) for _ in range(N)]
chk = [[False] * N for _ in range(N)]
result = []
each = 0
dy = [0,1,0,-1]
dx = [1,0,-1,0]
def dfs(y,x):
    global each
    each += 1
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if 0<=ny<N and 0<=nx<N:
            if map[ny][nx] == 1 and chk[ny][nx] == False:
                chk[ny][nx] = True
                dfs(ny, nx)


for j in range(N):
    for i in range(N):
        if map[j][i] == 1 and chk [j][i] == False:
            # 방문 체크 표시
            chk[j][i] = True
            each = 0
            dfs(j,i)
            result.append(each)
            # DFS로 크기 구하기
            # 크기를 결과 리스트에 넣기

result.sort()
print(len(result))
for i in result:
    print(i)




















