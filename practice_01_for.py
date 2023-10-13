# 문제1) 사용자가 입력한 단수를 출력하는 코드
# dan = int(input("단수: "))
# for i in range(1, 10):
#     print(f"{dan}x{i} = {dan*i}")

#  문제2) 2단에서 9단까지 출력(중첩 for문)
# for i in range(2, 10):                 # 단
#     for j in range(1, 10):             # 단수
#         print(f"{i} X {j} = {i*j}")

# 문제3) list a의 평균값을 계산하시오
a = [1, 2, 3, 4, 5, 99, 87, 54, 2, 5, 4]
# a길이 => len(a)
print(len(a))
total = 0
for num in a:
    total += num #tortal = tortal + num
result = total/len(a)
# round(값, 자리수) : 자리수만큼 반올림
print(round(result, 2))

print("="*50)
# 문제4) list b에서 최소값 찾기 #4.1 - 크기순정렬(자유)
b = [22, 1, 4, 7, 98]
num_min = b[0] # 22
for x in b:
    if x < num_min:
        num_min = x
print(f"최솟값: {num_min}") # 1 출력

print("="*50)
# 문제 5 list c의 최댓값 최솟값 찾기
c = [2, 5, 7, 1, 8]
num_min = c[0]
for x in c:
    if x < num_min:
        num_min = x

num_max = c[0]
for i in c:
    if i > num_max:
        num_max = i
print(f"최소값: {num_min}")
print(f"최대값: {num_max}")

