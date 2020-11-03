num_table = [('A', 8.5), ('B', 2.1), ('C', 4.5), ('D', 3.4), ('E', 11.2), ('F', 1.8), ('G', 2.5), ('H', 3.0), ('I', 7.5), ('J', 0.2),
         ('K', 1.1), ('L', 5.5), ('M', 3.0), ('N', 6.7), ('O', 7.2), ('P', 3.2), ('Q', 0.2), ('R', 7.6), ('S', 5.7), ('T', 7.0),
         ('U', 3.6), ('V', 1.0), ('W', 0.2), ('X', 0.2), ('Y', 0.2), ('Z', 0.2)]

class MinHeap :
    def __init__ (self) :
        self.heap = []
        self.heap.append(0)

    def size(self) : return len(self.heap)-1
    def isEmpty(self) : return self.size() == 0
    def Parent(self, i) : return self.heap[i//2]
    def Left(self, i) : return self.heap[i*2]
    def Right(self, i) : return self.heap[i*2+1]

    def display(self) : print(self.heap[1:])
    
    def insert(self, n) :
        self.heap.append(n)
        i = self.size()
        while (i!=1 and n.data[1] < self.Parent(i).data[1]) :
            self.heap[i] = self.Parent(i)
            i = i//2
        self.heap[i] = n

    def delete(self) :
        parent = 1
        child = 2
        if not self.isEmpty() :
            hroot = self.heap[1]
            last = self.heap[self.size()]
            while(child <= self.size()) :
                if child < self.size() and self.Left(parent).data[1] > self.Right(parent).data[1] :
                    child += 1
                if last.data[1] <= self.heap[child].data[1] : break
                self.heap[parent] = self.heap[child]
                parent = child
                child *= 2

            self.heap[parent] = last
            self.heap.pop(-1)
            return hroot

class Node :
    def __init__(self, data, left=None, right=None) :
        self.data = data
        self.left = left
        self.right = right

def make_tree(freq) :
    heap = MinHeap()

    for n in freq :
        heap.insert(Node(n))

    for i in range(0, len(freq)-1) :
        e1 = heap.delete()
        e2 = heap.delete()
        e3 = Node((None,e1.data[1]+e2.data[1]), e1, e2)
        heap.insert(e3)

    return heap.heap[1]

class Huffman :
    # 허프만 코드 테이블 만들기
    # Encoding, Decoding
    # 위 3가지 하면 됨(이어서)

    def makeTable(self, root, code = "") :
        if root.data[0] != None :
            self.table.append((root.data[0],code))
            return
        
        if root.left != None : 
            self.makeTable(root.left, code + "1")
        if root.right != None : 
            self.makeTable(root.right, code + "0")

    def __init__(self, root) :
        self.root = root

        self.table = []
        self.makeTable(self.root)
        self.table.sort()

        self.encodedText = []
        self.decodedText = ""

    def display(self) :
        print('---Huffman Code Table---')
        print(self.table)
        print('---Encoded Text---')
        print(self.encodedText)
        print('---Decoded Text---')
        print(self.decodedText)

    def encoding(self) :
        for i in input("문장을 입력하시오(대문자로만 입력) : ") :
            if not 'A' <= i <= 'Z' :
                self.encodedText.append(i)
                continue
            self.encodedText.append(self.table[ord(i) - ord('A')][1])

    def decoding(self) :
        for i in self.encodedText :
            if not i in [x[1] for x in self.table] :
                self.decodedText += "" + i
            else :
                root = self.root
                for j in i :
                    if j == '1' : root = root.left
                    else : root = root.right
                self.decodedText += root.data[0]

huffman = Huffman(make_tree(num_table))
huffman.encoding()
huffman.decoding()
huffman.display()