# DB에 저장된 수집 데이터를 가져와서 Excel로 저장
#   - List / Dict type(python) → pandas의 DataFrame(표)으로 생성 가능 → Excel, csv로 변환 및 저장 가능(file 형태로 존재)

import pandas as pd
from datetime import datetime
from db.movie_dao import get_reviews

reviews = get_reviews()

# DB에서 가져온 데이터 확인
for item in reviews:
    print(item)

# dict Type의 데이터를 Table 생성
print("=" * 100)
df_save = pd.DataFrame(reviews)
print(df_save)

now = datetime.now().strftime("%Y%m%d")
df_save.to_excel(f"./review_save_{now}.xlsx", index=False)