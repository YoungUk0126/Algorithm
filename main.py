"""
10828 스택
 1. 아이디어
 - 문자열을 비교하여 연산을 수행한다.(N만큼 반복)
 - 명령어들을 저장하는 문자열중 0~4번째 인덱스가 push라면 5번째 인덱스부터 있는
 숫자들을 읽어들여 스택에 추가한다.
 - 스택의 길이가 0이라면 스택이 빈 것으로 간주한다.(len 이용)
 - stack[-1]을 이용하여 마지막 인덱스를 출력한다.
 2. 자료구조
 - 스택을 표현할 리스트

 리스트의 내장함수들을 잘만 이용하면 되는 문제였고
 처음 봤을 때 push가 어렵겠다 생각했는데 1분도 안걸려서 알고리즘이 떠올라 뿌듯했다.
"""
import sys
input = sys.stdin.readline

n = int(input())

stack = []

for _ in range(n):
    str = input().strip()
    if str[:4] == 'push':
        stack.append(int(str[5:]))

    elif str == 'top':
        if len(stack) == 0:
            print("-1")
        else :
            print(stack[-1])

    elif str == 'pop':
        if len(stack) == 0:
            print("-1")
        else :
            print(stack.pop())
    elif str == 'size':
        print(len(stack))
    elif str == 'empty':
        if len(stack) == 0:
            print("1")
        else :
            print("0")















