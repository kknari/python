hap = 0

while True:
    a = input("더할 첫 번째 수 입력: ")
    if a=='$':
        break
    else:
        a = int(a)

    b = int(input("더할 두 번째 수 입력: "))
    hap = a+b
    print("%d + %d = %d" %(a, b, hap))