"""1260번 DFS와 BFS
어떤 것인지 개념은 알지만 프로그램으로 구현하기 어려웠다.
그래서 다른 사람 코드를 보면서 문제를 풀었다.
강의를 봐도 DFS의 재귀 형식은 아직도 이해하기 힘들다.
다른 유형의 문제를 풀면서 더 알아가야 겠다"""
N,M,V = map(int,input().split())

#행렬 만들기
graph = [[0]*(N+1) for _ in range(N+1)]
for i in range (M):
    a,b = map(int,input().split())
    graph[a][b] = graph[b][a] = 1

#방문 리스트 행렬
visited1 = [0]*(N+1)
visited2 = visited1.copy()

#dfs 함수 만들기
def dfs(V):
    visited1[V] = 1 #방문처리
    print(V, end=' ')
    for i in range(1, N+1):
        if graph[V][i] == 1 and visited1[i] == 0:
            dfs(i)

#bfs 함수 만들기
def bfs(V):
    queue = [V]
    visited2[V] = 1 #방문처리
    while queue:
        V = queue.pop(0) #방문 노드 제거
        print(V, end = ' ')
        for i in range(1, N+1):
            if visited2[i] == 0 and graph[V][i] == 1:
                queue.append(i)
                visited2[i] = 1 # 방문처리

dfs(V)
print()
bfs(V)














