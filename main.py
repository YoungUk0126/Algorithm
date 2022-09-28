"""
9012 괄호
 1. 아이디어
 - "(" 와 ")"의 갯수가 동일하면 YES 아니면 NO
 - 한줄씩 6번 읽어와서 "(" ")" 숫자 검색
 - "("가 나오지 않았는데 ")"가 먼저 나온 경우 생각
 2. 자료구조
 - 괄호 문자열 : String []

 ")"가 "("보다 먼저 나오고 "(" ")"의 갯수는 같은 경우를
 빼고는 쉬운 문제였다.
"""
import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    cnt1 = 0
    cnt2 = 0
    str = input()
    for i in str:
        if i == '(':
            cnt1 += 1
        elif i == ')':
            cnt2 += 1
        if (cnt1 - cnt2) < 0 :
            print("NO")
            break
    if cnt1 > cnt2 :
        print("NO")
    elif cnt1 == cnt2:
        print("YES")












