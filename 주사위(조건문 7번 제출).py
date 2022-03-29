import random

ad_1 = random.randint(1, 6)
ad_2 = random.randint(1, 6)
ad_result = ad_1 + ad_2

bd_1 = random.randint(1, 6)
bd_2 = random.randint(1, 6)
bd_result = bd_1 + bd_2

print("A의 주사위는 %d %d입니다." %(ad_1, ad_2))
print("B의 주사위는 %d %d입니다." %(bd_1, bd_2))

if ad_result > bd_result :
    print("A가 이겼네요.")

elif ad_result < bd_result :
    print("B가 이겼네요.")

else :
    print("둘이 비겼네요.")
