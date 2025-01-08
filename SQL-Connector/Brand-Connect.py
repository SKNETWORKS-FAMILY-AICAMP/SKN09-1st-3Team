import mysql.connector
import pandas as pd
from functools import reduce

# 테이블 구조
# CREATE TABLE BrandRegistration (
#     BrandID INT,
#     BrandName VARCHAR(255) NOT NULL,
#     YearID YEAR, -- YEAR 타입으로 변경
#     Registrations INT NOT NULL,
#     MarketShare FLOAT NOT NULL,
#     PRIMARY KEY (BrandID, YearID),
#     FOREIGN KEY (BrandID) REFERENCES BrandInfo(BrandID),
#     FOREIGN KEY (YearID) REFERENCES DomesticCarRegistration(YearID)
# );

# 파일 불러오기
df_1514 = pd.read_excel("20142015.xlsx", skiprows=5)
df_1514.drop(df_1514.columns[[0,2,3,4,5,6,7,8,9,14]], axis=1, inplace=True)
df_1514.columns = ["브랜드명", "2015등록대수", "2015점유율", "2014등록대수", "2014점유율"]

df_1716 = pd.read_excel("20162017.xlsx", skiprows=5)
df_1716.drop(df_1716.columns[[0,2,3,4,5,6,7,8,9,14]], axis=1, inplace=True)
df_1716.columns = ["브랜드명", "2017등록대수", "2017점유율", "2016등록대수", "2016점유율"]

df_1918 = pd.read_excel("20182019.xlsx", skiprows=5)
df_1918.drop(df_1918.columns[[0,2,3,4,5,6,7,8,9,14]], axis=1, inplace=True)
df_1918.columns = ["브랜드명", "2019등록대수", "2019점유율", "2018등록대수", "2018점유율"]

df_2120 = pd.read_excel("20202021.xlsx", skiprows=5)
df_2120.drop(df_2120.columns[[0,2,3,4,5,6,7,8,9,14]], axis=1, inplace=True)
df_2120.columns = ["브랜드명", "2021등록대수", "2021점유율", "2020등록대수", "2020점유율"]

df_2322 = pd.read_excel("20222023.xlsx", skiprows=5)
df_2322.drop(df_2322.columns[[0,2,3,4,5,6,7,8,9,14]], axis=1, inplace=True)
df_2322.columns = ["브랜드명", "2023등록대수", "2023점유율", "2022등록대수", "2022점유율"]

df_2024 = pd.read_excel("20232024.xlsx", skiprows=5)
df_2024.drop(df_2024.columns[[0,2,3,4,5,6,7,8,9,12,13,14]], axis=1, inplace=True)
df_2024.columns = ["브랜드명", "2024등록대수", "2024점유율"]

dataframes = [df_1514, df_1716, df_1918, df_2120, df_2322, df_2024]
merged_df = reduce(lambda left, right: pd.merge(left, right, on="브랜드명"), dataframes)

# print(merged_df.columns)

# 데이터 정제
# 1. 데이터 int형으로 변환환
registration_columns = ['2014등록대수', '2015등록대수', '2016등록대수', '2017등록대수', '2018등록대수', '2019등록대수', 
                        '2020등록대수', '2021등록대수', '2022등록대수', '2023등록대수', '2024등록대수']

for col in registration_columns:
    merged_df[col] = merged_df[col].replace({',': ''}, regex=True).astype(int)

# 2. 데이터 순서대로 정렬
brand_column = ['브랜드명']
metric_columns = [col for col in merged_df.columns if col != '브랜드명']

metric_columns = [col for col in metric_columns if col[:4].isdigit()]

sorted_columns = sorted(
    metric_columns,
    key=lambda x: (int(x[:4]), '등록대수' not in x) 
)
final_columns = brand_column + sorted_columns
merged_df = merged_df[final_columns]

# print(merged_df.columns)
# print(merged_df.info())

# CONNECTION 생성
connection = mysql.connector.connect(
    host = "localhost",
    user = "squirrel",
    password = "squirrel",
    database = "CarRegistrationDB"
)

# CONNECTION 생성
connection = mysql.connector.connect(
    host="localhost",
    user="squirrel",
    password="squirrel",
    database="CarRegistrationDB"
)

if connection.is_connected():
    print(f"MYSQL에 성공적으로 연결되었습니다.")

cursor = connection.cursor()

# 브랜드명 데이터 삽입 (BrandInfo 테이블)
for index, row in merged_df.iterrows():
    brand_name = row['브랜드명']
    
    # BrandInfo 테이블에 브랜드명이 없으면 삽입
    cursor.execute("SELECT BrandID FROM BrandInfo WHERE BrandName = %s", (brand_name,))
    brand_id = cursor.fetchone()
    
    if not brand_id:
        # 브랜드명 삽입
        cursor.execute("INSERT INTO BrandInfo (BrandName) VALUES (%s)", (brand_name,))
        connection.commit()  # 삽입 후 커밋하여 BrandID가 생성되도록 함
        
        # 삽입된 후 자동 생성된 BrandID 조회
        cursor.execute("SELECT LAST_INSERT_ID()")
        brand_id = cursor.fetchone()[0]  # 마지막 삽입된 BrandID를 가져옴
    else:
        brand_id = brand_id[0]  # 이미 존재하는 경우 BrandID 사용
    
    # 연도별 등록대수 및 점유율 삽입 (2014부터 2024까지)
    for year in range(2014, 2025):
        registrations_col = f'{year}등록대수'
        market_share_col = f'{year}점유율'

        # 등록대수와 점유율 값을 가져옴
        registrations = row[registrations_col]
        market_share = row[market_share_col]
        
        # BrandRegistration 테이블에 데이터 삽입
        insert_query = """
        INSERT INTO BrandRegistration (BrandID, BrandName, YearID, Registrations, MarketShare)
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(insert_query, (brand_id, brand_name, year, registrations, market_share))

# 커밋하여 변경 사항 저장
connection.commit()

# 종료 처리
cursor.close()
connection.close()