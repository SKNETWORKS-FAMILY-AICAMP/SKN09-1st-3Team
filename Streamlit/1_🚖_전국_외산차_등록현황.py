import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import matplotlib.font_manager as fm
import streamlit as st

## -------------matplotlib font설정 및 테마 설정----------------
# sns.set_theme(style="whitegrid")
sns.set_theme(style="darkgrid", rc={"axes.facecolor": "lightgrey"})
warnings.filterwarnings("ignore", category=UserWarning, module="matplotlib")
warnings.filterwarnings("ignore", category=FutureWarning, module="seaborn")

font_path = "C:\\Users\\Playdata\\AppData\\Local\\Microsoft\\Windows\\Fonts\\Pretendard-Regular.otf"
font_name = fm.FontProperties(fname=font_path).get_name()
plt.rc('font', family=font_name)

plt.rcParams['axes.unicode_minus'] = False

## ---------------------매인 텍스트 영역 -----------------------
st.title("🚕전국 외산차 등록현황")

year_options = ['2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']
year = st.selectbox("Year", year_options)

