# file 입출력 문제
# 출력 후 콘솔 x 파일을 열어서 확인

# test.txt 파일을 만들고 다음과 같이 쓰세요
# "hello"
# "hi"
f = open('test.txt', 'w')

f.write('hello\n')
f.write('hi \n')

f.close()


# score.txt 파일을 만들고 다음과 같이 쓰세요
# "80 90 70 100 60"

f = open('score.txt' , 'w')

f.write("80 90 70 100 60")

f.close()

# numbers.txt 파일을 만들고 10부터 20까지 쓰세요
#10
#11
#12 ...
#20

f = open('numbers.txt','w')

for n in range(10,21):
    f.write(f'{n}\n')

f.close()