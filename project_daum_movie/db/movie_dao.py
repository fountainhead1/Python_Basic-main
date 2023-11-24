from db.common.connection import connection


# 리뷰 데이터 저장 함수


def add_review(data):
    # 1) connection
    conn = connection()

    # DB / file system : 반드시 예외처리 필요함
    try:
        # 2) 일꾼 생성
        curs = conn.cursor()
        # 3) 일거리 생성(SQL) → INSERT, DELETE, UPDATE, SELECT
        sql = """
               INSERT INTO tbl_review(title, review, score, writer, reg_date)
               VALUES(%(title)s, %(review)s, %(score)s, %(writer)s, %(reg_date)s);
              """
        # 4) 작업 시작
        curs.execute(sql, data)
    except Exception as e:
        print(e)
    finally:
        # 5) 자원 반납
        conn.close()