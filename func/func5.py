# 함수 만들기
# 문자를 입력 받고, 나쁜 말이 들어오면 종료하는 함수
def say_nick(nick):
    # 닉네임 검사
    if nick == '바보' :    
        return     #함수 종료               
        #return 키워드를 만나면 더이상 코드를 실행x > 함수 종료 됨
        # return 키워드 뒤에 값 생략 가능, 값이 return만 있으면 함수만 종료 됨
    
    print(f'나의 별명은 {nick}입니다')        #출력 : 나의 별명은 짱구입니다

# 함수 호출
say_nick("짱구")            #나의 별명은 짱구입니다
say_nick("바보")            #나의 별명은 바보입니다 => 출력x
#나쁜말을 입력하면 강제 종료


# 함수 만들기
def func():
    a = 1
    b = 2
    c = 3

#반환값은 무조건 1개
# 한번에 abc를 반환하면 어떻게 될까?
    return a , b , c

# => return에 값을 여러개 쓰면 tuple로 묶어서 반환 됨
print(func())   # (1, 2, 3) = 튜플 1개

