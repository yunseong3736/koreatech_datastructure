class Node: # 단순연결리스트를 위한 노드 클래스
    def __init__(self, elem, link = None): # 생성자. 디폴트 인수 사용
        self.data = elem # 데이터 멤버 생성 및 초기화
        self.link = link

class LinkedList:
    def __init__(self):
        self.head = None

    # 연결리스트 초기화
    def clear(self):
        self.head = None

    # 연결리스트의 크기
    def size(self):
        node = self.head
        count = 0
        while not node == None:
            node = node.link
            count += 1
        return count

    # pos번째의 노드를 반환
    def getNode(self, pos) :
        if pos < 0 : return None
        node = self.head;
        while pos > 0 and node != None :
            node = node.link
            pos -= 1
        return node

    # pos번째에 노드를 생성하는 함수
    def insert(self, pos, elem):
        # 바로 앞의 노드를 찾음
        before = self.getNode(pos-1)
        # 맨 앞에 삽입하는 경우
        if before == None :
            self.head = Node(elem, self.head)
        # 중간에 삽입하는 경우
        else :
            node = Node(elem, before.link)
            before.link = node

class Term:
    def __init__(self, expo, coef) :
        self.expo = expo # 항의 차수
        self.coef = coef # 항의 계수

class SparsePoly(LinkedList) : # 희소 다항식 클래스
    # 부모 클래스의 생성자 호출
    def __init__(self) :
        super().__init__()

    # 희소 다항식 입력 함수
    def read(self) :
        self.clear()
        token = input("입력(계수 차수 계수 차수 ... [Enter] : ").split(' ')
        token2 = []
        for i in range(len(token)//2) :
            token2.append((float(token[i*2]),int(token[i*2+1])))
        # 차수를 기준으로 내림차순 정렬
        token2 = sorted(token2, key = lambda x : x[1])
        token2.reverse()
        
        # LinkedList의 노드 생성
        for i in range(len(token2)) :
            self.insert(self.size(), Term(int(token2[i][1]), float(token2[i][0])))

    # 희소 다항식 출력 함수
    def display(self, msg = "f(x) = "):
        node = self.head
        while not node == None:
            # 상수항 처리
            if not node.data.expo == 0 : msg += "{:.2f} x^{} ".format(node.data.coef, node.data.expo)
            else : msg += "{:.2f}".format(node.data.coef)
            # 음수에 대한 부호 처리
            if not node.link == None and not node.link.data.coef < 0:
                msg += "+"
            node = node.link
        print("\t", msg)

    # 희소 다항식의 음수 처리
    def neg (self) :
        c = SparsePoly()
        a = self.head
        while not a == None :
            c.insert(c.size(), Term(a.data.expo, -a.data.coef))
            a = a.link

        return c

    def add(self, obj):
        c = SparsePoly()
        a = self.head
        b = obj.head
        # 희소 다항식의 길이가 같은 부분까지 반복
        while not a == None and not b == None :
            if(a.data.expo == b.data.expo) :
                if a.data.coef + b.data.coef != 0 : c.insert(c.size(), Term(a.data.expo, a.data.coef + b.data.coef))
                a, b = a.link, b.link
            elif(a.data.expo > b.data.expo) :
                c.insert(c.size(), Term(a.data.expo, a.data.coef))
                a = a.link
            else :
                c.insert(c.size(), Term(b.data.expo, b.data.coef))
                b = b.link

        # 희소 다항식의 길이가 다를 경우를 처리
        while not a == None :
            c.insert(c.size(), Term(a.data.expo, a.data.coef))
            a = a.link
        while not b == None :
            c.insert(c.size(), Term(b.data.expo, b.data.coef))
            b = b.link

        return c

    # 음수를 붙인 희소 다항식을 더한다는 개념 적용
    def sub(self, obj) : return self.add(obj.neg())

    # 2중 반복을 통해 곱하기를 구현
    def mul(self, obj) :
        c = SparsePoly()
        a = self.head
        b = obj.head
        while not a == None :
            while not b == None :
                # 임시 희소 다항식 객체
                t = SparsePoly()
                # 차수끼리는 더하고 계수끼리는 곱한다는 수학개념 적용
                t.insert(t.size(), Term(a.data.expo + b.data.expo, a.data.coef * b.data.coef))
                # 결과로 반환할 희소 다항식 객체에 임시 객체를 더함
                c = c.add(t)
                b = b.link
            a = a.link
            # 두 번째 희소 다항식은 다시 처음부터 탐색
            b = obj.head

        return c

# 테스트하는 함수
def main() :
    A = SparsePoly()
    B = SparsePoly()

    # 두 희소 다항식의 입력 테스트
    A.read()
    B.read()

    # 두 희소 다항식의 출력 테스트
    A.display("A = ")
    B.display("B = ")

    # 두 희소 다항식에 대한 덧셈, 뺄셈, 곱셈 및 출력 테스트
    A.add(B).display("A+B = ")
    A.sub(B).display("A-B = ")
    A.mul(B).display("A*B = ")

if __name__ == '__main__' :
    # 이 파일이 메인으로 실행되면 main() 함수 호출
    main()