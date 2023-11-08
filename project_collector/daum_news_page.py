import requests
from bs4 import BeautifulSoup
from service.service_news import get_news

count = 0
page = 1  # 시작 페이지 1로 고정

while True:
    url = f"https://news.daum.net/breakingnews/digital?page={page}"
    result = requests.get(url)

    if result.status_code == 200:
        print(result, "접속 성공 → 데이터를 수집합니다.")

        doc = BeautifulSoup(result.text, "html.parser")
        url_list = doc.select("ul.list_news2 a.link_txt")

        # print(f"{page}페이지의 기사 갯수 : {len(url_list)}")

        if len(url_list) == 0:
            break
        for url in (url_list):
           count += 1
           print(f"{count}.", "=" * 100)
           get_news(url["href"])
    else:
        print("URL 경로가 잘못되었습니다.")

    page += 1

    print(result)