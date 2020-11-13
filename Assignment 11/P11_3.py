import heapq # heapq 모듈

parent = []
set_size = 0

# 집합을 초기화하는 함수
def init_size(nSets) :
    # 전역변수
    global set_size, parent
    set_size = nSets
    # 모든 정점에 대해 각각이 고유의 집합이 되도록
    for i in range(nSets) :
        parent.append(-1)

# 집합의 루트를 반환하는 함수
def find(id) :
    # 부모가 없는 노드, 즉, 루트를 찾을 때까지 반복
    while(parent[id] >= 0) :
        id = parent[id]
    return id

# 집합을 합치는 함수
def union(s1, s2) :
    # 전역변수
    global set_size
    # s1의 부모가 s2가 되면서 두 집합은 같은 집합이 됨
    parent[s1] = s2
    # 두 집합이 병합됐으므로 개수가 하나 줄어 듦
    set_size = set_size - 1

# kruskal의 최소 비용 신장 트리
def MSTKruskal(vertex, adj) :
    # 정점의 개수
    vsize = len(vertex)
    # 정점의 개수에 대한 집합 초기화
    init_size(vsize)
    # heapq모듈 사용을 위한 리스트 (간선 리스트)
    eList = []

    for i in range(vsize-1) :
        for j in range(i+1, vsize) :
            if adj[i][j] != None :
                # 모든 간선을 힙에 push
                heapq.heappush(eList,(adj[i][j],i,j))

    # 추가된 간선의 수
    edgeAccepted = 0
    while(edgeAccepted < vsize - 1) :
        # 가장 작은 가중치를 가진 간선
        e = heapq.heappop(eList)
        uset = find(e[1]) # 두 정점의 집합에 대한 루트 구함
        vset = find(e[2])

        # 다른 집합이라면
        if uset!=vset :
            print("간선 추가 : (%s, %s, %d)"%(vertex[e[1]], vertex[e[2]], e[0]))
            # 두 집합을 합침
            union(uset, vset)
            # 추가된 간선의 수 1 증가
            edgeAccepted += 1

if __name__ == "__main__" :
    vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    weight = [[None,29,None,None,None,10,None],
              [29,None,16,None,None,None,15],
              [None,16,None,12,None,None,None],
              [None,None,12,None,22,None,18],
              [None,None,None,22,None,27,25],
              [10,None,None,None,27,None,None],
              [None,15,None,18,25,None,None]]

    print("MST By Kruskal's Algorithm")
    MSTKruskal(vertex, weight)