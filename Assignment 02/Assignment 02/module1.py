import copy

def check(obj, j, k):
    way = 0
    if j-1 >= 0 :
        way += int(obj[j-1][k])
    if j+1 <= 2 :
        way += int(obj[j+1][k])
    if k-1 >= 0 :
        way += int(obj[j][k-1])
    if j+1 <= 2 :
        way += int(obj[j+1][k])
    

after = [[0,0,0],[0,1,0],[0,0,0]]

for i in range(1,19):
    before = copy.deepcopy(after)
    
    for j in range(3):
        for k in range(3):
            after[j][k] = check(before,j,k)

case = sum(after[0]) + sum(after[1]) + sum(after[2])
print(case)
print(after[0][0] / case)