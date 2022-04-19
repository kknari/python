import random
list = []

for i in range(1, 21):
    a = random.randrange(1, 21)
    list.append(a)

print("생성된 리스트: ", list)

for k in range(1, 21):
    if k in list:
        print("%d는 뽑혔습니다." %k)
