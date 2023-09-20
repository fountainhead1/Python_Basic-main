# 컬렉션 타입 - 변수 하나에 값을 여러개 저장 : 실질적으로 변수에 컬렉션 1개가 저장
# 리스트(List), 튜플(Tuple), 딕셔너리(Dictionary), 세트(Set)

# 리스트(List) : 시퀀스 자료형(연속된 값을 저장함), 정렬 가능, mutable(생성 된 후 값 변경 가능), index 사용(Slicing 가능), 패킹과 언패킹 가능, 멤버함수 : append(), extend(), insert(), remove(), pop(), index(), sorted(), et cetera, 대괄호 사용
# 리스트 초기화(생성)
list_a = [1, 2, 3]
list_b = []
list_c = ["chosun", 98, 3.14, [1, 2, 3]]  # 리스트 안의 리스트 -> 2차원, 3차원, ...
# 2차원 리스트는 표(table)와 동일한 형태를 갖는다.

print(list_c[1:3])
print(list_c[0])

# 패킹과 언패킹
list_d = ["a", "b", "c"]  # 패킹
a, b, c = list_d  # 언패킹

a = [1, 2, 3, 4, 5]
a.append(10)  # append(value) : 리스트 맨 마지막에 값을 추가
print(a)

a.insert(1, "A")  # insert(index, object) : 원하는 인덱스에 특정 값을 추가
print(a)

a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)  # extend(): 리스트 병합(List A + List B) - A에 B를 넣는다(A가 기준이 됨)
print(a)  # = print(a+b)

a = ["a", "b", "c"]
a.remove("b")  # remove() : 값으로 삭제
print(a)

b = ["a", "b", "c"]
b.pop(0)  # pop() : 인덱스로 삭제
c = b.pop(0)  # 값을 삭제 전 변수에 담아서 삭제 후에 사용 가능(선택사항)
print(b)
print(c)

a = [1, 2, 3]
print(a.index(3))  # index() : 찾고자 하는 값의 인덱스 반환 - "2"를 반환함

# sort() and sorted() : 리스트 값 정렬
# sort() : 원본 값 정렬 - 원본 값까지 수정하기 때문에, 사용하는 경우가 드뭄
# sorted() : 복제 한 값 정렬

a = [9, 3, 2, 1, 5, 8, 10]
b = sorted(a)  # 원본 값은 정렬되지 않은 상태로 그대로 출력됨.
b = sorted(a, reverse=True)  # 내림차순 정렬도 가능함(Default : 오름차순)
print(a)
print(b)