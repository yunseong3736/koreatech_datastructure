# p85, P2.2
import random

answer = random.randrange(0,100)
min = 0 ; max = 99
for i in range(10):
    guess = int(input(f"숫자를 입력하세요(범위:{min}~{max}) : "))
    if guess == answer :
        print('정답입니다. {:2d}번 만에 맞추셨습니다.'.format(i+1))
        break
    elif guess > answer :
        print('아닙니다. 더 작은 숫자입니다!')
        max = guess
    else :
        print('아닙니다. 더 큰 숫자입니다!')
        min = guess
print('게임이 끝났습니다.')