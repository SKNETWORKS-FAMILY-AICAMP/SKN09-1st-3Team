## 1. 팀소개

### 팀명: **시기상조** 🚀

- **목표**: 국내의 외산차 등록 현황과 브랜드별 점유율 데이터를 분석하여 시각적으로 제공하고, 2025 외산차 Top 5 브랜드를 예측하여 외산차 트렌드를 파악할 수 있도록 지원합니다.

---

## 팀원 소개 🌟


<p align="center">
  <span>
    🧑‍💻 <b>박주은</b><br>
    <a href="https://github.com/pprain1999">@pprain1999</a><br>
    <img src="https://github.com/user-attachments/assets/67954a06-e180-492e-b7dd-202668a9b09c" alt="박주은" width="100">
  </span>
  &nbsp;&nbsp;&nbsp;&nbsp;
  <span>
    👩‍💻 <b>서예찬</b><br>
    <a href="https://github.com/syc9811">@syc9811</a><br>
    <img src="https://github.com/user-attachments/assets/efd43c51-4666-4dff-83ce-8ff0c6c84b6f" alt="서예찬" width="100">
  </span>
  &nbsp;&nbsp;&nbsp;&nbsp;
  <span>
    👩‍💻 <b>이다인</b><br>
    <a href="https://github.com/daainn">@daainn</a><br>
    <img src="https://github.com/user-attachments/assets/1390df3b-bfc8-44fe-9220-1aa38884492f" alt="이다인" width="100">
  </span>
  &nbsp;&nbsp;&nbsp;&nbsp;
  <span>
    👨‍💻 <b>조민훈</b><br>
    <a href="https://github.com/alche22">@alche22</a><br>
    <img src="https://github.com/user-attachments/assets/34347395-6119-44b0-9031-71d17fb7ac18" alt="조민훈" width="100">
  </span>
  &nbsp;&nbsp;&nbsp;&nbsp;
  <span>
    👩‍💻 <b>조이현</b><br>
    <a href="https://github.com/SIQRIT">@SIQRIT</a><br>
    <img src="https://github.com/user-attachments/assets/b152d0e8-6ae8-476d-a443-37c59199ff27" alt="조이현" width="100">
  </span>
</p>

---

## 2. 프로젝트 개요 🛠️

### **프로젝트명**: 외산차 등록 현황 및 점유율 분석 대시보드

- **소개**:
  1. 🌍 전국 외산차 등록 현황 분석.
    * 과거 10년간의 외산차 등록 데이터 분석 및 시각화.
  2. 🔍 브랜드별 외산차 등록 현황 분석.
    * 과거 10년간의 외산차 등록 데이터 분석 및 시각화.
  3. 🔮 2025년 외산차 기업의 점유율 예측.
  4. 🔮 📋 2025년 TOP 5 외산차 기업 FAQ 조회.
- **목표**:
  - 🚙 외산차 등록 현황 시각화 자료를 사용자에게 제공.
  - 📊 외산차 시장 점유율 분석 및 기업 트렌드 파악.
  - 📝 기업별 FAQ 검색 조회 기능을 사용자에게 제공.
- **배경**:
  - 🚙 시장 변화와 관심 증가
      * 최근 국내 자동차 시장에서 외산차의 점유율이 꾸준히 증가하며, 브랜드 간의 경쟁이 치열해지고 있는 상황.
      * 이러한 변화 속에서 외산차 시장의 흐름과 주요 브랜드의 동향을 파악하고, 데이터를 통해 인사이트를 제공하기 위해 본 프로젝트를 기획.

---

## 3. 기술스택 🖥️

| **분류**          | **기술/도구**                                                                 |
|-------------------|------------------------------------------------------------------------------|
| **언어**          |![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)                                                        |
| **라이브러리**    | ![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)![Pandas](https://img.shields.io/badge/pandas-150458.svg?style=for-the-badge&logo=pandas&logoColor=white)![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black) ![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)            |
| **데이터베이스**   | ![MySQL](https://img.shields.io/badge/mysql-4479A1.svg?style=for-the-badge&logo=mysql&logoColor=white)                                                           |
| **WEB**        | ![Streamlit](https://img.shields.io/badge/Streamlit-%23FE4B4B.svg?style=for-the-badge&logo=streamlit&logoColor=white)                                               |
| **협업 툴**       | ![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)![Notion](https://img.shields.io/badge/Notion-%23000000.svg?style=for-the-badge&logo=notion&logoColor=white)                                                   |
---

## 4. WBS 🗂️

![image](https://github.com/user-attachments/assets/eb10283c-7d58-4f14-bc8b-1a5a31c6f083)


---

## 5. 요구사항 명세서 📜

### **핵심 요구사항**

| **RQ_ID**  | **기능유형** | **요구사항 설명**               | **요구사항 내용**                                       |
| ---------- | ------------ | ----------------------------- | ----------------------------------------------------- |
| **RQ_001** | 기능         | 전국 외산차 등록 현황 조회 기능    | 사용자가 전국 외산차 및 국산차 등록 현황을 년도별로 조회할 수 있어야 함.        |
| **RQ_002** | 기능         | 과거 10년간 등록 데이터 분석     | 2014-2023년 외산차 등록 현황 및 시장 점유율 변화를 분석하고 사용자가 볼 수 있도록 시각화.   |
| **RQ_003** | 기능         | 외산차 브랜드별 점유율 분석 기능 | 사용자가 주요 외산차 기업의 시장 점유율 및 등록현황을 조회할 수 있어야 함.   |
| **RQ_004** | 기능         | 과거 10년간 등록 데이터 분석     | 2014-2023년 외산차 브랜드별 등록 현황 및 시장 점유율 변화를 분석하고 사용자가 볼 수 있도록 시각화.   |
| **RQ_005** | 기능         | 2025년 점유율 예측 기능          | 과거 10년의 데이터를 기반으로 2025년 외산차 점유율을 선형회귀로 예측하여 사용자에게 시각화 자료 제공.     |
| **RQ_006** | 기능         | FAQ 조회                        | 사용자가 2025 예측 TOP 5브랜드의 FAQ를 조회 및 검색할 수 있어야 함.        |

## 6. ERD 🗺️

### **데이터 구조**
![image](https://github.com/user-attachments/assets/a5a66af1-18a9-4740-a4df-e436f806c331)

---

## 7. 프로젝트 시연 페이지 📺

### **Streamlit 데모 페이지**

1. 🌍 **년도별 전국 외산차 등록현황 조회**
     ![image](https://github.com/user-attachments/assets/ff7d67a2-8910-498b-80a0-78e219ed9759)
   - 사용자가 연도별로 외산차 및 국산차 등록 현황을 선택하여 조회할 수 있음.
     ![image](https://github.com/user-attachments/assets/7c40a5a0-8ada-4fd5-a4b8-3badfa2feaef)
     ![image](https://github.com/user-attachments/assets/17b46cf7-b665-486d-99df-03370881980d)
   - 등록현황 변화 시각화 자료 제공.

2. 🔍 **브랜드별 외산차 등록현황 및 점유율 분석**
     ![image](https://github.com/user-attachments/assets/df2d48c3-0886-4809-b386-4ad61f680dea)
   - 10년간 연도별, 브랜드별 외산차 등록현황과 점유율을 조회할 수 있음
     ![image](https://github.com/user-attachments/assets/d7674f80-94b9-4d12-9b25-682936ed0fdf)
     ![image](https://github.com/user-attachments/assets/957081f6-7daf-4752-b68e-a39f53675b41)
   - 관련 시각화 자료 제공

3. 📝 **2025 외산차 브랜드 점유율 예측**
     ![image](https://github.com/user-attachments/assets/3bf2c287-4046-43eb-b90a-7a603f014ce7)
   - 선형회귀 모델을 기반으로 2025년 브랜드별 외산차 점유율을 예측하여 제공
     ![image](https://github.com/user-attachments/assets/c23e0109-55c5-4e35-ad0f-6970cdd864a9)
     ![image](https://github.com/user-attachments/assets/b2afecce-afe9-4bb8-a9e7-cd617112c87a)
   - 예측 결과에 대한 시각화 자료 제공

4. 📋 **2025 TOP 5 외산차 기업 FAQ 조회**
   ![image](https://github.com/user-attachments/assets/14305dd0-4501-4b28-9a42-980d67f7346c)
   - FAQ 조회 기능 확인 가능.

---

## 8. 팀원 한 줄 회고 🌈

- **박주은**: "웹크롤링으로 가져온 데이터를 활용하는 프로그램을 구성할 때, 데이터를 가져오는 과정을 단순화하는 것뿐만 아니라 비정기적으로 웹의 데이터가 변화할 것도 고려해 프로그램이 매번 적절한 데이터를 활용할 수 있도록 하는 것이 중요하다는 것을 구체적으로 깨닫게 되었다." ✨
- **서예찬**: "이틀안에 하는 기획부터 발표까지 하는 프로젝트인데다가 처음으로 하는 프로젝트이다보니 열심히해야겠다고 생각했는데 프로젝트 기간동안 독감에 걸려 많이 참여하지 못해 팀원들에게 많이 미안하다." 🧑‍🔬
- **이다인**: "프로젝트 진행 중 mysql.connector과 streamlit 라이브러리를 사용하며 import 순서로 인한 충돌이 발생했습니다. mysql.connector가 제대로 작동하지 않거나, streamlit 구동 중 라이브러리 충돌로 실행이 멈추는 문제가 있었는데, import 순서를 조정하거나, 라이브러리를 주석 처리하여 테스트하는 방식으로 원인을 찾아 해결했습니다. 또한, 같은 코드를 다른 폴더에서 실행했을 때 정상 작동하는 경우를 통해 폴더명과 환경 설정도 디버깅의 중요한 요소임을 배웠습니다." 🎯 🎯
- **조민훈**: "사이트마다 설계구조가 다르기때문에 원활한 웹크롤링을 위해서는 구조에 대한 정확한 이해가 필요하다는 점을 실감했다. " 🎨
- **조이현**: "실전에서 부딪히면서 고생을 많이 했습니다. 그렇지만 다른 팀원들의 든든한 협력이 있어서 많이 배웠다고 생각합니다." 🤝
