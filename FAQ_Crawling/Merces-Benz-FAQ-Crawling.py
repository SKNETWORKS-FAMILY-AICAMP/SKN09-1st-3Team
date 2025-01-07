from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pandas as pd
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

def extract_faq_to_csv(chrome_driver_path):
    """
    메르세데스-벤츠 FAQ 페이지에서 질문과 답변을 추출하여 'faq_list.csv'로 저장하는 함수.
    """
    # Chrome WebDriver 설정
    service = Service(chrome_driver_path)
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
                answer = item.find_element(By.CLASS_NAME, "wb-accordion-content").text

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

    # DataFrame 생성
    df = pd.DataFrame(faq_list)

    # CSV 저장
    output_file = 'faq_list.csv'
    df.to_csv(output_file, index=False, encoding='utf-8-sig')
    print(f"FAQ 데이터가 '{output_file}'로 저장되었습니다.")