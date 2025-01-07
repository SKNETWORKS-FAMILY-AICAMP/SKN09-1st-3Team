from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import os
import time
import mimetypes

# Chrome WebDriver 경로 설정
driver_path = "C:\\sk_ai\\web-crawling\\dynamic-web-page\\chromedriver.exe"

# Chrome 옵션 설정
options = webdriver.ChromeOptions()
download_dir = r"C:\sk_ai\1th_Project\crawling"  # 다운로드 디렉토리 설정
prefs = {
    "download.default_directory": download_dir,
    "download.prompt_for_download": False,
    "safebrowsing.enabled": True
}
options.add_experimental_option("prefs", prefs)

# WebDriver 서비스 설정
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=options)

# 다운로드 페이지로 이동
url = "https://www.kaida.co.kr/ko/statistics/kaidaShareList.do"
driver.get(url)

try:
    # 다운로드 버튼 대기 후 클릭
    wait = WebDriverWait(driver, 10)
    download_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "excel_down")))
    download_button.click()

    # 다운로드 완료 대기
    time.sleep(10)  # 다운로드에 소요되는 시간을 감안하여 충분히 기다림

    # 다운로드된 파일 찾기
    files = os.listdir(download_dir)
    downloaded_file = None

    for file in files:
        if file.endswith(".xls") or file.endswith(".xlsx"):
            downloaded_file = os.path.join(download_dir, file)
            break

    if downloaded_file:
        print(f"다운로드된 파일 경로: {downloaded_file}")

        # 파일 타입 확인
        file_type, _ = mimetypes.guess_type(downloaded_file)
        print(f"다운로드된 파일의 타입: {file_type}")
    else:
        print("다운로드된 파일을 찾을 수 없습니다.")

finally:
    # WebDriver 종료
    driver.quit()


# import os
# import time
# import mimetypes
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.service import Service


# def Total_data (driver_path):
#     """
#     Selenium을 이용해 지정된 URL에서 '2024외산차data.csv' 파일을 다운로드합니다.

#     Parameters:
#         driver_path (str): Chrome WebDriver의 경로

#     Returns:
#         str: 다운로드된 파일의 전체 경로 또는 None (다운로드 실패 시)
#     """
#     # 고정된 URL과 파일명
#     url = "https://www.kaida.co.kr/ko/statistics/kaidaShareList.do"
#     file_name = "2024외산차data.csv"

#     # Chrome 옵션 설정
#     options = webdriver.ChromeOptions()
#     prefs = {
#         "download.prompt_for_download": False,
#         "safebrowsing.enabled": True
#     }
#     options.add_experimental_option("prefs", prefs)

#     # WebDriver 서비스 설정
#     service = Service(driver_path)
#     driver = webdriver.Chrome(service=service, options=options)

#     try:
#         # 다운로드 페이지로 이동
#         driver.get(url)

#         # 다운로드 버튼 대기 후 클릭
#         wait = WebDriverWait(driver, 10)
#         download_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "excel_down")))
#         download_button.click()

#         # 다운로드 완료 대기
#         time.sleep(10)  # 다운로드에 소요되는 시간을 감안하여 충분히 기다림

#         # 다운로드된 파일 찾기
#         default_download_dir = os.path.expanduser("~/Downloads")
#         files = os.listdir(default_download_dir)
#         downloaded_file = None

#         for file in files:
#             if file_name in file:  # 파일 이름이 일치하는지 확인
#                 downloaded_file = os.path.join(default_download_dir, file)
#                 break

#         if downloaded_file:
#             print(f"다운로드된 파일 경로: {downloaded_file}")

#             # 파일 타입 확인
#             file_type, _ = mimetypes.guess_type(downloaded_file)
#             print(f"다운로드된 파일의 타입: {file_type}")
#             return downloaded_file
#         else:
#             print("다운로드된 파일을 찾을 수 없습니다.")
#             return None

#     except Exception as e:
#         print(f"오류 발생: {e}")
#         return None

#     finally:
#         # WebDriver 종료
#         driver.quit()


# chrome_driver_path = "C:\\sk_ai\\web-crawling\\dynamic-web-page\\chromedriver.exe"
# Total_data(chrome_driver_path)