# 나머지 매개변수를 사용하여 
# 입력받은 과일의 이름만 출력하세요
# 예) apple , banana, orange

def calc(**kwargs):
    #여기에 코드를 작성하세요
    for key in kwargs.keys():
        print(key)                      #apple banana orange

# 함수호출
calc(apple =1200, banana = 800, orange = 1500)

# 나머지 매개변수를 사용하여 입력받은 학생의 점수만 출력하세요
# 결과) 90,85,100
dic = {'철수': 90, '영희':85, '민수':100}
print(dic.values())     #dict_values([90, 85, 100])

def show_scores(**kwargs):
    for value in kwargs.values():
        print(value)                        #90 85 100

# 함수호출
show_scores(철수 = 90, 영희 = 85, 민수 = 100)       #main의 첫줄 = 브레이크 포인트



# 나머지 매개변수를 사용하여 입력받은 도시 이름과 인구 수를 모두 출력하세요
# (인구 수는 만 명 단위)
# 결과) seoul 950, busan 340, incheon 300

dic ={'seoul' :950, 'busan': 340, 'incheon' :300}
print(dic.items())                                                    #dict_items([('seoul', 950), ('busan', 340), ('incheon', 300)])

def show_population(**kwargs):
    for k,v in kwargs.items():
        print(k,v)                                                         #seoul 950 busan 340 incheon 300
    

show_population(seoul = 950, busan = 340, incheon = 300)


# 나머지 매개변수를 사용하여 입력받은 상품의 상품명만 출력하세요
# 결과) milk bread egg(가격은 무시, 상품명만 출력)

dic ={'milk': 2500, 'bread' : 2000, 'egg' : 3000}
print(dic.keys())

def show_items(**kwargs):
    for k in kwargs.keys():
        print(k)                                    #milk bread egg

show_items(milk = 2500, bread = 2000, egg = 3000)
