class Polynomial :
    def __init__(self):
        self.coef = []

    def degree(self) :
        return len(self.coef) - 1

    def display(self, msg = "f(x) = ") :
        print(msg,end='')
        chk = 0
        for i in range(len(self.coef)):
            if self.coef[i] != 0:
                if chk == 0 :
                    chk = 1
                else :
                    print(' ',end='')
                    if self.coef[i] > 0 : print('+',end='')
                if (self.degree() - i) == 1 : print(self.coef[i],'x',end='',sep='')
                elif (self.degree() - i) == 0 : print(self.coef[i],end='')
                else : 
                    if self.coef[i] == 1 : print('x^%d' % (self.degree() - i),end='',sep='')
                    elif self.coef[i] == -1 : print('-x^%d' % (self.degree() - i),end='',sep='')
                    else : print(self.coef[i],'x^%d' % (self.degree() - i),end='',sep='')
        if chk == 0 : print(0.0, end='')
        print()

    def add(self, b) :
        s = Polynomial()
        self.coef.reverse()
        b.coef.reverse()
        if len(self.coef) > len(b.coef) :
            for i in range(len(self.coef)) :
                if i not in range(len(b.coef)) : s.coef.append(self.coef[i])
                else : s.coef.append(self.coef[i] + b.coef[i])

        else :
            for i in range(len(b.coef)) :
                if i not in range(len(self.coef)) : s.coef.append(b.coef[i])
                else : s.coef.append(self.coef[i] + b.coef[i])

        self.coef.reverse()
        b.coef.reverse()
        s.coef.reverse()
        return s

    def sub(self, b) :
        s = Polynomial()
        self.coef.reverse()
        b.coef.reverse()
        if len(self.coef) > len(b.coef) :
            for i in range(len(self.coef)) :
                if i not in range(len(b.coef)) : s.coef.append(self.coef[i])
                else : s.coef.append(self.coef[i] - b.coef[i])

        else :
            for i in range(len(b.coef)) :
                if i not in range(len(self.coef)) : s.coef.append(-b.coef[i])
                else : s.coef.append(self.coef[i] - b.coef[i])

        self.coef.reverse()
        b.coef.reverse()
        s.coef.reverse()
        return s

    def mul(self, b) :
        s = Polynomial()

        s.coef = [0] * (self.degree() + b.degree() + 1)
        
        for i in range(len(self.coef)):
            for j in range(len(b.coef)):
                s.coef[i+j] += self.coef[i] * b.coef[j]

        return s

    def eval(self, x) :
        result = 0.0
        for i in range(len(self.coef)) :
            result += self.coef[i] * x ** (self.degree() - i)

        return result

    def read(self):
        deg = int(input("다항식의 최고 차수를 입력하시오 : "))
        for n in range(deg+1):
            coef = float(input("x^%d의 계수 : "% (deg - n)) )
            self.coef.append(coef)
    
    def easyread(self):
        deg = input("다항식의 각 차수를 입력하시오 : ")
        for i in deg.split():
            self.coef.append(float(i))

a = Polynomial()
b = Polynomial()
a.easyread()
b.easyread()

print('---Your input---')
a.display('A(x) = ')
b.display('B(x) = ')

print()
print('---add--- C(x) = A(x)+B(x)')
c = a.add(b)
c.display('C(x) = ')
print('C(2) =',c.eval(2))

print()
print('---subtract--- D(x) = A(x)-B(x)')
d = a.sub(b)
d.display('D(x) = ')
print('D(2) =',d.eval(2))

print()
print('---multiply--- E(x) = A(x)*B(x)')
e = a.mul(b)
e.display('E(x) = ')
print('E(2) =',e.eval(2))
