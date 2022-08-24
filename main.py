"""잃어버린 괄호 1541번
-를 마지막에 해야하는 건 알았지만
뒤에 +를 아예하지 않고 그냥 전부 빼주면 된다는 생각을 떠올리기 힘들었다.
"""

data = input().split('-')
#[55, 55+40, 30+20]
result = 0
for i in data[0].split('+'):
    result += int(i)
#55
for i in data[1:]:
    for j in i.split('+'):
        result -= int(j)

print(result)
        #-40
        #-90






