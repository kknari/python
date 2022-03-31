import random 

numbers = []
for num in range(1, 21) :
    numbers.append(random.randrange(1, 21))

print("생성된 리스트", numbers)

for num in range(1, 21) :
    if num in numbers :
        print("숫자 %d는 (은) 뽑혔습니다." %num)
