class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "%s:%s"%(self.key,self.value)

class HashMap:
    def __init__(self, M):
        self.table = [None]*M
        self.M = M

    def hashFn(self, key):
        sum = 0
        for c in key:
            sum = sum + ord(c) #ord() : 문자를 아스키 코드 값으로 바꿔주는 함수
        #문자열의 모든 문자에 대한 ASCII 값을 더하고 테이블 크기로 나눈 나머지
        return sum % self.M

    def insert(self, key, value):
        idx = self.hashFn(key)
        #이미 단어가 존재할 경우, 실패로 판단
        if not self.search(key) == None:
            print("Failed")
            return None

        while True:
            #버킷이 비었을 경우
            if self.table[idx] == None or self.table[idx] == -1 :
                #단어 삽입
                self.table[idx] = Entry(key, value)
                #단어가 삽입이 됐음을 명시
                print(key, value, "inserted")
                return #삽입 완료 후 메소드 종료
            idx += 1
            #테이블을 한 바퀴 돌았을 경우, 실패로 판단
            if idx == self.hashFn(key) : 
                print("Failed")
                return None

    def search(self, key):
        for i in range(len(self.table)):
            #해당 버킷에 Entry가 없어서 key가 존재하지 않아서 오류가 발생하는 경우가 있음
            #이를 방지 하기위해, -1과 None을 먼저 우선확인
            if self.table[i] != -1 and self.table[i] != None and self.table[i].key == key:return self.table[i]
        return None

    def delete(self, key):
        for i in range(len(self.table)):
            #해당 버킷에 Entry가 없어서 key가 존재하지 않아서 오류가 발생하는 경우가 있음
            #이를 방지 하기위해, -1과 None을 먼저 우선확인
            #값이 존재했다가 삭제 되었다는 의미로 -1로 초기화
            if self.table[i] != -1 and self.table[i] != None and self.table[i].key == key:
                self.table[i] = -1
                return
        return None

    def display(self, msg = '단어장'):
        print(msg)
        for i in range(len(self.table)):
            if self.table[i] == None or self.table[i] == -1 : continue
            print("[%2d] ->"%i, self.table[i].key, ":", self.table[i].value)


def main() :
    h = HashMap(10)
    
    print('----insert 테스트----')
    h.insert("game","게임")
    h.insert("data","자료")
    h.insert("structure","구조")
    h.insert("sequential","선형")
    h.insert("search","조사")
    print()
    
    print('---중복insert 방지 테스트---')
    print('h.insert("game","게임")')
    h.insert("game","게임")
    print('h.insert("data","자료")')
    h.insert("data","자료")
    print('h.insert("structure","구조")')
    h.insert("structure","구조")
    print('h.insert("sequential","선형")')
    h.insert("sequential","선형")
    print('h.insert("search","조사")')
    h.insert("search","조사")
    print()
    
    print('---search 테스트---')
    print(h.search('data'))
    print(h.search('search'))
    print(h.search('structure'))
    print(h.search('game'))
    print(h.search('notepad'))
    print()
    
    print('---delete 테스트---')
    h.delete('game')
    h.delete('search')
    h.display()

if __name__ == "__main__" :
    main()