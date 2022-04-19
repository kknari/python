hap = 0

a = int(input("시작값 입력: "))
b = int(input("끝값 입력: "))
plus = int(input("증가값 입력: "))

while a < b+1:
    hap += a
    a += plus

print(hap)