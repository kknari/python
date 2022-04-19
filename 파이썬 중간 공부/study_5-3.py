a = int(input("숫자 입력: "))

for i in range(2, a):
    if a%i == 0:
        print("%d는 소수가 아닙니다." %a)
        break
    elif i==(a-1):
        print("%d는 소수입니다." %a)