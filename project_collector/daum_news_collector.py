# Daum News Collector ver 1.0
# 사용자가 수집하고 싶은 뉴스 카테고리를 설정하면 해당 카테고리의 실시간 뉴스 기사와 제목을 수집하는 프로그램
# 작성일자 : 2023-11-08
# 작성자 : 한준수
# 라이브러리 : requests, BeautifulSoup4, pymongo

# 프로세스
# 1) 사용자로부터 뉴스 카테고리를 입력받음 -> input()
# 2) 해당 카테고리의 실시간 다음 뉴스를 수집(제목, 본문)
# 3) 수집한 기사를 데이터베이스(MongoDB)에 저장

import requests
from bs4 import BeautifulSoup
from service.service_news import get_news

count = 0
page = 1

print("=" * 150)
print("= 수집하고 싶은 뉴스 카테고리를 입력해주세요")
print("= 뉴스 카테고리 목록")
print("= 1. 사회")
print("= 2. 정치")
print("= 3. 경제")
print("= 4. 국제")
print("= 5. 문화")
print("= 6. 연예")
print("= 7. 스포츠")
print("= 8. IT")

dict_news = {
    "사회" : "society", "정치" : "politics", "경제" : "economic", "국제" : "foreign", "문화" : "culture", "연예" : "entertain", "스포츠" : "sports", "IT" : "digital"
}
while True:
    category = input("= > 카테고리 : ")
    if category in list(dict_news.keys()):
        break
    else:
        print("= MSG : 올바른 카테고리를 입력하세요.")


while True:
    url = f"https://news.daum.net/breakingnews/{dict_news[category]}?page={page}"
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