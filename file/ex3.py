# file2.txt의 현재 내용 : 1~10줄
# 파일에 한글이 있으면 인코딩 추가(한글=utf-8)
f = open('file2.txt', 'r' , encoding='utf-8')

# read 함수로 내용 읽어오기
# => file2의 내용이 10줄 이상이기 때문에 readline(s)를 사용
lis = f.readlines()

# 내용을 한줄씩 출력
for line in lis :
    print(line, end=' ')


# 위의 내용에 새로운 내용 추가 : 11~21줄
# 내용 추가 -> 쓰기모드( w 또는 a)
# ' w ' 모드는 기존의 내용을 덮어씌움
# ' a ' 모드는 이전 내용에서 뒤에 추가 됨 
f = open('file2.txt', 'a' , encoding='utf-8')

# 10번 줄 뒤에
# 11~20번 줄을 추가 = 'a'모드
for i in range(11,21):
    f.write(f'{i}번째 줄입니다\n')

f.close()