from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import requests

# Selenium WebDriver 설정
driver_path = "chromedriver"  # ChromeDriver 경로 설정
url = "https://auto.danawa.com/auto/"

# 저장 폴더
output_folder = "images"
os.makedirs(output_folder, exist_ok=True)

# 관심 브랜드 목록
brands = ["아우디", "BMW", "벤틀리", "캐딜락", "포드", "혼다", "재규어",
          "람보르기니", "랜드로버", "렉서스", "미니", "벤츠", "푸조",
          "포르쉐", "롤스로이스", "토요타", "폭스바겐", "볼보"]

# Selenium WebDriver 시작


driver = webdriver.Chrome()
driver.get(url)

# 페이지 로드 대기
time.sleep(5)

# 이미지 필터링 및 다운로드
try:
    # 새로운 CSS 셀렉터 사용
    images = driver.find_elements(By.CSS_SELECTOR, "#autodanawa_gridC > div.gridMain > article > main > dl > div.import > ul img")
    
    for img in images:
        # 이미지 URL과 브랜드 이름 추출
        img_url = img.get_attribute("src")
        alt_text = img.get_attribute("alt")  # 이미지의 alt 속성에서 브랜드명 추출
        
        if not img_url or not alt_text:
            continue
        
        # 지정된 브랜드가 alt 텍스트에 포함된 경우만 다운로드
        if any(brand in alt_text for brand in brands):
            if not img_url.startswith("http"):
                img_url = f"https:{img_url}"
            
            # 이미지 저장
            img_name = os.path.join(output_folder, f"{alt_text}_{os.path.basename(img_url)}")
            response = requests.get(img_url)
            if response.status_code == 200:
                with open(img_name, "wb") as file:
                    file.write(response.content)
                print(f"Downloaded: {img_name}")
            else:
                print(f"Failed to download: {img_url}")

finally:
    driver.quit()
