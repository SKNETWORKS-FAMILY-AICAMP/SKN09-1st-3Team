from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import os
import time

# URL, 파일 이름, 드라이버 경로 설정
url = "https://www.kaida.co.kr/ko/statistics/NewRegistList.do"
file_name = "statistics_file"
driver_path = "C:/parkjueun/web-crawling/03_dynamic-web-page/chromedriver.exe"

# 다운로드 디렉토리 설정
download_dir = "C:\parkjueun"

# 함수 정의
def download_files(url, driver_path):
    # 다운로드 경로에 폴더가 없으면 생성
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

    # Chrome WebDriver 옵션 설정
    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": download_dir,
        "download.prompt_for_download": False,
        "safebrowsing.enabled": True
    }
    options.add_experimental_option("prefs", prefs)

    # WebDriver 서비스 초기화
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=options)

    try:
        # URL로 이동
        driver.get(url)
        time.sleep(2)  # 페이지 로드 대기
        driver.maximize_window()

        # 연도 리스트 설정
        year_list = [2015, 2017, 2019, 2021, 2023]

        # 필터 컨테이너 찾기
        filter_con = driver.find_element(By.CLASS_NAME, "filter_con")
        
        # 화면에 보이도록 스크롤
        def scroll_into_view(element):
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)

        if not filter_con.is_displayed():
            scroll_into_view(filter_con)
            time.sleep(1)

        # 연도 선택 창
        year_dropdown = driver.find_element(By.ID, "dev_setStartYear")
        select_element = Select(year_dropdown)

        # 연도별로 파일 다운로드
        for year in year_list:
            # 연도 선택
            select_element.select_by_value(str(year))
            time.sleep(1)

            # 검색 버튼 클릭
            search_button = driver.find_element(By.CSS_SELECTOR, ".filter_fire button")
            if not search_button.is_displayed():
                scroll_into_view(search_button)
                time.sleep(1)
            search_button.click()
            time.sleep(5)  # 검색 결과 로드 대기

            # 다운로드 버튼 클릭
            # download_button = WebDriverWait(driver, 10).until(
            #     EC.element_to_be_clickable((By.CLASS_NAME, "excel_down"))
            # )

            # # 다운로드 버튼이 화면에 보일 때까지 스크롤
            # if not download_button.is_displayed():
            #     scroll_into_view(download_button)
            #     time.sleep(1)
            # download_button.click()
            # time.sleep(10)  # 다운로드 완료 대기

            wait = WebDriverWait(driver, 5)
            download_button = wait.until(
                 EC.element_to_be_clickable((By.XPATH, '//*[@id="mainCenter"]/div/article[1]/div/div[1]/button')))
            download_button.click()
            time.sleep(20)  # 다운로드 완료 대기



            # 다운로드 확인
            # files = os.listdir(download_dir)
            # downloaded_file = None
            # for file in files:
            #     if file.startswith(file_name) and (file.endswith(".xls") or file.endswith(".xlsx")):
            #         downloaded_file = os.path.join(download_dir, file)
            #         break

            # if downloaded_file:
            #     print(f"'{downloaded_file}' 저장 성공!")
            # else:
            #     print(f"{year}년 데이터 다운로드 실패.")

    finally:
        # 브라우저 종료
        driver.quit()

# 함수 호출
download_files(url, driver_path)
