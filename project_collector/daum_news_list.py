# 다음 실시간 뉴스 기사 수집기

# 내용 : 다음 실시간 뉴스 목록(list : 15개)에서 url을 추출 -> 15개의 url
# 각 url별로 기사 제목, 본문, 날짜 수집

import requests  # 전체 소스코드
from bs4 import BeautifulSoup  # 원하는 정보 SELECT
from service.service_news import get_news

count = 0  # 전체 기사 수
url = "https://news.daum.net/breakingnews/digital"
result = requests.get(url)

# url을 잘못 작성하는 경우가 있을 수 있으므로
if result.status_code == 200:
    print(result, "접속 성공 → 데이터를 수집합니다.")

    doc = BeautifulSoup(result.text, "html.parser")
    url_list = doc.select("ul.list_news2 a.link_txt")
    for url in (url_list):
        count += 1
        print(f"{count}.", "=" * 100)
        # get_news() : 기사 제목, 본문, 날짜 수집하는 함수
        get_news(url["href"])
else:
    print("URL 경로가 잘못되었습니다.")

print(result)  # 200이 출력되는지 확인