N,K = map(int, input().split())
list = [ int(input()) for x in range(0,N)]
result = 0
for i in range(N-1, -1 ,-1):
    if K == 0:
        break
    if list[i] > K:
        continue
    result += K // list[i]
    K = K % list[i]

print(result)