i=0
hap=0

for i in range(0, 11, 1):
    hap = hap + i

print("1에서 10까지의 합계: %d" %hap)


i=0
hap=0

for i in range(0, 100, 7):
    hap = hap + i

print("1에서 100까지의 7의 배수 합계: %d" %hap)

s=0
l=0
g=0
hap=0

s = int(input("시작값을 입력하세요: "))
l = int(input("끝값을 입력하세요: "))
g = int(input("증가값을 입력하세요: "))

for g in range(s, l+1, g):
    hap = hap + g
    
print("%d부터 %d까지 %d값만큼 증가시킨 값의 합계: %d" %(s, l, g, hap))
