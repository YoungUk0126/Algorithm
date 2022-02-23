array = [
    2,9,3,6,7,3,4
]
commands = [
    [
        1,3,1
    ],
    [
        5,6,2
    ],
    [
        1, 7, 3
    ]
]

com1 = 0
com2 = 0
com3 = 0
temp = []
answer = []

for i in range(0,len(commands)) :
    com1 = commands[i][0]
    print(com1)
    com2 = commands[i][1] 
    print(com2)
    com3 = commands[i][2] 
    print(com3)
    temp = array[com1 - 1 : com2]
    temp.sort()
    print(temp)
    answer.append(temp[com3-1])

    print(answer)