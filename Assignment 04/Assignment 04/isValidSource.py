from Stack import *
def isValidSource(lines) :
    stack = Stack()
    eCode, lcnt, ccnt = 0, 0, 0 # 각각 에러코드, 라인 수, 문자 수
    isch = False # ' 안에 있는 문자인지 확인하는 역할
    isch2 = False # " 안에 있는 문자인지 확인하는 역할
    ischl = False # /* */ 안에 있는 문자인지 확인하는 역할
    for line in lines :
        lcnt += 1
        for ch in range(len(line)) :
            ccnt += 1

            # // 뒤, 즉, 한줄 주석인 경우
            if not isch and not isch2 and not ischl \
                and line[ch] == '/' and line[ch+1] == '/' : break

            # /* */ : 여러 줄 주석인 경우
            if (line[ch] == '/' and line[ch+1] == '*') or \
               (line[ch] == '*' and line[ch+1] == '/'): ischl = not ischl
            if ischl : continue

            # ""안에 없는 ' 인 경우
            if line[ch] == '\'' and not isch2:
                isch = not isch
            if isch : continue

            # ''안에 없는 " 인 경우
            if line[ch] == '\"' and not isch:
                isch2 = not isch2
            if isch2 : continue

            if line[ch] in '{[(' :
                stack.push(line[ch]) # 여는 괄호는 스택에 쌓는다
            elif line[ch] in '}])' :
                if stack.isEmpty() : return 2, lcnt, ccnt # 2번 위반
                else :
                    left = stack.pop()
                    if (line[ch] == '}' and left != '{') or \
                       (line[ch] == ']' and left != '[') or \
                       (line[ch] == ')' and left != '(') :
                        return 3, lcnt, ccnt # 3번 위반
        ccnt = 0 # 한 줄이 끝나면 다시 문자 수를 0으로 초기화

    if not stack.isEmpty() : return 1, lcnt, ccnt # 1번 위반
    return 0, lcnt, ccnt # No problem