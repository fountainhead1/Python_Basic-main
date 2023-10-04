# 문제1) 입력된 단수를 출력하는 코드
# dan = int(input("단수 : "))
# for i in range(1, 10):
#    print(f"{dan} x {i} = {dan*i}")

# 문제2) 2단 ~ 9단
for i in range(2, 10):
    for j in range(1, 10):
        print(f"{i} x {j} = {i*j}")

print("=" * 200)

# 문제3) list a의 평균값을 계산하세요
a = [1, 2, 3, 4, 5, 99, 87, 54, 2, 5, 4]
length = len(a)
total = 0
for i in a:
    total += i

result = total / length
print(round(result, 2))  # round(값, 소수점 숫자) 함수 -> 반올림

# 문제4) list b에서 최소값 찾기
b = [22, 1, 4, 7, 98]

print(num_min)