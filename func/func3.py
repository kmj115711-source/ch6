# 함수 만들기
# 값을 하나 입력 받고 출력하기
def func1(a):
    print(a)

# 함수 호출하기
func1(1)


# 값을 두개 입력 받고 호출하는 함수 만들기
def func2(a, b):
     print(a, b)

func2(1, 2)

# 값을 세개 입력 받고 호출하는 함수 만들기
def func3(a, b, c):
     print(a, b, c)

func3(1, 2, 3)


# 매개변수의 개수가 달라져도 사용할 수 있는 함수 만들기
# => 나머지 매개변수 = 나머지 매개변수 만들때는 별 [**] 두개
def func(**kwargs):
     print(kwargs)

# 함수 호출
# 나머지 매개변수는 딕셔너리 형태로 저장됨
# => 따라서 마음대로 데이터를 추가할 수 있음
func(a=1)                   #{'a': 1}
func(a=1, b=2)          #{'a': 1, 'b': 2}


# 나머지 매개변수를 사용하는 함수 만들기
# 사람의 정보를 입력받아 출력하는 함수 만들기=(모두 출력)
def info(**kwargs):
     print(kwargs)

# 함수 호출
info(name='둘리', age =10) 
 #주소 모름 {'name': '둘리', 'age': 10} =>dic 1개 , 요소의 갯수 상관x
info(name='도우너', age =8, address = '서울')  
 #{'name': '도우너', 'age': 8, 'address': '서울'} =>dic 1개


# 딕셔너리의 함수들
dic = {'name':'둘리','age':10}
print(dic.keys())       #dict_keys(['name', 'age']) =>이터러블 객체(순회 가능) = for문 사용 가능
print(dic.values())     #dict_values(['둘리', 10])
print(dic.items())      #dict_items([('name', '둘리'), ('age', 10)]) = items 객체의 요소는 튜플

#  사람의 정보를 하나씩 꺼내기
def info(**kwargs):
     #딕셔너리 안에 있는 요소 하나씩 꺼내기 
    #  =>item 객체에서 요소를 꺼내면 튜플, 구조분해로 변수 두개에 (key, value)저장
     for key, value in kwargs.items():       #예 : ('name', '둘리')
         print(key, value)                            #예 : name 둘리

info(name='둘리', age =10)   #주소 모름
info(name='도우너', age =8, address = '서울')  