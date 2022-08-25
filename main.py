"""1247번 부호
별로 좋은 문제는 아닌 것 같다.
입력받는 것에 시간이 오래 걸려 sys.stdin같은 이상한 함수를 써서
입력을 받아야한다.
다만 입력을 한 번에 여러줄을 넣더라도
입력을 세줄씩 따로 받아 처리하고
열 줄씩 따로 받아 처리하고 이런 식으로 동작할 수 있다는 것을 알게 되었다."""
import sys

for i in range(3):
    N = int(sys.stdin.readline().strip())
    data = 0
    for i in range(N):
        data += int(sys.stdin.readline().strip())
    if(data == 0):
        print('0')
    elif(data > 0):
        print('+')
    else:
        print('-')










