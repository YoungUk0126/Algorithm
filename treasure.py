N = int(input())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
S = 0

for i in range(N):
    S += max(A) * min(B)
    A.pop(A.index(max(A)))
    B.pop(B.index(min(B)))

print(S)