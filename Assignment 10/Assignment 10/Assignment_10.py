import queue

# p10.1
def dfs(adjMat, v, visited) :
    if visited[v] == 0 :
        visited[v] = 1 # 방문한 정점 기록
        print(chr(ord('A') + v), end = ' ') # 현재 탐색하는 정점 출력
        for x in range(len(adjMat)) : # 현재 탐색하고 있는 정점과 연결된 정점들을 확인
            if adjMat[v][x] == 1 and visited[x] == 0 : # 간선이 있으면서 방문한 적 없는 정점
                dfs(adjMat,x,visited)

# p10.2
def bfs(adjMat, v):
    visited = [0 for x in range(len(adjMat))]
    search = [] # 탐색 순서를 기록하는 리스트
    q = queue.Queue() # queue모듈의 Queue클래스 활용
    q.put(v) # 시작 정점을 큐에 넣음

    while q.qsize() : # 큐에 데이터가 있는 동안 반복
        v = q.get() # 탐색할 정점 선택(q에서 제거)
        if visited[v] == 1 : continue # 이미 탐색한 정점이면 건너뛰기
        visited[v] = 1 # 방문한 정점임을 기록
        search.append(chr(ord('A') + v)) # 탐색 순서를 기록

        for x in range(len(adjMat)) :
            if adjMat[v][x] == 1 and visited[x] == 0 : # 간선이 존재하면
                q.put(x) # 그 정점을 큐에 넣음

    return search # 기록된 탐색 순서를 반환

# p10.4
def spanningTree(adjMat, v, visited) :
    if visited[v] == 0 :
        visited[v] = 1
        for x in range(len(adjMat)) :
            if adjMat[v][x] == 1 and visited[x] == 0 : 
                print("({}, {})".format(chr(ord('A') + v), chr(ord('A') + x)), end=' ') # 간선을 출력
                spanningTree(adjMat,x,visited)

# p10.6
def findBridge(adjMat):
    bridge = [] # 브리지를 기록하는 리스트
    for x in range(len(adjMat)) : # 모든 정점에 대해
        for y in range(x + 1,len(adjMat)) : # 정점의 모든 간선에 대해 (이미 앞에서 검사한 간선은 건너뛰기 위해 x+1부터 시작)
            if adjMat[x][y] == 1 : # 간선이 존재하면
                adjMat[x][y], adjMat[y][x] = 0, 0 # 간선을 없애고
                visited = bfs(adjMat, 0) # bfs를 호출하여 방문한 정점들을 반환받음
                adjMat[x][y], adjMat[y][x] = 1, 1 # 간선을 다시 되돌림
                if len(visited) != len(adjMat): # 모든 정점을 방문하지 못 했을 경우
                    bridge.append((chr(ord('A') + x), chr(ord('A') + y))) # 간선을 bridge 리스트에 추가

    return bridge


if __name__ == "__main__" :
    vertex = ['A','B','C','D','E','F','G','H']
    adjMat = [[0,1,1,0,0,0,0,0],
              [1,0,0,1,0,0,0,0],
              [1,0,0,1,1,0,0,0],
              [0,1,1,0,0,1,0,0],
              [0,0,1,0,0,0,1,1],
              [0,0,0,1,0,0,0,0],
              [0,0,0,0,1,0,0,1],
              [0,0,0,0,1,0,1,0]]

    print('---DFS Test---')
    dfs(adjMat, 0, [0 for x in range(len(vertex))])

    print('\n\n---BFS Test---')
    search = bfs(adjMat, 0)
    for x in search : print(x,end = ' ')

    print('\n\n--Spanning Tree Test---')
    spanningTree(adjMat, 0, [0 for x in range(len(vertex))])
    
    print('\n\n---Find Bridges Test---')
    bridge = findBridge(adjMat)
    print(bridge)