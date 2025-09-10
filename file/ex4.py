# 파일을 쓰기 모드로 열기
f = open('new.txt', 'w')
f.write('hello world')
f.close()

# 위의 코드를 간단하게 작성하기
# with [open ( 파일이름, 모드 )] as f :
        #f.write(입력할내용)

with  open('new.txt', 'w') as f :               #with를 사용하면 마지막에 자동으로 close가 실행됨
    f.write('hello world')                          #블록에는 수행하고 싶은 코드를 작성
    #f.close는 생략