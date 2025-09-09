# 함수 만들기
# 두 수의 차를 구하는 함수 정의
# 매개변수 : 함수에 필요한 입력 값, 숫자 두개
# 반환값 : 두 수의 차를 구해서 결과를 반환
def sub(n1, n2):
    return n1 - n2

# 함수 호출
# 함수이름(함수에 필요한 값 입력)
# 입력값 있고, 반환값 있음,
# => 함수 내부에서 결과 확인x
result = sub(7,3)               #main 첫줄! = 시작
print(result)                       # 4 마지막 ! = 결과값 출력, 끝


# 인자를 순서와 상관없이 입력
# 매개변수의 이름을 직접 지정(매개변수이름 = 값 입력)
result = sub(n2=3, n1=7)              
print(result)  


# 문자열 두개를 입력받아 연결하는 함수 정의
def add_text(str1, str2):
    # 문자열 연결 방법
    print(str1 + ' ' + str2)            #hello world 
    # print(str1, str2)
    # print(f'{str1} {str2}')

# 함수 호출
# 매개변수를 순서대로 입력 (str1, str2)
# add_text('hello','world')

# 매개변수 이름을 지정하여 입력
# 순서와 상관없이 전달 가능
add_text(str2='world', str1='hello')


