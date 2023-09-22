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

# 2. 튜플(Tuple) : 리스트와 대부분 동일, 정렬 불가능하고 immutable(생성 된 후 값 변경 불가능)
# index 사용, packing/unpacking 가능, () 사용 - 생략 가능함
# 직접 Tuple을 생성하는 경우는 드뭄 -> Python에서 결과값을 받을 때 Tuple로 제공함

print("=" * 200)

a = [1, 2, 3]  # List
b = (1, 2, 3)  # Tuple
c = 1, 2, 3  # Tuple(괄호를 생략 가능하다)

a[0] = 99
print(a)

#  b[0] = 99
#  print(b)
#  오류 출력 -> Tuple은 값 변경이 불가능함

# Tuple 원소가 1개인 경우, 1개의 값?
a = (1, 2, 3)  # Tuple
b = 1, 2, 3    # Tuple
c = (1)        # Tuple
d = 1          # Int(Tuple이 아닌 Int로 출력)
e = 1,         # Tuple(원소 1개인 경우 원소 뒤에 , 를 붙여주면 Tuple로 출력)
print(type(b))
print(type(d))
print(type(e))

print("=" * 200)

a = 5
b = 8

a, b = b, a  # 튜플(패킹) 활용

print(a)
print(b)

# 3. Set(세트) : 수학의 집합 개념, 순서 없음(인덱스 및 정렬 불가능), 중복 값이 허용되지 않음(중요 -> 주 사용 목적), {} 사용
# member 함수 : union(), intersection(), difference(), 등.. (합/차/교집합 개념)

set_a = {1, 2, 3}
set_b = {1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 5}  # 중복 값을 싹 지우고 출력 - {1, 2, 3, 4, 5}
print(set_b)

# e.g. 중복값 제거 활용 방법
a = ["A", "A", "B", "B", "C", "C", "D", "E"]
a = list(set(a))  # List -> Set(중복값 제거) -> List(원형 복구)

print(a)

# 4. 딕트(Dictionary) : 순서가 없음(인덱스, 정렬 X), {key : value} 꼴로 사용 - key, value가 1쌍
# key는 중복 불가, value는 중복 가능, key를 통해서만 value에 접근이 가능함
# member 함수 : update(), get(), keys(), values(), items()

# 외부에서 데이터를 받아올 때 json이라는 형식으로 전달
# json == dict (동일)

dict_a = {"Korea" : "Seoul",
          "Canada" : "Ottawa",
          "USA" : "Washington D.C"}

print(dict_a)

# update() : dict와 dict를 병합해서 1개로 만듬(list의 extend와 동일)
a = {"a" : 1,
     "b" : 2}
b = {"b" : 3,
     "c" : 5}
a.update(b)
print(a)  # {'a': 1, 'b': 3, 'c': 5} : key값을 중복 허용하지 않음 -> (병합시 중복 key가 있는 경우) 나중에 온 값을 넣음

# pop() : dict 원소를 key로 삭제

c = a.pop("a")
print(a)
print(c)  # 삭제된 value를 출력

# in() : () 안의 key 값이 존재하는지 확인
print("c" in a)
print("f" in a)

# get() : 값 접근
# list, tuple, dict 접근 -> 컬렉션[Index or Key] : ex) a[2]
# print(a["f"])  # 존재하지 않는 key에 접근하는 경우 error 출력

print(a.get("f"))  # key가 없으면 none 출력(error 출력 X)

# keys(), values(), items() -> 사용빈도 높음
print(a.keys())  # key만 추출
print(a.values())  # value만 추출
print(a.items())  # (key, value) 추출

# 활용할 때 print(list(a.keys())) 같은 식으로 리스트로 형태 변경해서 추출

# clear() : dict 초기화
print(a)
a.clear()
print(a)

a = {}
print(type(a))  # <class 'dict'> : set 형태가 아닌 dict 형태