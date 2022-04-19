select, answer, innum, n1, n2 = 0, 0, '', 0, 0

select=int(input("1. 입력된 수식 계산, 2. 두 수 사이의 합계: "))

if select==1:
    innum = input("수식을 입력하세요: ")
    answer = eval(innum)
    print("입력된 수식: %s, 답: %f" %(innum, answer))

elif select==2:
    n1 = int(input("첫 번째 숫자 입력: "))
    n2 = int(input("두 번째 숫자 입력: "))
    for i in range(n1, n2+1):
        answer += i
    print("%d부터 %d까지의 합계: %d" %(n1, n2, answer))