class TNode:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

table = [('ㄱ','.-..'),('ㄴ','..-.'),('ㄷ','-...'),('ㄹ','...-'),
         ('ㅁ','--'),('ㅂ','.--'),('ㅅ','--.'),('ㅇ','-.-'),
         ('ㅈ','.--.'),('ㅊ','-.-.'),('ㅋ','-..-'),('ㅌ','--..'),
         ('ㅍ','---'),('ㅎ','.---'),('ㅏ','.'),('ㅑ','..'),
         ('ㅓ','-'),('ㅕ','...'),('ㅗ','.-'),('ㅛ','-.'),
         ('ㅜ','....'),('ㅠ','.-.'),('ㅡ','-..'),('ㅣ','..-'),
         ('ㅔ','-.--'),('ㅐ','--.-'),(' ','-------'),
         ('1','.----'),('2','..---'),('3','...--'),('4','....-'),('5','.....'),
         ('6','-....'),('7','--...'),('8','---..'),('9','----.'),('0','-----'),
         ('/','-..-.'),('?','..--..'),(',','--..--'),('.','.-.-.-'),]

def make_morse_tree():
    root = TNode(None,None,None)
    for tp in table :
        code = tp[1]
        node = root
        for c in code :
            if c == '.' :
                if node.left == None :
                    node.left = TNode(None,None,None)
                node = node.left
            elif c == '-' :
                if node.right == None :
                    node.right = TNode(None,None,None)
                node = node.right

        node.data = tp[0]
    return root

def decode(root, code):
    node = root
    for c in code:
        if c == '.' : node = node.left
        elif c == '-' : node = node.right
    return node.data

def encode(ch):
    for idx in table:
        if idx[0] == ch :
            return idx[1]
    return ""

# 초성 리스트. 00 ~ 18
CHOSUNG_LIST = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

# 중성 리스트. 00 ~ 20
JUNGSUNG_LIST = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']

# 종성 리스트. 00 ~ 27 + 1(1개 없음)
JONGSUNG_LIST = [' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

def divide(korean_word):
    r_lst = []
    for w in list(korean_word.strip()):
        if '가'<=w<='힣':
            # 588개 마다 초성이 바뀜. 
            ch1 = (ord(w) - ord('가'))//588
            # 중성은 총 28가지 종류
            ch2 = ((ord(w) - ord('가')) - (588*ch1)) // 28
            # 종성은 다 처리한 나머지 값
            ch3 = (ord(w) - ord('가')) - (588*ch1) - 28*ch2

            #초성
            #쌍자음 처리(ㄲ,ㄸ,ㅃ,ㅆ,ㅉ)
            if ch1 == 1 or ch1 == 4 or ch1 == 8 or ch1 == 10 or ch1 == 13 :
                r_lst.append(CHOSUNG_LIST[ch1-1])
                r_lst.append(CHOSUNG_LIST[ch1-1])
            else : r_lst.append(CHOSUNG_LIST[ch1])

            #중성
            #이중모음 처리(ㅒ,ㅖ,ㅘ,ㅙ,ㅚ,ㅝ,ㅞ,ㅟ,ㅢ)
            if ch2 == 3 : r_lst.append(JUNGSUNG_LIST[2]);r_lst.append(JUNGSUNG_LIST[20])
            elif ch2 == 7 : r_lst.append(JUNGSUNG_LIST[6]);r_lst.append(JUNGSUNG_LIST[20])
            elif ch2 == 9 : r_lst.append(JUNGSUNG_LIST[8]);r_lst.append(JUNGSUNG_LIST[0])
            elif ch2 == 10 : r_lst.append(JUNGSUNG_LIST[8]);r_lst.append(JUNGSUNG_LIST[1])
            elif ch2 == 11 : r_lst.append(JUNGSUNG_LIST[8]);r_lst.append(JUNGSUNG_LIST[20])
            elif ch2 == 14 : r_lst.append(JUNGSUNG_LIST[13]);r_lst.append(JUNGSUNG_LIST[4])
            elif ch2 == 15 : r_lst.append(JUNGSUNG_LIST[13]);r_lst.append(JUNGSUNG_LIST[5])
            elif ch2 == 16 : r_lst.append(JUNGSUNG_LIST[13]);r_lst.append(JUNGSUNG_LIST[20])
            elif ch2 == 19 : r_lst.append(JUNGSUNG_LIST[18]);r_lst.append(JUNGSUNG_LIST[20])
            else : r_lst.append(JUNGSUNG_LIST[ch2])

            #종성
            #겹받침 처리
            if ch3 == 0 : pass
            elif ch3 == 2 : r_lst.append(CHOSUNG_LIST[0]);r_lst.append(CHOSUNG_LIST[0]) #ㄲ
            elif ch3 == 3 : r_lst.append(CHOSUNG_LIST[0]);r_lst.append(CHOSUNG_LIST[9]) #ㄳ
            elif ch3 == 5 : r_lst.append(CHOSUNG_LIST[2]);r_lst.append(CHOSUNG_LIST[12]) #ㄵ
            elif ch3 == 6 : r_lst.append(CHOSUNG_LIST[2]);r_lst.append(CHOSUNG_LIST[18]) #ㄶ
            elif ch3 == 9 : r_lst.append(CHOSUNG_LIST[5]);r_lst.append(CHOSUNG_LIST[0]) #ㄺ
            elif ch3 == 10 : r_lst.append(CHOSUNG_LIST[5]);r_lst.append(CHOSUNG_LIST[6]) #ㄻ
            elif ch3 == 11 : r_lst.append(CHOSUNG_LIST[5]);r_lst.append(CHOSUNG_LIST[7]) #ㄼ
            elif ch3 == 12 : r_lst.append(CHOSUNG_LIST[5]);r_lst.append(CHOSUNG_LIST[9]) #ㄽ
            elif ch3 == 13 : r_lst.append(CHOSUNG_LIST[5]);r_lst.append(CHOSUNG_LIST[16]) #ㄾ
            elif ch3 == 14 : r_lst.append(CHOSUNG_LIST[5]);r_lst.append(CHOSUNG_LIST[17]) #ㄿ
            elif ch3 == 15 : r_lst.append(CHOSUNG_LIST[5]);r_lst.append(CHOSUNG_LIST[18]) #ㅀ
            elif ch3 == 18 : r_lst.append(CHOSUNG_LIST[7]);r_lst.append(CHOSUNG_LIST[9]) #ㅄ
            elif ch3 == 20 : r_lst.append(CHOSUNG_LIST[9]);r_lst.append(CHOSUNG_LIST[9]) #ㅆ
            else : r_lst.append(JONGSUNG_LIST[ch3])
        else:
            r_lst.append(w)
    return r_lst

def join(inputlist):
    result = ""
    cho, jung, jong = 0, 0, 0
    inputlist.insert(0, "")
    while len(inputlist) > 1:
        if inputlist[-1] == ' ' : result += inputlist.pop();continue
        if inputlist[-1] in JONGSUNG_LIST:
            #겹받침 처리
            if inputlist[-2] in JONGSUNG_LIST:
                r = CHOSUNG_LIST.index(inputlist.pop())
                l = CHOSUNG_LIST.index(inputlist.pop())
                if l == 0 and r == 0 : jong = 2
                elif l == 0 and r == 9 : jong = 3
                elif l == 2 and r == 12 : jong = 5
                elif l == 2 and r == 18 : jong = 6
                elif l == 5 and r == 0 : jong = 9
                elif l == 5 and r == 6 : jong = 10
                elif l == 5 and r == 7 : jong = 11
                elif l == 5 and r == 9 : jong = 12
                elif l == 5 and r == 16 : jong = 13
                elif l == 5 and r == 17 : jong = 14
                elif l == 5 and r == 18 : jong = 15
                elif l == 7 and r == 9 : jong = 18
                elif l == 9 and r == 9 : jong = 20
            elif inputlist[-2] in JUNGSUNG_LIST:
                jong = JONGSUNG_LIST.index(inputlist.pop())
            else:
                result += inputlist.pop()
        elif inputlist[-1] in JUNGSUNG_LIST:
            if inputlist[-2] in CHOSUNG_LIST or inputlist[-3] in CHOSUNG_LIST:
                #이중모음 처리
                if inputlist[-2] in JUNGSUNG_LIST:
                    r = JUNGSUNG_LIST.index(inputlist.pop())
                    l = JUNGSUNG_LIST.index(inputlist.pop())
                    if l == 2 and r == 20 : jung = 3
                    elif l == 6 and r == 20 : jung = 7
                    elif l == 8 and r == 0 : jung = 9
                    elif l == 8 and r == 1 : jung = 10
                    elif l == 8 and r == 20 : jung = 11
                    elif l == 13 and r == 4 : jung = 14
                    elif l == 13 and r == 5 : jung = 15
                    elif l == 13 and r == 20 : jung = 16
                    elif l == 18 and r == 20 : jung = 19
                else : jung = JUNGSUNG_LIST.index(inputlist.pop())
                cho = CHOSUNG_LIST.index(inputlist.pop())
                #쌍자음 처리
                if (cho == 0 or cho == 3 or cho == 7 or cho == 9 or cho == 12) and CHOSUNG_LIST[cho] == inputlist[-1]:
                    inputlist.pop()
                    cho += 1
                result += chr(0xAC00 + ((cho*21)+jung)*28+jong)
                cho, jung, jong = 0, 0, 0
            else:
                result += inputlist.pop()

        else:
            result += inputlist.pop()
    return result[::-1]

if __name__ == "__main__":

    koreanTree = make_morse_tree()

    test = input("문장을 입력하세요. (단, 완성형으로 구성된 한글문장)\n-> ")
    d_test = divide(test)
    print("\n문장을 조합형으로 나눈 결과")
    print(d_test)
    print()
    m_test = ""
    for i in d_test :
        m_test += encode(i)
        m_test += " "
    print("모스부호로 변환한 결과")
    print(m_test)
    print()

    m_test = m_test.split()
    c_test = []
    for i in m_test :
        c_test.append(decode(koreanTree,i))

    print("모스부호를 조합형을 변환한 결과")
    print(c_test)
    print()

    print("조합형을 완성형으로 변환한 결과")
    print(join(c_test))
    print()