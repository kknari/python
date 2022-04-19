hap = 0 
i = 0

while i < 101:
    hap += i
    if hap >= 1000:
        break
    i += 1

print("1~100 합계를 최초로 1000 넘게하는 숫자: %d" %i)