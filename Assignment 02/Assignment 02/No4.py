# p84, 2.16

def printNum(n):
    for i in range(n):
        print(i+1, end=' ')
    print()

def printRevNum(n):
    for i in range(n-1,-1,-1):
        print(i+1, end=' ')
    print()

printNum(15)
printRevNum(15)