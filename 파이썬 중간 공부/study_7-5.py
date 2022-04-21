baby = {"곰":"곰자식",
        "개":"개자식",
        "닭":"닭자식",
        "고등어":"고등어자식",
        "명태":"명태자식",
        "말":"말자식",
        "호랑이":"호랑이자식"}

while True:
    a = input(str(list(baby.keys())) + "중에 새끼 이름 알고 싶은 동물은?: ")
    if a in baby:
        print("%s의 새끼는 %s입니다." %(a, baby.get(a)))
    elif a == '끝':
        break
    else:
        print("다시 입력")