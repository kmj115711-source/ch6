# 더하기 함수 만들기
def add(a, b):
    return a + b

# 람다 함수 만들기
# 변수 = lambda 매개변수 : 반환값
# 변수 = 함수
add = lambda a , b : a+b        #변수 이름 x = 익명함수

# 람다 함수 호출
result = add(3, 4)
print(result)

# 꼭 써야 하는가?
# 복합 대입이나  람다 함수는 선택이다
# sum += 1 


# 문자열 정렬
strings = ['foo', 'card', 'ba', 'aaa']

# sort : 목록을 순차적으로 정렬, 함수의 입력값으로 함수 입력
# 예) 1 2 3 4 5/ 5 4 3 2 1
# 문자를 정렬할때는 람다 함수 필요

# result = strings.sort()  => 출력x #none
# 문자의 크기를 비교하는 함수
# 변수 = lambda 매개변수 : 반환값

# sort는 원본을 변경하는 함수 => 반환 x
# 숫자는 자동으로 오름차순 정렬,
# 문자는 정렬기준이 없으므로 람다함수로 정렬기준 작성해야 함
# sort 함수의 매개변수는 함수
# 함수의 매개변수가 함수 일 때 , 람다식 함수를 활용 
strings.sort( key= lambda s : len(s))

print(strings)       #['ba', 'foo', 'aaa', 'card']