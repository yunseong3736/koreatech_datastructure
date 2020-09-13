# p84, 2.16

def printNum(n):
    if n == 1 :
        print(n, end = ' ')
        return
    else :
        printNum(n-1)
        print(n, end = ' ')

def printRevNum(n):
    for i in range(n-1,-1,-1):
        print(i+1, end=' ')
    print()

printNum(15)
print()
printRevNum(15)