# p85, P2.1

#정순 탐색 해결방법
#rate = [[0,6],[1200,15],[4600,24],[8800,35],[15000,38]]
#tax = 0.0

#income = int(input("소득을 입력하세요(만원 단위) ==> "))

#for i in range(len(rate)) : 
#    if(income > rate[i][0]) :
#        if(income > rate[i+1][0] and i+1 in range(len(rate))) :
#            tax += (rate[i+1][0] - rate[i][0]) * rate[i][1] / 100
#        else :
#            tax += (income - rate[i][0]) * rate[i][1] / 100

#print('전체세금 =',tax)
#print('순수소득 =',income-tax)

#역순 탐색 해결방법
rate = [[0,6],[1200,15],[4600,24],[8800,35],[15000,38]]
tax = 0.0

income = int(input("소득을 입력하세요(만원 단위) ==> "))
n = income
for i in rate[::-1] :
    if n > i[0] :
        tax += (n-i[0]) * i[1] / 100
        n -= (n-i[0])

print('전체세금 =',tax)
print('순수소득 =',income-tax)