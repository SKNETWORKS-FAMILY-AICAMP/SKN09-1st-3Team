
import mysql.connector
import pandas as pd
import os
import re

# 처리할 파일 목록 및 경로
file_list = ["LEXUS_FAQ.csv", "BENZ_FAQ.csv", "VOLVO_FAQ.csv"]
upload_path = "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads"       # csv 파일이 포함되어 있는 경로로

try:
    print("MySQL 연결 준비 중...")
    connection = mysql.connector.connect(
        host="localhost",
        user="squirrel",
        password="squirrel",
        database="carregistrationdb"
    )
    if connection.is_connected():
        print("MYSQL에 성공적으로 연결되었습니다.")
    else:
        print("MYSQL 연결에 실패했습니다.")
        exit()  # 연결 실패 시 프로그램 종료
except mysql.connector.Error as e:
    print(f"MYSQL 연결 오류: {e}")
    exit()

cursor = connection.cursor()

# BrandFAQ 테이블에 맞는 SQL 쿼리 (FAQID 제외)
sql = "INSERT INTO BrandFAQ(BrandID, Question, Answer) VALUES (%s, %s, %s)"

for file_name in file_list:
    file_path = os.path.join(upload_path, file_name)
    try:
        print(f"\n{file_name} 파일 읽기 시도...")
        brand_faq = pd.read_csv(file_path, encoding='utf-8')  # utf-8 인코딩 명시
        print(f"{file_name} 파일 읽기 성공")
    except FileNotFoundError:
        print(f"오류: {file_path} 파일을 찾을 수 없습니다. 경로 및 파일명을 확인해주세요.")
        continue  # 다음 파일로 진행
    except pd.errors.ParserError as e:
        print(f"CSV 파일 파싱 오류 ({file_name}): {e}")
        continue
    except Exception as e:
        print(f"파일 읽기 오류 ({file_name}): {e}")
        continue

    try:
        print(brand_faq.head())
        print(brand_faq.info())
        brand_faq = brand_faq[["Question", "Answer"]]
        print("필요한 컬럼 선택 완료")
    except KeyError as e:
        print(f"오류: {file_name} 파일에 필요한 컬럼({e})이 없습니다. 파일의 컬럼명을 확인해주세요.")
        continue

    # 파일 이름에서 BrandID 추출 및 Brand 테이블 조회
    try:
        brand_name = re.match(r"([a-zA-Z]+)_FAQ\.csv", file_name).group(1)
        cursor.execute("SELECT BrandID FROM BrandRegistration WHERE BrandName = %s", (brand_name,))
        result = cursor.fetchone()
        if result:
            brand_id = result[0]
            print(f"BrandName: {brand_name}, BrandID: {brand_id}")
        else:
            print(f"경고: Brand 테이블에 {brand_name}이 존재하지 않습니다. BrandID를 NULL로 설정합니다.")
            brand_id = None  # BrandID를 NULL로 설정
    except AttributeError:
        print(f"오류: {file_name} 파일 이름 형식이 올바르지 않습니다. '[BrandName]_FAQ.csv' 형식을 따라야 합니다.")
        continue
    except Exception as e:
        print(f"BrandID 추출/조회 오류: {e}")
        continue

    # NaN 값을 빈 문자열로 채우기
    brand_faq["Question"] = brand_faq["Question"].fillna("")
    brand_faq["Answer"] = brand_faq["Answer"].fillna("")

    # values 생성 시 FAQID 제외 (핵심 수정 부분)
    values = [(brand_id, row["Question"], row["Answer"]) for index, row in brand_faq.iterrows()]

    try:
        cursor.executemany(sql, values)
        connection.commit()
        print(f"{file_name}: {cursor.rowcount}개의 행을 삽입하였습니다.")

        # 삽입된 데이터의 FAQID 확인
        cursor.execute("SELECT LAST_INSERT_ID();")
        last_id = cursor.fetchone()[0]
        if last_id:
            print(f"마지막으로 삽입된 FAQID: {last_id}")
        else:
            print("삽입된 FAQID를 가져오는데 실패했습니다.")

    except mysql.connector.Error as e:
        connection.rollback()
        print(f"{file_name} 데이터베이스 삽입 오류: {e}")
    except Exception as e:
        connection.rollback()
        print(f"{file_name} 알 수 없는 오류 발생: {e}")

cursor.close()
connection.close()
print("모든 파일 처리 완료")
