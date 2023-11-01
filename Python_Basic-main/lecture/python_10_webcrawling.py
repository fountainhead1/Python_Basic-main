# WebCrawling(웹 크롤링) : 웹 페이지에서 원하는 데이터를 수집하는 기술
# 데이터가 필요한 작업 -> 원하는 데이터가 없는 경우(제공X, 다운로드X)
# 웹 크롤링을 사용해서 직접 데이터를 수집

# 웹 크롤링 + 스케줄링 = 자동화

# 외부 라이브러리(다운로드 + import)
# 1. BeautifulSoup4(bs4) 2. Requests 3. Selenium

# 웹 페이지
# - 정적 페이지(bs4 + Requests) : 먼저 시도
# - 동적 페이지(bs4 + Selenium) : 정적 페이지가 안 될때 시도

# conda env list -> basic 확인
# 없으면 : conda create -n basic python = 3.8
# conda activate basic
# pip install requests
# pip install beautifulsoup4
# pip install selenium

# import requests
# import selenium
# from bs4 import BeautifulSoup

# 웹 프로그래밍 기초(속성)
# MVC 패턴

#   - VIEW(사용자 화면) - 프론트 엔드
#   - CONTROLLER - 백 엔드
#   - MODEL(데이터베이스 : 저장) - 백 엔드

# 웹 페이지 화면 구현
# - 웹 표준 : HTML, CSS, Javascript(국제적 표준)
# 1. HTML : 프레임 구현
# 2. CSS : 디자인(색상, 크기, 모양, etc.)
# 3. Javascript : 동적 기능

# HTML 속성
#   <tag></tag> 구현
#   tag 종류 : div, span, a, h4, et cetera..

#   tag 종속관계

#    <div>
#      <span>
#        <span></span>
#      </span>
#      <span></span>
#    </div>

#    div : 부모
#     ㄴ span : 자식
#   종속관계 표현 : 부모 - 자식 관계(div > span : div 태그의 자식 태그인 span)
#                 자손 관계(div span : div 태그 안에 있는 모든 span)

# 선택자
# 1. ID 선택자(#) : 유일한 선택자
# 2. CLASS(.) : 복수 선택자

import requests
from bs4 import BeautifulSoup

url = "https://v.daum.net/v/20231101150230274"  # 수집하고 싶은 웹사이트 주소

# 1. 특정 URL에 접속해서 전체 소스코드를 가져옴
result = requests.get(url)
# status_code -> 200 출력 : 성공, 400, 500번대 출력 : 오류 발생(e.g. error 404 / 505)
print(result)
print(result.text)

# 2. 전체 소스코드(requests)를 bs4로 전달
doc = BeautifulSoup(result.text, "html.parser")

# 3. 원하는 정보 수집
title = doc.select("h3.tit_view")[0].get_text()  # []를 벗김, txt만 가져옴
# select() -> [List type]의 결과를 가져옴
print(f"제목 : {title}")

# 경고 -> Tag 이름으로는 수집 금지
content_list = doc.select("div.article_view p")

content = ""
for p in content_list:
    content += p.get_text()
print(f"본문 : {content}")

# 기사 날짜 수집?
# reg_date = doc.select("")
# print(f"날짜 : {reg_date}")