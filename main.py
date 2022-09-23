"""
2606 바이러스
 1. 아이디어
 - 2중 for map == 1 && chk == False => BFS
 - maxv를 이용하여 가장 많이 연결된 값 출력
 2. 자료구조
 - 그래프 저장: int[][]
 - 방문 체크: bool[][]
 - Queue(BFS)
 - 가장 많이 연결되어 있는 값: int

  슬슬 익숙해 지는 것 같다.
  입력 받는 부분이나 graph, chk를 문제 용도에 따라
  다르게 하는 부분만 익숙해 지면 탐색 문제를 다 풀 수 있을 것 같다.
"""
import sys
sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for i in range(n+1)]
chk = [False] * (n+1)
cnt = 0

for i in range(m):
    a, b = map(int, input().strip().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(graph, v):
    global cnt
    q = ([v])
    while q:
        n = q.pop()
        chk[n] = True

        for i in graph[n]:
            if chk[i] == False:
                chk[i] = True
                q.append(i)
                cnt += 1

bfs(graph, 1)
print(cnt)







