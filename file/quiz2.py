# Q. score.txt 파일을 읽고 합계와 평균을 구하세요
# read=전체 내용을 문자열 하나로 가져옴(내용 적을 때) 
# readlines = 한줄씩 읽어서 리스트로 가져옴(내용 많을 때 )

f = open("score.txt", 'r')
text = f.read()                        
scores = text.split(' ')                  # read로 불러온 데이터가 통 데이터이기 때문에 쪼개줄 split함수 사용

sum = 0
for s in scores:
    sum += int(s)                       #s = str =>형변환필요 int사용

cnt = len(scores)

print("합계:", sum)
print("평균:", sum / cnt)
f.close()


# Q. numbers.txt 파일을 읽고 짝수만 출력하세요

f = open('numbers.txt', 'r')

lis = f.readlines()

for i in lis:
    if int(i) %2 == 0 :         # i = str =>형변환 int
        print(i, end=' ')

f.close()         


