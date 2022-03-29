import random

ad1 = random.randint(1, 6)
ad2 = random.randint(1, 6)
bd1 = random.randint(1, 6)
bd2 = random.randint(1, 6)

print(f"A의 주사위 숫자는 {ad1} {ad2}입니다.")
print(f"B의 주사위 숫자는 {bd1} {bd2}입니다.")

if ad1+ad2 > bd1+bd2:
    print("A가 이겼네요.")
    
elif ad1+ad2 < bd1+bd2:
    print("B가 이겼네요.")

else:
    print("둘이 비겼네요.")
