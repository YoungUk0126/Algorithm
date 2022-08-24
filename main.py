"""잃어버린 괄호 1541번
-를 가장 마지막에 해야 한다는 대략적인 그림을 그리고 있었으나
그냥 -를 기준으로 모든 숫자들을 분리한 후 +를 하지않고
모두 -처리를 해준다는 생각을 떠올리기가 어려웠다."""

data = input().split('-')

result = 0
for i in data[0].split('+'):
    result += int(i)

for i in data[1:]:
    for j in i.split('+'):
        result -= int(j)

print(result)








