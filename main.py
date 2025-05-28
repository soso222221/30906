import streamlit as st
import pandas as pd
import plotly.express as px  # 여기 수정


# 앱 제목
st.set_page_config(page_title="데이터 시각화 웹앱", layout="wide")
st.title("📊 데이터 시각화 웹앱")

# 데이터 로딩 함수 (캐싱)
@st.cache_data
def load_data():
    url = "https://drive.google.com/uc?export=download&id=1pwfON6doXyH5p7AOBJPfiofYlni0HVVY"
    df = pd.read_csv(url)
    return df

# 데이터 불러오기
df = load_data()

# 데이터 미리보기
st.subheader("🔍 데이터 미리보기")
st.dataframe(df.head())

# 날짜 컬럼 처리
if 'Date' in df.columns:
    df['Date'] = pd.to_datetime(df['Date'])

# 시각화 1: 시계열 그래프
if {'Date', 'Value'}.issubset(df.columns):
    st.subheader("📈 시계열 그래프")
    fig1 = px.line(df, x='Date', y='Value', color='Category', title="날짜별 Value 변화")
    st.plotly_chart(fig1, use_container_width=True)

# 시각화 2: 카테고리별 평균값
if {'Category', 'Value'}.issubset(df.columns):
    st.subheader("📊 카테고리별 평균 Value")
    avg_df = df.groupby('Category')['Value'].mean().reset_index()
    fig2 = px.bar(avg_df, x='Category', y='Value', title="카테고리별 평균 Value", color='Category')
    st.plotly_chart(fig2, use_container_width=True)

# 참고: 데이터 컬럼 확인을 위해 표시
st.sidebar.header("데이터 정보")
st.sidebar.write("컬럼 목록:", list(df.columns))
