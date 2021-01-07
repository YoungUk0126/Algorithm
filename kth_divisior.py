n, k = eval(input("n과k를 입력하세요(n은 1이상 10000이하, k는 1이상 n이하 : "))

while n>=10000 or n<=1 or k<=1 or k>=n :
    n, k = eval(input("입력값이 잘못됐습니다. 다시 입력해주세요 : "))

print("n은" + str(n) + "입니다.")
print("k는" + str(k) + "입니다.")

list = []

for i in range(1, n, 1):
    if int(n)%i == 0:
        list.append(i)

list.sort()

print(list[k-1])
