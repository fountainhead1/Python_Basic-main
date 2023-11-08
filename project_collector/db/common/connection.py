# 데이터베이스(DB) : 데이터를 효율적으로 저장하는 시스템(이론)
# File System : 폴더를 사용한 데이터 저장(데이터를 관리하지 않고 저장만 함)

# 데이터베이스 관리시스템(DBMS) : DB 이론을 실제로 구현
# ** DBMS 종류
#  1) 관계형 데이터베이스(RDB) : 전통적(스키마 : 명세서 사용) -> 데이터 처리가 까다로움
#   - ORACLE, MySQL, MariaDB
#  2) NoSQL -> 신형 DBMS : 스키마를 사용하지 않음 -> 데이터 처리 속도 빠름
#   - MongoDB, Redis
#  두개는 상호보완 관계

# ** DB 프로세스
#  PyCharm(Python)  ---------------  DB(MongoDB)
#  - Do : ID/PW 저장
#  1) PyCharm - DB Connection 맺기
#     - IP(컴퓨터를 찾아갈 수 있는 주소), PORT(컴퓨터 내에서 특정 프로그램의 위치), ID/PW 4가지 필요
#  2) SQL을 사용해서 DB에 CRUD 작업 진행
#     - SQL(구조질의어) : DB와 소통할 수 있는 언어(반드시)
#     Create(삽입), Read(조회), Update(수정), Delete(삭제) - CRUD
#     Insert, Select, Update, Delete(SQL에서 쓰는 방법)