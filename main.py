import streamlit as st

st.set_page_config(page_title="MBTI 진로 추천기", page_icon="🎓")

st.title("🎓 MBTI 기반 진로 추천기")
st.write("안녕! 너의 MBTI를 선택하면 딱 맞는 진로 2개를 추천해줄게 😊✨")

# MBTI 데이터
career_paths = {
    'INFJ': {
        'career1': '심리상담사 🧠💗',
        'career2': '작가 ✍️✨',
        'description1': '사람들의 마음을 이해하고 공감하는 능력이 뛰어난 INFJ! 상담사로서 누군가에게 진짜 힘이 되어줄 수 있어 😊',
        'description2': '깊은 생각과 감성을 글로 표현하는 능력 최고! INFJ는 의미 있는 스토리 만드는 데 천재야 ✨',
        'major1': '심리학, 상담학',
        'major2': '국문학, 문예창작, 영문학',
        'personality1': '배려심 깊고 감정에 민감하며 타인을 돕고 싶은 마음이 큰 사람 💗',
        'personality2': '감수성이 풍부하고, 글이나 창작 활동을 좋아하는 사람 ✍️'
    },
    'INTJ': {
        'career1': '연구원 🔬🧠',
        'career2': '전략 기획가 📊🧩',
        'description1': '논리와 분석력 끝판왕 INTJ! 연구로 새로운 지식을 만드는 타입이야.',
        'description2': '계획 세우고 전략 짜는 거 좋아하지? 회사의 방향을 잡는 멋진 전략가가 딱이야!',
        'major1': '공학, 자연과학, 통계학',
        'major2': '경영학, 경제학',
        'personality1': '논리적이고 혼자 깊이 탐구하는 걸 좋아하는 사람 🔍',
        'personality2': '냉철하게 판단하고 효율을 중요하게 여기는 사람 📈'
    },
    'ENFP': {
        'career1': '마케팅 전문가 📣🔥',
        'career2': '행사 기획자 🎉✨',
        'description1': '아이디어 뿜뿜! 사람들과 잘 어울리는 ENFP의 끼를 마음껏 펼칠 수 있어!',
        'description2': '활발하고 창의적인 너라면 행사 기획에서 분위기 메이커 확정!',
        'major1': '경영학, 광고홍보학',
        'major2': '이벤트 기획, 문화콘텐츠학',
        'personality1': '새로운 걸 시도해보고, 사람들과 소통하는 걸 즐기는 타입 🙌',
        'personality2': '창의적이고 팀 분위기를 이끄는 걸 좋아하는 사람 😆'
    },
    'ISTJ': {
        'career1': '회계사 📘📊',
        'career2': '법률 전문가 ⚖️📚',
        'description1': '꼼꼼함의 대명사 ISTJ! 숫자와 자료를 정확하게 다룰 수 있어.',
        'description2': '규칙•원칙 중요하게 생각하는 성격이라 법조계와 찰떡!',
        'major1': '회계학, 세무학, 경영학',
        'major2': '법학, 행정학',
        'personality1': '정리정돈 잘하고 책임감 강한 사람 👍',
        'personality2': '원칙적이고 공정함을 중요하게 여기는 사람 ⚖️'
    }
}

# MBTI 선택
mbti_list = list(career_paths.keys())
user_mbti = st.selectbox("너의 MBTI를 골라줘! 😎", mbti_list)

st.divider()

if user_mbti:
    data = career_paths[user_mbti]

    st.subheader(f"🌟 {user_mbti} 유형 추천 진로")
    
    # 진로 1
    st.write(f"### 🎯 추천 진로 1: **{data['career1']}**")
    st.write(f"- {data['description1']}")
    st.write(f"- **관련 학과:** {data['major1']}")
    st.write(f"- **잘 맞는 성격:** {data['personality1']}")

    st.write("---")

    # 진로 2
    st.write(f"### 🎯 추천 진로 2: **{data['career2']}**")
    st.write(f"- {data['description2']}")
    st.write(f"- **관련 학과:** {data['major2']}")
    st.write(f"- **잘 맞는 성격:** {data['personality2']}")
