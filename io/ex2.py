# 키보드로 입력받기
# 모니터에 출력하기
# print : 화면에 숫자, 문자 ,리스트 등을 출력하는 함수

print(123)   # 숫자 출력
print("python")   # 문자열 출력
print([1, 2, 3])   # 리스트 출력

# 여러 문자열을 연결하여 출력
print("hello" "world")  
print("hello" + "world")
print("hello", "world") # 콤마를 쓰면 공백이 들어감

# print 함수는 출력 후 줄바꿈됨
# end 옵션으로 출력 뒤에 올 문자를 지정할 수 있음
print(1)
print(2)
print(3)

# print 함수의 선언부
# end는 기본값이 있는 매개변수
# '\n'은 특수문자로 줄바꿈
# end 옵션은 앞에 value를 출력, 마지막으로 \n을 출력함
# print(value, end='\n')

# end 매개변수를 줄바꿈 대신 공백으로 바꾸기
print(1, end = ' ')
print(2, end = ' ')
print(3, end = ' ')
# 출력 => 1 2 3

