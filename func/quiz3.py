# 단을 입력 받아 구구단을 출력하는 함수를 만드세요(리턴x)
# 예 ) 3단 3x1 =3, 3x2 =6....


def func(num):
           for n in range(1,10):
            print(f'{num}x{n}={num*n}')
            for i in range(2,10):
                print(i)
                func(i)


# 2단부터 9단까지 출력하세요
           

# 리스트를 입력받아 그 안에 
# 문자열(str) 자료형이 몇 개인지 세는 함수를 만드세요
# 예) [1,"apple",3.5,'banana',10, 'hi'] ->3
# 예 ) ['a','b','c'] ->3
# 예) [1,2,3]->0
sum = 0
def func(lis):
            #전달받은 리스트에서 문자 개수 세기
            #리스트 안에 있는 요소 하나씩 꺼내고, 문자인지 확인
    for item in lis:                    #조건 : if , 요소의 타입 == str
          if type(item)==str :        #자료형은 ''문자열처리x 예약어로 작성
             print(item)
      

func([1,"apple",3.5,'banana',10, 'hi'])
func( ['a','b','c'])
func([1,2,3])


def count_strings(lst):
    count = 0
    for item in lst:
        if isinstance(item, str):
            count += 1
    return count

print(count_strings([1,"apple",3.5,'banana',10, 'hi']))
print(count_strings(['a','b','c']))                      
print(count_strings([1,2,3]))     