# 아래 코드에서 각 변수에 무엇이 저장되는지 주석을 작성하세요

# 리스트를 입력받아 첫 번째 갑을 반환하는 함수 만들기
def func(lis):  #lis : result 값 함수의 매개변수(목적) 로, 함수 내부에 선언됨(scope)
    return lis[0]

my_lis = [10,20,30]     #my_lis :  함수에 전달하기 위한 리스트로, 메인에 선언 됨
result = func(my_lis)  #result : 함수의 결과를 저장하기 위한 변수로, 메인에 선언 됨
print(result)



# 문자열을 입력받아 길이를 반환하는 함수 만들기
def func(msg) :      #msg : 매개변수 "abc","hello"
    return len(msg)

my_str1 = "abc"   #my_str1 : func 함수를 호출할때 입력할 문자열
result1 = func(my_str1)  #result1 : func함수의 결과, "abc"의 길이를 저장할 변수
my_str2 = "hello"  #my_str2 :  func 함수를 호출할때 입력할 문자열
result2 = func(my_str2)  #result2 : "hello"의 길이를 저장할 변수