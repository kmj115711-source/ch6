# file
# 이전 입출력 장치 : 키보드와 모니터

# 파일 열기 = 파일은 입,출력 동시에 x
#파일이 있으면 연결되고,  해당 파일이 없으면 새로 생성됨
# open(파일이름, 모드) 

# f = open('새파일.txt', 'w')

# 파일에 내용 쓰기
# f.write('a b c d e')

# 파일 닫기
# 안써도 프로그램상 문제는 없지만
# 프로그램과 파일이 계속 연결되어 있어 메모리가 낭비됨
# f.close()

# 파일 열기
# open(파일이름, 모드)
f = open('file1.txt', 'w')

# 파일에 1부터 10까지 쓰기
for n in range(1,11):
    # 줄바꿈 추가
    f.write(f'{n}\n')     #write 함수의 매개변수는 int =>str

f.close()

# 파일을 쓰기 모드로 열기
# 한글 입력시 인코딩 설정 추가
f = open('file2.txt', 'w', encoding='utf-8')

# 1부터 10까지 출력하기
for i in range(1,11):
    f.write(f'{i}번째 줄입니다\n')     #i = 정수, int => str

f.close()