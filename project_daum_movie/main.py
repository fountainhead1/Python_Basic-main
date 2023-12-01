# TODO : 1. 스케줄링 작업 / 2. 리뷰 수집시 중복 체크(중복인 경우 수집 않도록)
#        3. 데이터베이스에 수집된 데이터 → Excel 저장 / 4. 데이터베이스에 수집된 데이터 → 간단한 텍스트 분석
#        5. 데이터베이스에 수집된 데이터 → WorldCloud 시각화
# TIP : 이모티콘으로 작성된 리뷰 : 어떤 형식인지 확인 후 정규식으로 제거

from collect.collect_daum_movie_review import review_collector
from db.movie_dao import get_last_review

def main():
    print("="*100)
    print("== 영화리뷰수집기 ==")
    print("="*100)
    movie_code = input("영화 코드>> ") #  e.g.) 169328(나폴레옹)
    print("MSG: 매일 12시간에 수집")

    last_date = get_last_review()
    print(last_date)
    exit()

    # last_date : DB에 저장된 마지막 리뷰 날짜
    review_collector(movie_code, last_date)

if __name__ == "__main__":
    main()