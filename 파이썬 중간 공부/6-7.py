import random

a1, a2, a_result = 0, 0, 0
b1, b2, b_result = 0, 0, 0

a1 = random.randrange(1,7)
a2 = random.randrange(1,7)
b1 = random.randrange(1,7)
b2 = random.randrange(1,7)

a_result = a1 + a2
b_result = b1 + b2

print("A의 주사위 숫자는 %d %d입니다." %(a1, a2))
print("B의 주사위 숫자는 %d %d입니다." %(b1, b2))

if a_result > b_result:
    print("A가 이겼네요")
elif a_result < b_result:
    print("B가 이겼네요")
else:
    print("둘이 비겼네요")