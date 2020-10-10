import queue
import copy
import time

# 10 X 10의 미로 내에서 이동가능한 노드인지 확인
def isValidPos(maze, x, y) :
    if x < 0 or y < 0 or x >= 10 or y >= 10 : return False
    else :
        return maze[x][y] == 0

# 우선순위 큐
class PriorityQueue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0
    def size(self) : return len(self.items)
    def clear(self) : self.items = []

    def enqueue(self, node):
        # f를 기준으로 내림차순으로 삽입
        # 같은 노드가 이미 있고, 더 작은 f가 존재 한다면 SKIP
        for i in range(len(self.items)):
            if node == self.items[i] and node.f > self.items[i].f : return
            if node.f > self.items[i].f :
                self.items.insert(i, node)
                return
        # for문이 끝나버렸다면 넣으려는 값보다 작은 값이
        # 없다는 뜻이므로 제일 뒤에 삽입
        self.items.append(node)
        return

    # 가장 낮은 f의 노드를 pop하여 반환
    def dequeue(self):
        return self.items.pop()

MAX_QSIZE = 50 # 최악의 경우를 대비해서 넉넉하게 50
class CircularQueue:
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.items = [None] * MAX_QSIZE
    def isEmpty(self) : return self.front == self.rear

    # 공백상태와 구분을 두기 위해 항상 하나는 비워두는 전략을 사용
    def isFull(self) : return self.front == (self.rear + 1) % MAX_QSIZE

    def clear(self) : self.front = self.rear
    def enqueue(self,item):
        if not self.isFull():
            # rear를 회전시킨다는 개념
            self.rear = (self.rear + 1) % MAX_QSIZE
            self.items[self.rear] = item

    def dequeue(self):
        if not self.isEmpty():
            # front를 회전시킨다는 개념
            self.front = (self.front + 1) % MAX_QSIZE
            return self.items[self.front]

    def peek(self):
        if not self.isEmpty():
            return self.items[(self.front + 1) % MAX_QSIZE]

class Node:
    def __init__(self, parent=None, position=None):
        # 부모 노드와 현재 위치를 저장하는 역할
        self.parent = parent
        self.position = position

        # g : 출발점으로부터 현재노드까지의 가중치
        # h : 자식노드로부터 도착지까지의 예상 거리 (heuristic)
        # f : 현재까지 이동하는데 걸린 가중치와 예상 거리를 합친 값
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

def aStar(maze, start, end):

    print('---aStar---')

    # startNode와 endNode 설정
    # 이때 부모 노드는 없다(None)고 설정
    startNode = Node(None, start)
    endNode = Node(None, end)

    # openList : 앞으로 방문할 노드들
    # closedList : 더 이상 방문할 필요없는 노드들
    openList = PriorityQueue()
    closedList = []

    # openList에 시작 노드 추가
    openList.enqueue(startNode)

    # endNode를 찾을 때까지 실행
    # 혹은 더 이상 방문할 노드가 없을 때까지 실행
    while not openList.isEmpty():

        # 현재 노드 지정
        currentNode = openList.dequeue()
        closedList.append(currentNode)

        # 현재 노드가 목적지면 현재위치를 추가하고
        # current의 부모로 이동
        # 부모노드가 None일때까지 반복
        if currentNode == endNode:
            path = []
            current = currentNode
            while current is not None:
                path.append(current.position)
                current = current.parent
            # 목적지부터 되돌아가면서 경로출력
            for i in path[::-1] :
                print(i, end = '->')
            print('미로탐색 성공')
            return

        # 인접한 상하좌우 전부
        for newPosition in [(0, -1), (0, 1), (-1, 0), (1, 0)]:

            # 노드 위치 업데이트
            nodePosition = (
                currentNode.position[0] + newPosition[0],  # X
                currentNode.position[1] + newPosition[1])  # Y
                
            # 탐색할 수 있는 노드인가 검사
            if not isValidPos(maze, nodePosition[0], nodePosition[1]) : continue

            new_node = Node(currentNode, nodePosition) # 현재 노드 정보에 대한 노드 객체 생성
            
            # 자식이 closedList에 있으면 continue
            if len([closedChild for closedChild in closedList if closedChild == new_node]) > 0:
                continue

            # 탐색하게 될 노드의 f, g, h값 업데이트
            new_node.g = currentNode.g + 1
            new_node.h = ((new_node.position[0] - endNode.position[0]) ** 2) \
                       + ((new_node.position[1] - endNode.position[1]) ** 2)            
            new_node.f = new_node.g + new_node.h
            
            # 탐색하게 될 노드 PriorityQueue에 삽입
            openList.enqueue(new_node)
    
    print('미로탐색 실패')
    return

def dfs(maze, start, end):
    # queue모듈의 LifoQueue 사용
    stack = queue.LifoQueue(maxsize=50)
    stack.put(start)
    print('---DFS---')

    # endNode를 찾을 때까지 실행
    # 혹은 더 이상 방문할 노드가 없을 때까지 실행
    while not stack.empty():
        # 현재 위지 업데이트
        current = stack.get()
        print(current, end = '->')
        x, y = current
        if(current == end):
            print('미로탐색 성공')
            return
        else :
            # 지나온 위치는 . 표시
            maze[x][y] = '.'
            # 상하좌우 인접 노드들 중 갈 수 있는 곳을 삽입
            for i, j in [[0,-1],[0,1],[-1, 0],[1,0]] :
                if isValidPos(maze, x + i, y + j): stack.put((x+i,y+j))

    print('미로탐색 실패')
    return

def bfs(maze, start, end):
    # 원형 큐 사용
    que = CircularQueue()
    que.enqueue(start)
    print('---BFS---')

    # endNode를 찾을 때까지 실행
    # 혹은 더 이상 방문할 노드가 없을 때까지 실행
    while not que.isEmpty():
        # 현재 위지 업데이트
        current = que.dequeue()
        print(current, end = '->')
        x, y = current
        if(current == end):
            print('미로탐색 성공')
            return
        else :
            # 지나온 위치는 . 표시
            maze[x][y] = '.'
            # 상하좌우 인접 노드들 중 갈 수 있는 곳을 삽입
            for i, j in [[0,-1],[0,1],[-1, 0],[1,0]] :
                if isValidPos(maze, x + i, y + j): que.enqueue((x+i,y+j))

    print('미로탐색 실패')
    return

def main():
    maze = [[1,1,1,1,1,1,1,1,1,1],
            [0,0,0,0,0,0,0,0,0,1],
            [1,0,1,1,1,1,1,1,0,1],
            [1,0,1,0,0,0,1,1,0,1],
            [1,0,1,0,1,0,0,1,0,1],
            [1,0,1,0,1,0,1,1,0,1],
            [1,0,0,0,1,0,1,1,0,1],
            [1,0,1,0,1,0,1,1,0,1],
            [1,0,1,0,1,0,0,0,0,0],
            [1,1,1,1,1,1,1,1,1,1]]
    start = (1,0)
    end = (8,9)

    dfs(copy.deepcopy(maze),start,end)
    print()
    bfs(copy.deepcopy(maze),start,end)
    print()
    aStar(maze, start, end)

if __name__ == '__main__' :
    main()