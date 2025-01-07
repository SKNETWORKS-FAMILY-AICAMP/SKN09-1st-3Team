from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pandas as pd
import time 


# 화면에 요소가 보이는지 확인하는 함수
def elem_view(element):
    location = element.location
    size = element.size
    window_size = driver.execute_script("return [window.innerWidth, window.innerHeight]")
                    
    is_in_view = (
        location['x'] >= 0 and location['y'] >= 0 and
        location['x'] + size['width'] <= window_size[0] and
        location['y'] + size['height'] <= window_size[1]
        )
    return is_in_view


# VOLVO FAQ 크롤링 함수

def crawl_faq(driver_path):  # driver_path 인자 추가


    # 드라이버 실행 시 경로 지정
    service = Service(driver_path)
    driver = webdriver.Chrome(service = service)  # driver_path 사용

    

    try:
        # 사이트 접근
        driver.get('https://www.volvocars.com/uk/car-finance/faq/general/')
        time.sleep(1)

        # 쿠키 팝업 해제
        cookie_banner = driver.find_element(By.XPATH, '//*[@id="onetrust-reject-all-handler"]')
        cookie_banner.click()
        time.sleep(1)

        # Q&A 항목 찾기 (각 Q&A 항목의 <details> 태그)
        qna_borders = driver.find_elements(By.XPATH, "//details[@data-testid='faq-list__question']")

        # faq_list 만들기 
        faq_list = []

        # 각 Q&A 항목에 대해 반복
        for qna_border in qna_borders:
            try:
         

                # elem_view 함수로 요소가 화면에 보일 때까지 스크롤
                if not elem_view(qna_border, driver):  # elem_view에 driver 전달
                    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", qna_border)
                    time.sleep(2)  # 스크롤 후 잠시 대기

                # 각 항목 토글 클릭하여 열기
                toggle = qna_border.find_element(By.CSS_SELECTOR, "summary")
                toggle.click()
                time.sleep(1)  # 토글 열기 후 잠시 대기

                # 질문과 답변 가져오기
                question = qna_border.find_element(By.XPATH, ".//summary/span").text
                answer = qna_border.find_element(By.XPATH, ".//div[@class='mb-16']//p").text

                # 질문과 답변 faq_list에 추가
                faq_list.append({'Question': question, 'Answer': answer})

                # 토글 다시 닫기
                toggle.click()
                time.sleep(1)
            except Exception as e:
                print(f"오류 발생: {e}")
                continue

        # faq_list를 데이터프레임으로 변환하여 CSV 파일로 저장
        faq_df = pd.DataFrame(faq_list)
        faq_df.to_csv('VOLVO_FAQ.csv', index=False, encoding='utf-8-sig')
        print(f"FAQ 데이터가 'VOLVO_FAQ.csv'로 저장되었습니다.")
    
    except Exception as e:
        print(f"크롤링 중 오류 발생: {e}")
    finally:
        # 브라우저 종료
        time.sleep(2)
        driver.quit()


