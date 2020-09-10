# p85, P2.5

class Bag :
    def __init__(self):
        self.bag = []

    def insert(self, a):
        self.bag.append(a)

    def remove(self, a):
        if a not in self.bag:
            print("그 물건은 가방에 없습니다.")
        else :
            self.bag.remove(a)

    def __str__(self):
        return "가방속의 물건 : {}".format(self.bag)

myBag = Bag()
myBag.insert('휴대폰')
myBag.insert('지갑')
myBag.insert('손수건')
myBag.insert('빗')
myBag.insert('자료구조')
myBag.insert('야구공')
print(myBag)

myBag.insert('빗')
myBag.remove('손수건')
myBag.remove('손수건')
print(myBag)