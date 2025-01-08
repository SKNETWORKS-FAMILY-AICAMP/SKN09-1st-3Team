from modules.data_select import get_domestic_data, get_brand_registration_data, create_connection
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.font_manager as fm
import streamlit as st
from sklearn.linear_model import LinearRegression
import numpy as np

## -------------matplotlib font설정 및 테마 설정----------------
sns.set_theme(style="whitegrid")

# 격자선 색을 연한 색으로 설정
plt.rcParams["grid.color"] = "#fff0f5"
# sns.set_theme(style="darkgrid", rc={"axes.facecolor": "lightgrey"})
# warnings.filterwarnings("ignore", category=UserWarning, module="matplotlib")
# warnings.filterwarnings("ignore", category=FutureWarning, module="seaborn")

font_path = "C:\\Users\\Playdata\\AppData\\Local\\Microsoft\\Windows\\Fonts\\Pretendard-Regular.otf"
font_name = fm.FontProperties(fname=font_path).get_name()
plt.rc('font', family=font_name)

# plt.rcParams['axes.unicode_minus'] = False



@st.cache_resource
def get_connection():
    return create_connection()

@st.cache_data
def load_domestic_data():
    connection = get_connection()
    return get_domestic_data(connection)

@st.cache_data
def load_brand_registration_data():
    connection = get_connection()
    return get_brand_registration_data(connection)
#------------------제목-------------------

# 제목
st.markdown("""
    <div style="background-color: #fffafa; padding: 10px; border-radius: 3px; margin-bottom: 10px;">
        <h1 style="color: black; font-size: 3x; text-align: center;">🚗 브랜드별 외산차 등록현황</h1>
    </div>
""", unsafe_allow_html=True)

# 구분선
st.markdown("""
    <hr style="border: none; border-top: 0.1px solid #454876; margin-top: 20px; margin-bottom: 40px;">
""", unsafe_allow_html=True)
#--------------------------------------------
# # 데이터 로딩
brand_registration_data = load_brand_registration_data()


brand_options = ['전체'] + brand_registration_data['BrandName'].unique().tolist()
year_options = ['전체'] + brand_registration_data['YearID'].unique().astype(str).tolist()

# 선택 옵션 UI
selected_brand = st.selectbox("브랜드 선택", brand_options)
selected_year = st.selectbox("연도 선택", year_options)

# 브랜드와 연도를 선택했을 때 데이터를 필터링
if selected_brand != '전체':
    brand_registration_data = brand_registration_data[brand_registration_data['BrandName'] == selected_brand]

if selected_year != '전체':
    brand_registration_data = brand_registration_data[brand_registration_data['YearID'] == int(selected_year)]



# 선택된 필터에 맞는 데이터를 화면에 표시
st.dataframe(brand_registration_data, use_container_width=True)
st.markdown("""
    <hr style="border: none; border-top: 0.1px solid #454876; margin-top: 20px; margin-bottom: 40px;">
""", unsafe_allow_html=True)


# ---------------------------------------------------

if brand_registration_data.empty:
    st.warning("선택된 조건에 맞는 데이터가 없습니다.")
else:
    # 2024년 데이터만 필터링
    data_2024 = brand_registration_data[brand_registration_data['YearID'] == 2024]

    # 'total'을 포함하는 브랜드 제거
    no_total_data_2024 = data_2024[data_2024['BrandName'] != 'Total']

    if no_total_data_2024.empty:
        st.warning("2024년 데이터가 없습니다.")
    else:
        # 점유율이 1% 미만인 브랜드들을 "기타"로 묶기
        threshold = 1  # 1% 미만
        low_share_brands = no_total_data_2024[no_total_data_2024['MarketShare'] < threshold]
        high_share_brands = no_total_data_2024[no_total_data_2024['MarketShare'] >= threshold]

        # "기타" 브랜드 생성
        other_share = low_share_brands['MarketShare'].sum()
        other_registrations = low_share_brands['Registrations'].sum()

        # "기타" 데이터를 포함한 새로운 데이터프레임 생성
        other_brand = pd.DataFrame({
            'BrandName': ['기타'],
            'MarketShare': [other_share],
            'Registrations': [other_registrations]
        })

        # 1% 이상인 브랜드들과 "기타"를 합친 새로운 데이터
        final_data_2024 = pd.concat([high_share_brands, other_brand])

        # 데이터 정렬 (점유율이 큰 순서대로)
        final_data_2024 = final_data_2024.sort_values(by='MarketShare', ascending=False)

        # 색상 팔레트 정의
        colors = sns.color_palette('Pastel1', len(final_data_2024))

        # 원 그래프
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("2024년 브랜드별 점유율")
            fig1, ax1 = plt.subplots(figsize=(6, 6))
            ax1.pie(
                final_data_2024['MarketShare'],
                labels=final_data_2024['BrandName'],
                autopct='%1.1f%%',
                startangle=90,
                colors=colors  # 색상 적용
            )
            ax1.axis('equal')  # 원 모양 유지
            st.pyplot(fig1)

        # 세로 막대 그래프
        with col2:
            st.subheader("2024년 브랜드별 등록대수")
            fig2, ax2 = plt.subplots(figsize=(6, 6))
            ax2.bar(
                final_data_2024['BrandName'],
                final_data_2024['Registrations'],
                color=colors  # 색상 적용
            )
            ax2.set_xlabel("브랜드명")
            ax2.set_ylabel("등록 대수")
            ax2.set_title("2024년 브랜드별 등록 대수")
            ax2.tick_params(axis='x', rotation=45)  # x축 라벨 회전
            st.pyplot(fig2)

st.markdown("""
    <hr style="border: none; border-top: 0.1px solid #454876; margin-top: 20px; margin-bottom: 40px;">
""", unsafe_allow_html=True)

#-------------------------------------------------------------------------------------------------
# 2024년 top 5 브랜드, 점유율,등록대수
# 등록대수 
top5_data = final_data_2024.head(5)
st.subheader("2024년 등록대수 TOP 5 외산차 브랜드")
st.dataframe(top5_data)


st.markdown("""
    <hr style="border: none; border-top: 0.1px solid #454876; margin-top: 20px; margin-bottom: 40px;">
""", unsafe_allow_html=True)

#--------------------------------------------------------------------------------------------------

# # 과거 10년간 브랜드별 외산차 점유율 변화
brand_registration_data = load_brand_registration_data()
data = brand_registration_data[brand_registration_data['YearID'] != 2024]

# 'total'을 포함하는 브랜드 제거
data = data[data['BrandName'] != 'Total']
# 타이틀
st.subheader("브랜드별 등록 대수 변화 (2014년 ~ 2023년)")

# # 데이터 필터링: 2014년 ~ 2023년
# filtered_data = brand_registration_data[
#     (brand_registration_data['YearID'] >= 2014) & (brand_registration_data['YearID'] <= 2023)
# ]
# final_data_2024
# 데이터 필터링: 2014년 ~ 2023년

# filtered_data = data[
#     (data['YearID'] >= 2014) & (final_data_2024['YearID'] <= 2023)
# ]

# 데이터 확인
if data.empty:
    st.warning("선택된 조건에 맞는 데이터가 없습니다.")
else:
    # 브랜드별 선 그래프 그리기
    fig, ax = plt.subplots(figsize=(10, 6))


    # 브랜드별 데이터 색상 지정
    sns.set_palette('Pastel1', len(data['BrandName'].unique()))  # 브랜드 수에 따라 색상 설정
    for brand in data['BrandName'].unique():
        brand_data = data[data['BrandName'] == brand]
        ax.plot(
            brand_data['YearID'],
            brand_data['Registrations'],
            marker='o',
            label=brand
        )

    # 그래프 스타일 설정
    ax.set_title("2014년 ~ 2023년 브랜드별 등록 대수 변화", fontsize=16)
    ax.set_xlabel("연도", fontsize=12)
    ax.set_ylabel("등록 대수", fontsize=12)
    ax.legend(title="브랜드명", bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=10)  # 범례 위치 조정
    ax.grid(True, linestyle='--', alpha=0.7)

    # 그래프 출력
    st.pyplot(fig)