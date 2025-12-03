import streamlit as st
import pandas as pd

# 파일 업로드 처리
st.title("MBTI 유형에 맞는 진로 추천")

# 파일을 로드합니다.
uploaded_file = st.file_uploader("CSV 파일을 업로드하세요.", type="csv")

if uploaded_file is not None:
    # 파일을 읽어 DataFrame으로 변환
    df = pd.read_csv(uploaded_file)

    # 파일 내용 확인
    st.write("파일 내용 미리보기:")
    st.write(df.head())

    # MBTI 유형을 선택하는 드롭다운 메뉴
    mbti_type = st.selectbox("MBTI 유형을 선택하세요:", df['MBTI'].unique())

    # 선택한 MBTI에 맞는 진로 추천
    selected_data = df[df['MBTI'] == mbti_type].iloc[0]
    st.write(f"**{mbti_type}** 유형에 맞는 진로를 추천합니다!")

    career1 = selected_data['Career1']
    career2 = selected_data['Career2']
    st.write(f"1. **{career1}**: 이 진로에 적합한 학과는 {selected_data['Career1_Dept']}이며, 성격은 {selected_data['Career1_Trait']}입니다.")
    st.write(f"2. **{career2}**: 이 진로에 적합한 학과는 {selected_data['Career2_Dept']}이며, 성격은 {selected_data['Career2_Trait']}입니다.")
    
    # 이코지 추가
    st.write("진로 선택에 도움이 되길 바라요! :) 꿈을 향해 가는 길, 멋지게 걸어가자구요!")
