import os
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def fetch_faq_data(chrome_driver_path):
    # 현재 작업 디렉토리로 저장 경로 설정
    output_csv_path = os.path.join(os.getcwd(), "LEXUS_FAQ.csv")

    # 크롬 드라이버 설정
    chrome_options = Options()
    chrome_options.add_argument("--ignore-certificate-errors")
    service = Service(executable_path=chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # URL 접속
    driver.get("https://www.lexus.ca/lexus/en/faq")
    time.sleep(1)

    # FAQ 데이터 리스트
    faq_data = []

    # 각 문단의 XPath 패턴
    section_xpath_pattern = '//*[@id="faq-content-viewer"]/div[{section_index}]/ul/li'

    # 문단 순회 (1~4번 문단이라 가정)
    for section_index in range(1, 5):
        try:
            # 문단의 모든 토글 버튼 가져오기
            section_toggle_xpath = section_xpath_pattern.format(section_index=section_index) + '/span'
            toggle_buttons = driver.find_elements(By.XPATH, section_toggle_xpath)
            print(f"Section {section_index}: toggle buttons found:", len(toggle_buttons))

            # 각 토글 버튼 클릭 후 질문/답변 크롤링
            for idx, button in enumerate(toggle_buttons):
                try:
                    # 버튼 클릭
                    ActionChains(driver).move_to_element(button).click().perform()
                    time.sleep(3)  # 클릭 후 로드 대기

                    # 해당 토글 안의 질문 요소 찾기
                    questions_xpath = section_xpath_pattern.format(section_index=section_index) + f'[{idx+1}]/div'
                    questions = driver.find_elements(By.XPATH, questions_xpath)

                    for question in questions:
                        try:
                            # 질문 텍스트
                            question_text = question.find_element(By.XPATH, './/p[1]').text.strip()

                            # 답변 텍스트 수집
                            answer_paragraphs = question.find_elements(By.XPATH, './/p')  # 모든 p 태그 찾기
                            answer_lists = question.find_elements(By.XPATH, './/ul')  # 모든 ul 태그 찾기

                            # 답변을 합치기
                            answer_text = ""
                            for p in answer_paragraphs:
                                if p.text.strip() != question_text:
                                    answer_text += p.text + "\n"

                            for ul in answer_lists:
                                list_items = ul.find_elements(By.TAG_NAME, 'li')  # ul 내의 li 태그 찾기
                                for li in list_items:
                                    answer_text += "- " + li.text + "\n"

                            # 데이터 저장
                            faq_data.append({'Question': question_text, 'Answer': answer_text.strip()})
                        except Exception as e:
                            print(f"Error with question in section {section_index}, toggle {idx+1}: {e}")
                except Exception as e:
                    print(f"Error with toggle {idx+1} click in section {section_index}: {e}")
        except Exception as e:
            print(f"Error with section {section_index}: {e}")

    # 결과를 DataFrame으로 저장 후 CSV 파일로 저장
    faq_df = pd.DataFrame(faq_data)
    faq_df.to_csv(output_csv_path, index=False, encoding='utf-8-sig')

    print(f"FAQ data has been saved to '{output_csv_path}'.")

    # 브라우저 종료
    driver.quit()