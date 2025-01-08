from modules.data_select import get_domestic_data, get_brand_registration_data, create_connection
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# import warnings
import matplotlib.font_manager as fm
import streamlit as st

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


# ------------------------MySQL 연결--------------------

# MySQL 연결 함수 및 데이터 session_state에 저장하여 불필요한 데이터 조회 방지지
@st.cache_resource
def get_connection():
    return create_connection()

@st.cache_data
def load_domestic_data():
    connection = get_connection()  # get_connection()에서 캐시된 연결을 가져옵니다.
    return get_domestic_data(connection)

@st.cache_data
def load_brand_registration_data():
    connection = get_connection()  # get_connection()에서 캐시된 연결을 가져옵니다.
    return get_brand_registration_data(connection)


def get_connection():
    return create_connection()

# 데이터 로드 함수, 연결을 매번 새로 생성
def load_domestic_data():
    connection = get_connection()  # get_connection()에서 새로 연결을 가져옵니다.
    return get_domestic_data(connection)

def load_brand_registration_data():
    connection = get_connection()  # get_connection()에서 새로 연결을 가져옵니다.
    return get_brand_registration_data(connection)


def initialize_session_data():
    if "domestic_data" not in st.session_state:
        st.session_state.domestic_data = load_domestic_data()
    if "brand_registration_data" not in st.session_state:
        st.session_state.brand_registration_data = load_brand_registration_data()

initialize_session_data()




# BrandName별 Total 등록 건수 계산
brand_totals = st.session_state.brand_registration_data[
    st.session_state.brand_registration_data["BrandName"] == "Total"
].drop(columns=["BrandID", "BrandName", "MarketShare"])


merged_data = pd.merge(
    st.session_state.domestic_data,
    brand_totals,
    how="inner",
    on="YearID"
)

merged_data = merged_data.rename(columns={
    'YearID': '연도',
    'TotalRegistrations': '국산차', 
    'Registrations': '외산차'   
})


## ---------------------매인 텍스트 영역 -----------------------

# 제목
st.markdown("""
    <div style="background-color: #fffafa; padding: 10px; border-radius: 3px; margin-bottom: 10px;">
        <h1 style="color: black; font-size: 3x; text-align: center;">🚕 전국 외산차 등록현황</h1>
    </div>
""", unsafe_allow_html=True)

# 구분선
st.markdown("""
    <hr style="border: none; border-top: 0.1px solid #454876; margin-top: 20px; margin-bottom: 40px;">
""", unsafe_allow_html=True)

#--------------------데이터 표시------------------
year_options = merged_data["연도"].unique()
year = st.multiselect("Year", year_options)
# year가 비어 있으면 전체 데이터로 필터링
if not year:
    filtered_df = merged_data
else:
    # 사용자가 선택한 연도에 맞게 필터링
    filtered_df = merged_data[merged_data["연도"].isin(year)]

# 국내 자동차 등록 데이터 표시
st.subheader("국내 자동차 등록 데이터 ")
st.dataframe(filtered_df, use_container_width=True)
#구분선선
st.markdown("""
    <hr style="border: none; border-top: 0.1px solid #454876; margin-top: 20px; margin-bottom: 40px;">
""", unsafe_allow_html=True)
#-------------------그래프 그리기-----------------
st.subheader("2024년 외산차 등록대수와 국산차 등록대수 비율 ")
plot_2024_df = merged_data[merged_data['연도'] == 2024]

labels = ['수입자동차_등록량', '국산자동차_등록량']
sizes = [
    plot_2024_df['외산차'].iloc[0], 
    plot_2024_df['국산차'].iloc[0]
]

# 색상 설정
colors = sns.color_palette('coolwarm', len(labels))

# 원그래프 그리기
plt.figure(figsize=(4, 4))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
plt.axis('equal')  # 원형 그래프 유지

# Streamlit에서 그래프 출력
st.pyplot(plt)

#구분선
st.markdown("""
    <hr style="border: none; border-top: 0.1px solid #454876; margin-top: 20px; margin-bottom: 40px;">
""", unsafe_allow_html=True)
#-----------------그래프2 그리기-----------------------
st.subheader("과거 10년간 외산차 등록대수와 국산차 등록대수 변화")
plot_non_2024_df = merged_data[merged_data['연도'] != 2024]
# 그래프 그리기
fig, ax1 = plt.subplots(figsize=(10, 6))

colors = sns.color_palette('coolwarm')

# 첫 번째 y축 (외산차 등록대수)
sns.lineplot(data=plot_non_2024_df, x="연도", y="외산차", ax=ax1, label="외산차", color=colors[1])
ax1.set_xlabel("연도", fontsize=12)
ax1.set_ylabel("외산차 등록대수", fontsize=12, color=colors[1])
ax1.tick_params(axis="y", labelcolor=colors[1])

# 두 번째 y축 (국산차 등록대수)
ax2 = ax1.twinx()
sns.lineplot(data=plot_non_2024_df, x="연도", y="국산차", ax=ax2, label="국산차", color=colors[4])
ax2.set_ylabel("국산차 등록대수", fontsize=12, color=colors[4])
ax2.tick_params(axis="y", labelcolor=colors[4])

plt.title("전체차량 등록대수와 외산차 등록대수 (연도별)", fontsize=14)

ax1.legend(loc="upper left")
ax2.legend(loc="upper right")

plt.tight_layout()
st.pyplot(fig)