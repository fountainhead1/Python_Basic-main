# 조건문(Condition) : if ~ elif ~ else, 특정 조건을 만족하는 경우에만 수행할 작업이 있는 경우
# 모든 조건은 Boolean으로 표현 됨
# 조건문의 경우 if, elif, else 블록 내 종속된 코드 들여쓰기
# 모든 블록문의 시작점은 마지막에 : 추가
# Python에서 블록 내의 코드는 반드시 들여쓰기(tab -> 강제성을 가짐)


# if문의 4가지 조합
# 1. if
# 2. if~elif~elif
# 3. if~else
# 4. if~elif~else


# 논리연산자 AND, OR, NOT

# 1. AND
# 조건1  조건2  결과
#  F and F     F
#  T and F     F
#  F and T     F
#  T and T     T  -> 2개 모두여야 T

# 2. OR
# 조건1 조건2 결과
#  F or F    F
#  T or F    T  -> 1개이기만 해도 T
#  F or T    T
#  T or T    T

# 3. NOT : 입력값을 반대로 바꿈
# T -> F
# F -> T

# 문제 1. 어떤 종류의 학생인지 맞추시오(초등, 중등, 고등, 대학생, 학생X)
from datetime import datetime

# input() : 키보드에서 값을 입력할 때 모두 String 형태로만 받아들임
# 자료형을 변경해 줘야 함
born = input("당신이 태어난 년도를 입력하세요 : ")
today = datetime.today().year
age = today - int(born)+1
print(age)

if 8 <= age <= 26:
    if 20 <= age:
        print("대학생")
    elif 17 <= age:
        print("고등학생")
    elif 14 <= age:
        print("중학생")
    elif 8 <= age:
        print("초등학생")
else:
    print("학생이 아닙니다")
