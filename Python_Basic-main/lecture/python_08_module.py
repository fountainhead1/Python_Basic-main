# 라이브러리(Library), 패키지(Package), 모듈(Module)
# 라이브러리 >= 패키지 >= 모듈

# 1. 라이브러리 : 여러 패키지와 모듈의 묶음
# 2. 패키지 : 특정 기능과 관련된 여러 모듈의 묶음
# 3. 모듈 : 이미 작성된 프로그램(일반적으로 한 파일을 의미)

# ** 모듈의 종류
# 1. 내부 모듈 : 파이썬 설치하면 기본적으로 제공
# 2. 외부 모듈 : 다른 개발자가 개발해 놓은 모듈
# 3. 사용자 정의 모듈 : 사용자가 직접 개발해서 사용하는 모듈

# ** 모듈 사용 방법
# 라이브러리 또는 모듈을 사용하기 위해서는 "import" 필요

# 가정 : requests 내에 1000개의 모듈이 있음
# 1. import
# e.g.) import requests
#   → "requests" library 전체를 호출함(→ 라이브러리 내의 1000개의 모듈 전체를 가져옴)
#   → requests.get()

# 2. from ~ import
# e.g.) from requests import get
#   → "requests" library 내에서 get module만 호출(1000개중 get이라는 모듈 1개만 호출)
#   → get()

# 3. as(Alias : 별명)
# e.g.) import requests as req
#   → "requests" module 전체를 호출하고 req라는 별명을 붙임
#   → req.get()