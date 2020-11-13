INF = 9999
def choose_vertex(dist, found) :
    min = INF
    minpos = -1
    for i in range(len(dist)) :
        if dist[i]<min and found[i]==False :
            min = dist[i]
            minpos = i
    return minpos

def dijkstra(vtx, adj, start) :
    vsize = len(vtx)
    dist = list(adj[start])
    path = [start] * vsize
    found = [False] * vsize
    found[start] = True
    dist[start] = 0

    for i in range(vsize) :
        u = choose_vertex(dist, found)
        found[u] = True

        for w in range(vsize) :
            if not found[w] :
                if dist[u] + adj[u][w] < dist[w] :
                    dist[w] = dist[u] + adj[u][w]
                    path[w] = u

    return path, dist

def printpath(path, start, i) :
    global vertex
    if i == start :
        print(vertex[start],end='')
        return
    printpath(path, start, path[i])
    print(' -> ',vertex[i],sep='',end='')

vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
weight = [[0,7,INF,INF,3,10,INF],
          [7,0,4,10,2,6,INF],
          [INF,4,0,2,INF,INF,INF],
          [INF,10,2,0,11,9,4],
          [3,2,INF,11,0,13,5],
          [10,6,INF,9,13,0,INF],
          [INF,INF,INF,4,5,INF,0]]

print("Shortest Path By Dijkstra Algorithm")
start = 0
result = dijkstra(vertex, weight, start)
print('Src->Dst      Dist    Path')
for i in range(len(vertex)) :
    if i != start :
        print("{}  ->  {}{:10d}".format(vertex[start],vertex[i],result[1][i]), end='    ')
        printpath(result[0], start, i)
        print()