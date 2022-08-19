
"""1439 뒤집기
더 쉬운 방법이 있었는데
좀 더 사람이 생각하는 방식으로 만들고 싶었다."""
S = input()

count1 = 0
count0 = 0
first_flag = 0
if(S[0] == "1"):
    count1 += 1
elif(S[0] == "0"):
    count0 += 1
for i in range(0,len(S)-1,1):
    if(S[i] != S[i+1]):
        if(first_flag == 0):
            first_flag = 1
            continue
        if(S[i] == "1"):
            count1 += 1
        elif(S[i] == "0"):
            count0 += 1

if(first_flag == 1 and count0 == 0):
    print(count1)
elif(first_flag == 1 and count1 == 0):
    print(count0)
else:
    print(count0 if count1 > count0 else count1)
