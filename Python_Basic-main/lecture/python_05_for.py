# 제어문 - 1. 조건문(if, switch~case), 2. 반복문(for, while)

# 반복문(Loop) - 반복적인 작업을 가능하게 해주는 도구
# list, str, tuple 등 컬렉션 타입의 아이템을 하나씩 순회하면서 사용 가능(for)
# 특정 조건을 만족하는 경우(while)

# 반복횟수를 알고 있을 때 -> for / 반복횟수를 모를 때 -> while 사용

# for문 기본 문법
# for i in [1, 2, 3] :
#   print(i)    -> 3번 반복하는 것을 알 수 있음(=반복횟수를 이미 알고 있다)

# range(시작, 끝, 증감)
# range(3) -> 0부터 2까지 1의 간격으로 출력 -> 간격을 따로 입력해주지 않으면 자동으로 +1
# range(1, 10) -> 1부터 9까지 출력
# range(2, 5, 2) -> 2부터 4까지 2의 간격으로 출력(2, 4 출력)

# range()를 활용하여 1부터 9가지 출력하는 for문
for i in range(1, 10):
    print(i)

print("=" * 200)

# List를 활용한 for문
temp = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
for alpha in temp:
    print(alpha)

# Index를 출력하고 싶은 경우 - enumerate 함수 사용 (index는 0번부터 시작함)
for i, alpha in enumerate(temp):
    print(i, alpha)

print("=" * 200)

# 구구단 2단 출력

# input() 활용해서 사용자가 입력한 값(2~9) -> 해당 단 출력
for i in range(1, 10):
    print(f"2x{i}={2*i}")

# dict를 사용한 for문 -> value가 아닌 key값을 출력함
# keys(), values(), items() -> keys는 굳이 사용할 필요가 없다.
temp = {"A" : 1, "B" : 2, "C" : 3, "D" : 4}

for element in temp:
    print(element)
for element in temp.values():
    print(element)
for element in temp.items():
    print(element)

for key, value in temp.items():
    print("*****")
    print(key)
    print(value)

# break, continue
# break : 반복문을 즉시 빠져 나감
# continue : 다음 반복으로 즉시 넘어감

a = [1, 2, 3, 4, 5]
for i in a:
    if i == 3:
        break;
    print(i)

print("=" * 200)

# 홀수만 출력
for i in range(30):
    if i % 2 == 0:
        continue
    print(i)