import random
comscore = 0
mescore = 0

print("컴퓨터와 하는 가위바위보 게임입니다.")

while True:
    a = input("가위', '바위', '보' 중 입력(끝내려면 끝 입력): ")
    
    if a == '끝':
        break
    
    com = random.randint(1, 3)
    if com == 1 :
        com = '가위'
        print("컴퓨터는 가위")
        
    elif com == 2:
        com = '바위'
        print("컴퓨터는 바위")
        
    elif com == 3:
        com = '보'
        print("컴퓨터는 보")
        

    if (a == com):
        print("비겼습니다 \n")

    elif (a == '가위' and com == '보') or (a == '바위' and com == '가위') or (a == '보' and com == '바위'):
        print("이겼습니다 \n")
        mescore = mescore + 1
    else:
        print("졌습니다 \n")
        comscore = comscore + 1

    if (mescore == 2) or (comscore == 2):
        break
