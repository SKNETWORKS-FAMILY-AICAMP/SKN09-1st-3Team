import mysql.connector
import pandas as pd

# MySQL 연결
def create_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="squirrel",
        password="squirrel",
        database="carregistrationdb"
    )
    return connection

# 데이터 조회: DomesticCarRegistration
def get_domestic_data(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT YearID, TotalRegistrations FROM DomesticCarRegistration")
    result = cursor.fetchall()
    columns = ["YearID", "TotalRegistrations"]
    df_domestic = pd.DataFrame(result, columns=columns)
    cursor.close()
    print("--------------")
    print(df_domestic)
    return df_domestic

# 데이터 조회: BrandRegistration
def get_brand_registration_data(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT BrandID, BrandName, YearID, Registrations, MarketShare FROM BrandRegistration")
    result = cursor.fetchall()
    columns = ["BrandID", "BrandName", "YearID", "Registrations", "MarketShare"]
    df_registration = pd.DataFrame(result, columns=columns)
    cursor.close()
    print(df_registration)
    return df_registration

# 데이터 조회: (BrandInfo 관련, 주석처리)
# def get_brand_info(connection):
#     cursor = connection.cursor()
#     cursor.execute("SELECT BrandID, BrandName FROM BrandInfo")
#     result = cursor.fetchall()
#     columns = ["BrandID", "BrandName"]
#     df_brand_info = pd.DataFrame(result, columns=columns)
#     cursor.close()
#     return df_brand_info

# 연결하고 함수 호출 예시
def main():
    connection = create_connection()

    if connection.is_connected():
        print(f"MYSQL에 성공적으로 연결되었습니다.")
    
    df_domestic = get_domestic_data(connection)
    df_registration = get_brand_registration_data(connection)
    
    # 주석처리된 부분은 필요에 따라 호출
    # df_brand_info = get_brand_info(connection)

    # 결과 출력 (예시)
    print(df_domestic.head())
    print(df_registration.head())

    # 연결 종료
    connection.close()

if __name__ == "__main__":
    main()
