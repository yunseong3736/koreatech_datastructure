class Node :
    def __init__(self, data, link):
        self.data = data
        self.link = link

class CircularLinkedQueue :
    def __init__(self) :
        self.tail = None

    def isempty(self) : return (self.tail == None)

    def clear(self) : self.tail = None

    def enqueue(self, data) :
        if self.isempty() :
            self.tail = Node(data, None)
            self.tail.link = self.tail
        else :
            node = Node(data, self.tail.link)
            self.tail.link = node
            self.tail = node

    def dequeue(self) :
        if not self.isempty() :
            data = self.tail.link.data
            if self.tail.link == self.tail :
                self.tail = None
            else :
                self.tail.link = self.tail.link.link
            return data

    def display(self) :
        print("생성된 연결 리스트 : ",end="")
        node = self.tail.link
        while True :
            print(node.data,end="")
            node = node.link
            if node == self.tail.link : 
                print()
                break
            print("->",end="")

    def sum(self) :
        n = 0
        node = self.tail.link
        while True :
            n += node.data
            node = node.link
            if node == self.tail.link : 
                break
        return n

    def search(self, data) :
        n = 0
        node = self.tail.link
        while True :
            if node.data == data : n += 1
            node = node.link
            if node == self.tail.link : 
                break
        return n

if __name__ == "__main__" :
    cq = CircularLinkedQueue()
    print("6.12")
    while True :
        n = int(input("양의 정수를 입력하세요(종료 : -1): "))
        if n == -1 : break
        cq.enqueue(n)
    while True :
        n = cq.dequeue()
        if n == None : 
            print(n)
            break
        print(n,end = "->")
    print()

    print("6.13")
    cq.clear()
    n = int(input("노드의 개수 : "))
    for i in range(n) :
        j = int(input("노드 #{} 데이터 : ".format(i+1)))
        cq.enqueue(j)
    cq.display()
    print()

    print('6.14')
    n = int(input("끝에 추가할 데이터 : "))
    cq.enqueue(n)
    cq.display()
    print()

    print('6.15')
    print('첫 번째 노드 삭제 후 연결 리스트')
    cq.dequeue()
    cq.display()
    print()

    print('6.16')
    print('연결 리스트의 데이터 합 :',cq.sum())
    print()
    

    print('6.17')
    n = int(input("탐색할 값을 입력하시오 : "))
    print('{}는 연결 리스트에서 {}번 나타납니다.'.format(n, cq.search(n)))