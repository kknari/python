# import re
# ss = input("문자열을 입력하세요: ")

# word = re.sub('[^가-힣a-zA-Z]', '', ss).strip()
# print(word)

ss = input("문자열을 입력하세요: ")
result = ""

for i in ss:
    if ord('가') <= ord(i) <= ord('힣'):
        result += i
    elif ord('A') <= ord(i) <= ord('Z'):
        result += i
    elif ord('a') <= ord(i) <= ord('z'):
        result += i
    else:
        del(i)

print(result)