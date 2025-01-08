from modules.data_select import get_domestic_data, get_brand_registration_data, create_connection
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.font_manager as fm
import streamlit as st
from sklearn.linear_model import LinearRegression
import numpy as np

## -----------------제목--------------
st.markdown("""
    <div style="background-color: #fffafa; padding: 10px; border-radius: 3px; margin-bottom: 10px;">
        <h1 style="color: black; font-size: 3x; text-align: center;">❓ FAQ조회시스템</h1>
    </div>
""", unsafe_allow_html=True)


# 구분선
st.markdown("""
    <hr style="border: none; border-top: 0.1px solid #454876; margin-top: 20px; margin-bottom: 40px;">
""", unsafe_allow_html=True)
#----------------------------

df_lexus = pd.read_csv("LEXUS_FAQ.csv", encoding='utf-8-sig')
df_benz = pd.read_csv("BENZ_FAQ.csv", encoding='utf-8-sig')
df_volvo = pd.read_csv("VOLVO_FAQ.csv", encoding='utf-8-sig')

# 브랜드 선택지 UI
brand_options = ['Lexus', 'Benz', 'Volvo']
selected_brand = st.selectbox("브랜드 선택", brand_options)

# 브랜드에 맞는 데이터프레임 선택
if selected_brand == 'Lexus':
    df_selected = df_lexus
elif selected_brand == 'Benz':
    df_selected = df_benz
else:
    df_selected = df_volvo

# 검색창 UI
search_query = st.text_input("FAQ 검색", "")

# 검색 결과 필터링 (검색어가 포함된 FAQ만 표시)
if search_query:
    df_selected = df_selected[df_selected['FAQ'].str.contains(search_query, case=False, na=False)]

# 선택된 브랜드에 맞는 FAQ 데이터 표시
st.dataframe(df_selected, use_container_width=True)