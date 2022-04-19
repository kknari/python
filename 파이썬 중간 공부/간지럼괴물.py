print("시작")
print("괴물이 나타났습니다!")
a = int(input("도망 0, 공격 1 입력: "))

if a==0:
    print("뜁니다")
    a1 = int(input("0과 1중 선택: "))
    if a1 == 0:
        print("잡혔습니다... 공격당함")
    elif a1 == 1:
        print("무사히 도망쳤습니다")
        
elif a==1:
    print("간지럽힙니다")
    a2 = int(input("0과 1중 선택: "))
    if a2==0:
        print("웃게 만들었습니다! 성공!")
    elif a2==1:
        print("괴물이 오히려 화났습니다... 공격당함")
    

print("끝")