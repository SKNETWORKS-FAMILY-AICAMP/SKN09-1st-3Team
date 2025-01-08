import mysql.connector
import pandas as pd

# 테이블 구조
# CREATE TABLE DomesticCarRegistration (
#     YearID YEAR, 
#     TotalRegistrations INT NOT NULL,
#     PRIMARY KEY (YearID)
# );

# total_2024_car는 월 합산 값이 마지막 행에 total로 들어가 있음 => total을 2024로 바꾸고 컬럼 값을 YearID로로
total_2024_car = pd.read_excel("total_2024.xlsx", skiprows=17)
total_2024_car.drop(total_2024_car.columns[[0,2,3,5,6]], axis=1, inplace=True)
total_2024_car.columns = ["YearID",  "TotalRegistrations"]
total_2024_car["YearID"] = 2024
total_2024_car['TotalRegistrations'] = total_2024_car['TotalRegistrations'].replace({',': ''}, regex=True).astype(int)

total_past_car = pd.read_excel("total_past.xlsx", skiprows=32)
total_past_car.drop(total_past_car.columns[[0,2,3,5,6,7]], axis=1, inplace=True)
total_past_car.columns = ["YearID",  "TotalRegistrations"]
total_past_car['TotalRegistrations'] = total_past_car['TotalRegistrations'].replace({',': ''}, regex=True).astype(int)
print(total_2024_car.head())
print(total_past_car.head())



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
except mysql.connector.Error as e:
    print(f"MYSQL 연결 오류: {e}")
    exit()


cursor = connection.cursor()

# % 는 place holder라고 해서 값이 들어갈 자리를 비워두는 것
values_past = total_past_car[["YearID", "TotalRegistrations"]].values.tolist()
values_2024 = total_2024_car[["YearID", "TotalRegistrations"]].values.tolist()

sql = "INSERT INTO DomesticCarRegistration(YearID, TotalRegistrations) VALUES (%s,%s)"
cursor.executemany(sql, values_past)  # 여러 행 삽입
print(f"{cursor.rowcount}개의 행을 삽입하였습니다 (과거 데이터).")
cursor.executemany(sql, values_2024)  # 여러 행 삽입
print(f"{cursor.rowcount}개의 행을 삽입하였습니다 (2024 데이터).")

connection.commit()

print(f"{cursor.rowcount}개의 행을 삽입하였습니다.")

cursor.close()
connection.close()



