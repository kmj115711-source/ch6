# 반대로 파일의 내용을 읽어오기

# 읽기 모드로 파일 열기
# => 파일 이름, 모드(w=쓰기, r=읽기) , 같은 경로에 있을 때는 이름만 적어줘도O
f = open('새파일.txt', 'r')


# 파일의 내용 읽어오기
# 읽기 함수들 중에서 
# readlines는 결과를 리스트로 반환
# 결과는 리스트로 저장됨
# lines = f.readlines() = ['a b c d e'] 

# read는 파일의 내용을 문자열 하나로 반환
text = f.read()

print(text)       #a b c d e

#문자열 안에 있는 알파벳을 하나씩 꺼내기
# split = 함수의 인자 : 구분자,
# => 공백을 기준으로 문자열을 쪼개고 결과를 리스트로 반환
# 리턴값이 있을 때 :
lis = text.split( ' ' )   #구분자 = 공백
print(lis)                  #['a', 'b', 'c', 'd', 'e']

# 반환받은 리스트를 이용, 알파벳 하나씩 출력하기
for ch in lis:
    print(ch)               #a b c d e


# 리턴값이 없을 때 :
# lis.sort()

f.close()


# 반대로 파일 읽어오기
# 입력장치 : 키보드 -> 파일

# 키보드에서 값 입력받기
# input()
# 파일에서 값 읽어오기
# f.read()

f = open('file1.txt', 'r')
# 결과를 리스트로 반환
lis = f.readlines()

# 한줄씩 출력하기
for line in lis : 
    # end 매개변수 값 변경
    # => 기본값이 \n = 줄바꿈,=> 기본값을 ' ' 공백으로 바꿔 줄바꿈 1번으로 
    print(line, end=' ')

#print함수에는 end라는 매개변수가 있고
# 기본값이 \n
print('1', end='\n') 


#print(lis)      #['1\n', '2\n', '3\n', '4\n', '5\n', '6\n', '7\n', '8\n', '9\n', '10\n'] =줄바꿈 포함



