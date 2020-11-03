class Set:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)
    def display(self, msg):
        print(msg, self.items)

    def delete(self, elem):
        if elem in self.items:
            self.items.remove(elem)

    def insert(self, elem):
        if elem in self.items : return
        for idx in range(self.size()):
            #오름차순으로 정렬되도록 값을 리스트에 삽입
            if elem < self.items[idx]:
                self.items.insert(idx,elem)
                return

        self.items.append(elem)

    def __eq__(self, setB):
        #리스트의 크기가 다르거나 값이 하나라도 다르면 다른 집합으로 판단
        if self.size() != setB.size(): return False
        for idx in range(self.size()):
            if self.items[idx] != setB.items[idx]:
                return False

        return True

    #합집합
    def union(self, setB):
        #합집합 결과가 저장될 임시 집합
        newSet = Set()
        a, b = 0, 0
        while a < len(self.items) and b < len(setB.items):
            valueA = self.items[a]
            valueB = setB.items[b]
            #둘 중 값이 작은 쪽의 인덱스 변수를 우선으로 1씩 증가
            #작은 값부터 임시 집합에 삽입
            if valueA < valueB:
                newSet.items.append(valueA)
                a += 1 #첫 번째 인덱스 변수 1증가
            elif valueA > valueB :
                newSet.items.append(valueB)
                b += 1 #두 번째 인덱스 변수 1증가

            #같으면 하나만 임시 집합에 삽입
            else :
                newSet.items.append(valueA)
                a += 1 #두 인덱스 변수 모두 1증가
                b += 1

        #남은 집합 원소를 임시 집합에 삽입
        while a < len(self.items):
            newSet.items.append(self.items[a])
            a += 1
        while b < len(setB.items):
            newSet.items.append(self.items[b])
            b += 1

        #결과 return
        return newSet

    #교집합
    def intersect(self, setB):
        #교집합 결과가 저장될 임시 집합
        newSet = Set()
        a, b = 0, 0
        while a < self.size() and b < setB.size() :
            valueA = self.items[a]
            valueB = setB.items[b]
            #둘 중 값이 작은 쪽의 인덱스 변수를 우선으로 1씩 증가
            if valueA < valueB :
                a += 1
            elif valueA > valueB :
                b += 1
            #값이 같으면 하나만 임시 집합에 삽입
            else :
                newSet.items.append(valueA)
                a += 1
                b += 1

        #결과 return
        return newSet

    #차집합
    def difference(self, setB):
        #차집합 결과가 저장될 임시 집합
        newSet = Set()
        a, b = 0, 0
        while a < self.size() and b < setB.size() :
            valueA = self.items[a]
            valueB = setB.items[b]
            #둘 중 값이 작은 쪽의 인덱스 변수를 우선으로 1씩 증가
            #첫 번째 집합이 작을 때만 임시 집합에 삽입
            if valueA < valueB :
                newSet.items.append(valueA)
                a += 1
            elif valueA > valueB :
                b += 1
            #값이 같으면 두 인덱스 변수 모두 1씩 증가
            else :
                a += 1
                b += 1
        #남은 원소를 임시 집합에 삽입
        while a < self.size() :
            newSet.items.append(self.items[a])
            a += 1
        #결과 return
        return newSet


def main() :
    A = Set()
    B = Set()
    
    A.insert(1)
    A.insert(5)
    A.insert(3)
    A.insert(9)
    A.insert(7)
    A.display('setA :')
    
    B.insert(9)
    B.insert(5)
    B.insert(3)
    B.display('setB :')
    
    C = A.union(B)
    C.display('setA union setB :')
    
    C = A.intersect(B)
    C.display('setA intersect setB :')
    
    C = A.difference(B)
    C.display('setA difference setB :')

if __name__ == "__main__" :
    main()