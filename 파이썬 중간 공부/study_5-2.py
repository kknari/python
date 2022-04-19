a = int(input("첫 번째 숫자 입력: "))
b = int(input("두 번째 숫자 입력: "))
plus = int(input("더할 숫자 입력: "))
hap = 0

for i in range(a, b+1, plus):
    hap += i

print("%d+%d+...+%d의 합은 %d입니다." %(a, a+plus, b, hap))