from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Chrome WebDriver 설정

 # ChromeDriver 경로 설정
driver = webdriver.Chrome()

try:
    # URL 열기
    url = "https://shop.mercedes-benz.com/ko-kr/connect/service/faq"
    driver.get(url)
    time.sleep(5)  # 페이지 로드 대기

    # FAQ 항목 확장 (모든 버튼 클릭)
    faq_buttons = driver.find_elements(By.CSS_SELECTOR, "button.wb-accordion__toggle")
    for button in faq_buttons:
        driver.execute_script("arguments[0].click();", button)
        time.sleep(0.5)  # 각 버튼 클릭 후 대기

    # 확장된 FAQ 항목에서 질문과 답변 추출
    faq_items = driver.find_elements(By.CLASS_NAME, "dcp-faq-service-page__accordion")

    faq_list = []
    for item in faq_items:
        try:
            # 질문 텍스트 추출
            question = item.find_element(By.CLASS_NAME, "wb-accordion__toggle-inner").text

            # 답변 텍스트 추출
            answer = item.find_element(By.TAG_NAME, "wb-accordion-content").text

            faq_list.append({'질문': question.strip(), '답변': answer.strip()})
        except Exception as e:
            print(f"Error processing item: {e}")

    # FAQ 출력
    for idx, faq in enumerate(faq_list, start=1):
        print(f"FAQ {idx}")
        print(f"질문: {faq['질문']}")
        print(f"답변: {faq['답변']}")
        print("-" * 50)

finally:
    # WebDriver 종료
    driver.quit()
                import pandas as pd

# DataFrame 생성
df = pd.DataFrame(faq_list)

# CSV 저장
df.to_csv('faq_list.csv', index=False, encoding='utf-8-sig')