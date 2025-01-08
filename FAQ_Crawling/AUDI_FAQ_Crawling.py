import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def extract_questions_and_answers(driver):
    """
    질문 옆 버튼을 클릭하고, 답변을 추출하여 질문-답변 쌍을 리스트로 반환

    Args:
        driver: WebDriver 인스턴스

    Returns:
        list: 질문과 답변의 튜플 리스트
    """

    all_question_answer_pairs = []

    # 모든 질문 버튼 찾기
    question_buttons = driver.find_elements(By.CSS_SELECTOR, 'button[aria-controls]')

    for button in question_buttons:
        button.click()

        # 각 질문에 대한 답변을 저장할 리스트 초기화
        question_answer_pairs_for_button = []

        # 답변 컨테이너 찾기 (예: id가 __panel로 끝나는 모든 div 요소)
        answer_containers = driver.find_elements(By.CSS_SELECTOR, "div[id$='__panel']")

        for answer_container in answer_containers:
            # 답변 텍스트 추출
            answer_texts = []
            for p_tag in answer_container.find_elements(By.TAG_NAME, "p"):
                answer_texts.append(p_tag.text.strip())
            answer_text = '\n'.join(answer_texts)

            # 질문 텍스트 추출 (버튼 텍스트 또는 다른 방법으로 추출)
            question_text = button.text.strip()

            # 질문-답변 쌍을 리스트에 추가
            question_answer_pairs_for_button.append((question_text, answer_text))

        # 모든 답변을 추출한 후, 최종 결과에 추가
        all_question_answer_pairs.extend(question_answer_pairs_for_button)

    return all_question_answer_pairs

# 마지막 페이지인지 판단하는 함수
def is_last_page(driver):
    return True  # True 반환

if __name__ == "__main__":
    url = "https://www.audi.co.kr/ko/aboutaudi/customerinfo/wcc/faq/"       # 웹 페이지 URL

    # WebDriver 초기화 (예: Chrome)
    driver = webdriver.Chrome()
    driver.get(url)

    # 질문과 답변 추출
    question_answer_pairs = extract_questions_and_answers(driver)

    # CSV 파일 저장
    with open('audi_faq.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['질문', '답변']
        writer = csv.writer(csvfile)
        writer.writerow(fieldnames)
        writer.writerows(question_answer_pairs)

    # WebDriver 종료
    driver.quit()

    print("데이터가 성공적으로 CSV 파일로 저장되었습니다.")
