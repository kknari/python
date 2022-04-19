ss = input("문자열을 입력하세요: ")
kor = ""
Eng = ""
eng = ""
num = ""
etc = ""

for i in ss:
    if ord('가') <= ord(i) <= ord('힣'):
        kor += i
    elif ord('A') <= ord(i) <= ord('Z'):
        Eng += i
    elif ord('a') <= ord(i) <= ord('z'):
        eng += i
    elif ord('0') <= ord(i) <= ord('9'):
        num += i
    else:
        etc += i
        

print("대문자: %s" %Eng)
print("소문자: %s" %eng) 
print("숫자: %s" %num) 
print("한글: %s" %kor)
print("기타: %s" %etc) 
