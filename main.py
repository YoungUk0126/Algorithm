"""설탕 배달 2839번
숨겨져 있는 규칙을 찾는게 재밌었다.
근데 답은 나오는데 백준 채점에서 오답 처리가 된다.
"""
import sys
input = sys.stdin.readline

data = int(input())

tmp = 0
if(data < 3):
    print(-1)
elif(data < 5 and data % 3 != 0):
    print(-1)
else:
    if(data % 5 == 0):
        print(int(data/5))
    elif(data % 5 == 4):
        tmp = data - 9#3*3
        tmp = tmp / 5
        print(int(tmp + 3))
    elif(data % 5 == 3):
        tmp = data - 3
        tmp = tmp / 5
        print(int(tmp + 1))

    elif(data % 5 == 2):
        tmp = data - 12
        tmp = tmp / 5
        print(int(tmp + 4))
    elif(data % 5 == 1):
        tmp = data - 6
        tmp = tmp / 5
        print(int(tmp + 2))

    else:
        print(-1)




