import mysql.connector
import pandas as pd
from functools import reduce

# MySQL 데이터베이스 연결
conn = mysql.connector.connect(
    host="localhost",      # 호스트 이름
    user="root",           # 사용자 이름
    password="7276",  # 비밀번호
    database='carregistrationdb'   # 데이터베이스 이름

)

cursor = conn.cursor()


# INSERT 문 실행
insert_query = """
INSERT INTO brandinfo (BrandID, BrandName) 
VALUES 
    (NULL, 'BMW'),
    (NULL, '람보르기니'),
    (NULL, '랜드로버'),
    (NULL, '렉서스'),
    (NULL, '롤스로이스'),
    (NULL, '미니'),
    (NULL, '벤츠'),
    (NULL, '벤틀리'),
    (NULL, '볼보'),
    (NULL, '아우디'),
    (NULL, '재규어'),
    (NULL, '캐딜락'),
    (NULL, '토요타'),
    (NULL, '포드'),
    (NULL, '포르쉐'),
    (NULL, '폭스바겐'),
    (NULL, '푸조'),
    (NULL, '혼다');
"""
cursor.execute(insert_query)
conn.commit()

# DELETE 문 실행
delete_query = "DELETE FROM brandinfo WHERE BrandID > 18;"
cursor.execute(delete_query)
conn.commit()

# UPDATE 문 실행
update_queries = [
    ("BMW", "C:\\\\easy\\\\web-crawling\\\\images\\\\BMW_362_90.png"),
    ("람보르기니", "C:\\\\easy\\\\web-crawling\\\\images\\\\람보르기니_440_90.png"),
    ("랜드로버", "C:\\\\easy\\\\web-crawling\\\\images\\\\랜드로버_399_90.png"),
    ("렉서스", "C:\\\\easy\\\\web-crawling\\\\images\\\\렉서스_486_90.png"),
    ("롤스로이스", "C:\\\\easy\\\\web-crawling\\\\images\\\\롤스로이스_385_90.png"),
    ("미니", "C:\\\\easy\\\\web-crawling\\\\images\\\\MINI_367_90.png"),
    ("벤츠", "C:\\\\easy\\\\web-crawling\\\\images\\\\벤츠_349_90.png"),
    ("벤틀리", "C:\\\\easy\\\\web-crawling\\\\images\\\\벤틀리_390_90.png"),
    ("볼보", "C:\\\\easy\\\\web-crawling\\\\images\\\\볼보_459_90.png"),
    ("아우디", "C:\\\\easy\\\\web-crawling\\\\images\\\\아우디_371_90.png"),
    ("재규어", "C:\\\\easy\\\\web-crawling\\\\images\\\\재규어_394_90.png"),
    ("캐딜락", "C:\\\\easy\\\\web-crawling\\\\images\\\\캐딜락_546_90.png"),
    ("토요타", "C:\\\\easy\\\\web-crawling\\\\images\\\\토요타_491_90.png"),
    ("포드", "C:\\\\easy\\\\web-crawling\\\\images\\\\포드_569_90.png"),
    ("포르쉐", "C:\\\\easy\\\\web-crawling\\\\images\\\\포르쉐_381_90.png"),
    ("폭스바겐", "C:\\\\easy\\\\web-crawling\\\\images\\\\폭스바겐_376_90.png"),
    ("푸조", "C:\\\\easy\\\\web-crawling\\\\images\\\\푸조_413_90.png"),
    ("혼다", "C:\\\\easy\\\\web-crawling\\\\images\\\\혼다_500_90.png"),
]

for brand_name, logo_path in update_queries:
    update_query = f"""
    UPDATE brandinfo
    SET BrandLogo = '{logo_path}'
    WHERE BrandName = '{brand_name}';
    """
    cursor.execute(update_query)

conn.commit()

# SELECT 문 실행
cursor.execute("SELECT BrandName, BrandLogo FROM brandinfo;")
results = cursor.fetchall()

# 결과 출력
for row in results:
    print(row)

# 연결 종료
cursor.close()
conn.close()
