from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import os
import time
import mimetypes

# Chrome WebDriver 경로 설정
driver_path = "C:\\easy\\web-crawling\\03_dynamic-web-page\\chromedriver.exe"

# Chrome 옵션 설정
options = webdriver.ChromeOptions()
download_dir = "C:\\web-crawling\\downloads"  # 다운로드 디렉토리 설정
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
# url = input('url을 입력하시오:')
driver.get(url)

try:
    # # 연도별 점유율 버튼 대기 후 클릭
    # wait = WebDriverWait(driver, 10)
    # yearly_share_button = wait.until(EC.element_to_be_clickable((By.ID, "searchConditionBtn1")))
    # yearly_share_button.click()
    wait = WebDriverWait(driver, 5)
    yearly_share_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#dev_vertical > label:nth-child(2) > span")))
    yearly_share_button.click()
    
    # # 검색하기 버튼 대기 후 클릭
    # search_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn_search")))
    # search_button.click()
    wait = WebDriverWait(driver, 5)
    search_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#mainCenter > article.body_wrap > div > form > div.filter_fire > button")))
    search_button.click()
    # 다운로드 버튼 대기 후 클릭
    wait = WebDriverWait(driver, 5)
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
