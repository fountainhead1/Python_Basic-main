# 문자열(String)의 이해

# 1. 문자열 인덱스
# 문자열은 각 문자마다 순서(인덱스)가 있음
# 첫번째 문자부터 마지막 문자까지 순차적으로 인덱스
# 인덱스 시작은 0(첫 문자열의 인덱스 = 0)
# 인덱스는 공백을 포함

print("=" * 200)

# 2. 문자 추출 - 인덱스를 통해서 문자 추출, 인덱스 범위 벗어난 경우 오류(index out of range) 발생
lang = "Python"
print(lang[0])
print(lang[2])
#  print(lang[9]) - IndexError: string index out of range

print("=" * 200)

# -1 인덱스(Reverse Index)
# 우측에서부터 좌측으로 인덱스를 붙임
# 최초 값 : -1 (0이 아님)

print(lang[-1])
print(lang[-3])

print("=" * 200)

# 3. 문자열 슬라이싱
# lang[3] -> 문자 1개만 추출
# 슬라이싱 : 부분 문자열을 추출하고 싶은 경우
# 시작 인덱스 : 끝 인덱스 2개가 필요함
# 끝 인덱스 번호 : +1 해줘야 함(e.g. [0:6] -> 0번 인덱스부터 5번 인덱스까지 출력)

msg = "Python is all you need"
print(msg[0:6])
print(msg[:6])  # 시작 인덱스 생략 -> 처음 인덱스(0번)부터 시작
print(msg[3:])  # 끝 인덱스 생략 -> 끝 인덱스(-1)까지 슬라이싱
print(msg[:]) # 시작/끝 인덱스 생략 -> 전체 출력

print("=" * 200)

print(msg[18:])  # 정방향 인덱스
print(msg[-4:])  # 역방향 인덱스

print("=" * 200)

# 4. 문자열 함수

str = "Hello World"

# 4-1. len() 함수 : 문자열 길이 계산 -> 자주 사용됨
print(len(str))

# 4-2. upper() and lower() : 대문자 / 소문자 변경 - 데이터 전처리 할 때에도 사용(e.g. 1a -> 1A or 1A -> 1a)
print(str.upper())
print(str.lower())

# 4-3. replace() 함수 : 문자열 내의 특정 문자를 치환해줌
print(str.replace("H", "J"))

# 4-4. split() 함수 : 구분자를 기준으로 문자열 분할(Default : 공백)
b = "Hello World what a nice weather"
print(b.split("w"))
print(b.split())  # 괄호 안에 아무것도 입력하지 않으면 공백을 기준으로 문자열을 분할하는 것임

# 4-5. strip() 함수 : 문자열의 좌우 공백을 제거해줌
id = "            python1004               "
print(id)
print(id.strip())

# 4-6. find() and rfind() : 문자열 내부의 특정 문자 위치 인덱스 출력 -> find는 왼쪽부터, rfind는 오른쪽부터 찾는다
# 중복되어 있는 것은 고려하지 않음, 처음 찾은 한 개만 뽑는다
print(str.find("o"))  # 4th "o"
print(str.rfind("o"))  # 7th "o"

print(str.find("Hello"))  # 0 -> 첫 글자의 인덱스를 출력함
print(str.find("world"))  # -1 -> 존재하지 않는 것은 -1을 출력함
print(str.find("World"))  # 6
print(str.rfind("World"))  # 6 -> find와 rfind 모두 첫 글자의 인덱스를 출력

# 4-7. in() : 특정 문자열이 포함되어 있는지 확인(출력형태 : True / False)
print("Hi" in "Hi Python")

print("=" * 200)

# Q1. id = "cherry1004@gmail.com" -> id만 추출
id1 = "cherry1004@gmail.com"
# id2 = "job1234@gmail.com"
# id3 = "abc@gmail.com"

num = id1.find("@")
val = id1[:num]
print(val)

# Q2
# www.naver.com
# www.daum.net
# www.google.com

url = "www.naver.com"

num_left = url.find(".") + 1
num_right = url.rfind(".")
val = url[num_left : num_right]

print(val)