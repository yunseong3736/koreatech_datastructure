int_triangle = []

n=int(input())

for i in range(n):
    input_ = input()
    line = list(map(int, input_.split(' ')))
    assert len(line) == i + 1
    int_triangle.append(line)
    
print(int_triangle[1])

import copy

triangle = copy.deepcopy(int_triangle)
root = [ [ [] for y in range(len(int_triangle[x])) ] for x in range(n) ]
print(root)
root[0][0] = [int_triangle[0][0]]
for i in range(n-1) :
    for j in range(len(int_triangle[i])) :
        if triangle[i][j] + int_triangle[i+1][j] > triangle[i+1][j] :
            triangle[i+1][j] = triangle[i][j] + int_triangle[i+1][j]
            root[i+1][j] = copy.deepcopy(root[i][j])
            root[i+1][j].append(int_triangle[i+1][j])
        if triangle[i][j] + int_triangle[i+1][j+1] > triangle[i+1][j+1] :
            triangle[i+1][j+1] = triangle[i][j] + int_triangle[i+1][j+1]
            root[i+1][j+1] = copy.deepcopy(root[i][j])
            root[i+1][j+1].append(int_triangle[i+1][j+1])

result = max(triangle[n-1])
print(result)
print(root[n-1][triangle[n-1].index(result)])
print(root)