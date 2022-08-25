"""1085 직사각형에서 탈출
직사각형의 왼쪽 꼭지점 좌표는 항상 0,0이니
x나 y가 직사각형의 가로 세로 길이보다 0에더 가깝다면 x나 y를 출력
그렇지 않다면 x에서 가로까지의 길이 y에서 세로까지의 길이를 출력하도록 하였다"""
x,y,w,h = map(int, input().split())
row = w - x
height = h - y

b_row=0
b_height=0

if(x<row):
    b_row = x
else:
    b_row = row

if(y<height):
    b_height=y
else:
    b_height=height

if(b_row<b_height):
    print(b_row)
else:
    print(b_height)










