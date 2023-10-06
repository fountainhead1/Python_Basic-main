# while 반복문 : 반복 횟수가 정해져 있지 않은 경우 사용(반복 횟수를 모를 때)
# 조건을 만족하는 동안 계속 반복, 조건이 True이면 무한 반복 / 조건이 False일때 반복 종료
# while문에 조건 True -> 무한 Loop문(조심!) -> 반드시 break문과 함께 사용할 것

# while 기본 문법
# while 조건:
#      실행문

a = list(range(1, 6))
print(a)

i = 0  # index
while i < len(a):
    print(a[i])
    i += 1

