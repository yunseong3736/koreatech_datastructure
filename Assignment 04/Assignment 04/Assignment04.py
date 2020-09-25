from isValidSource import *

#filename = "ArrayStack.h"
filename = "CheckBracketMain.cpp"     # 주석을 이용해서 괄호를 검사할 소스 파일 결정

infile = open(filename, 'r')
lines = infile.readlines()
infile.close()

eCode, lcnt, ccnt = isValidSource(lines) #isValidSource 함수로부터 에러코드와 해당 라인수, 해당 문자수를 구함
if eCode == 0 : print(filename, "---> No problem") # 에러코드가 0일 경우에는 문제가 없음을 확실하게 명시
else : 
    print(filename, " ---> ", eCode)
    print(" 라인수 = ", lcnt)
    print(" 문자수 = ", ccnt)