import streamlit as st

st.set_page_config(page_title="MBTI 진로 추천기", page_icon="🎓")

st.title("🎓 MBTI 기반 진로 추천기")
st.write("너의 MBTI를 선택하면 딱! 맞는 진로 2개를 친절하게 추천해줄게 😎✨")

# -------------------------------------------
# 🔥 16개 MBTI 풀버전 진로 데이터베이스
# -------------------------------------------

career_paths = {

    # ---------------- INFJ ----------------
    'INFJ': {
        'career1': '심리상담사 🧠💗',
        'career2': '작가 ✍️✨',
        'description1': '사람들의 감정에 공감 잘하는 INFJ는 상담사로 찰떡! 따뜻한 조언으로 누군가에게 힘이 될 수 있어 😊',
        'description2': '깊고 감성적인 INFJ의 글은 사람들에게 위로가 돼! 의미 있는 이야기를 좋아한다면 작가가 딱!',
        'major1': '심리학, 상담학',
        'major2': '문예창작학, 국문학, 영문학',
        'personality1': '공감 능력 뛰어나고 사람을 돕는 것을 좋아하는 사람 💗',
        'personality2': '감수성이 풍부하고 글이나 창작을 좋아하는 사람 ✍️'
    },

    # ---------------- INFP ----------------
    'INFP': {
        'career1': '예술가 🎨🌈',
        'career2': '사회복지사 🤝💛',
        'description1': '상상력 + 감성 폭발 INFP! 예술로 감정을 표현하는 데 엄청난 재능이 있어 🎨',
        'description2': '따뜻한 마음으로 도움 필요한 사람을 돌보는 사회복지사도 INFP에게 찰떡!',
        'major1': '미술, 디자인, 음악, 공연예술',
        'major2': '사회복지학, 아동가족학',
        'personality1': '감수성 풍부하고 창의력이 넘치는 사람 🌈',
        'personality2': '배려심 깊고 사람들에게 따뜻한 위로를 건네는 사람 🤗'
    },

    # ---------------- INTJ ----------------
    'INTJ': {
        'career1': '연구원 🔬🧠',
        'career2': '전략 기획가 📊🧩',
        'description1': '논리 끝판왕 INTJ는 연구실에서 자신의 능력을 제대로 펼칠 수 있어!',
        'description2': '미래를 예측하고 전략을 세우는 건 INTJ의 특기! 조직을 이끄는 브레인 역할 🔥',
        'major1': '공학, 물리학, 통계학, 자연과학',
        'major2': '경영학, 경제학, 빅데이터',
        'personality1': '논리적이고 깊이 탐구하는 걸 좋아하는 사람 🔍',
        'personality2': '계획적이고 효율을 중요하게 여기는 사람 📈'
    },

    # ---------------- INTP ----------------
    'INTP': {
        'career1': '데이터 과학자 🧮💡',
        'career2': '개발자 👨‍💻⚙️',
        'description1': '복잡한 문제 푸는 걸 좋아하는 INTP는 데이터 과학 분야와 궁합 최고!',
        'description2': '새로운 기술 탐구하는 걸 좋아하는 INTP는 개발자 체질!',
        'major1': '수학, 통계학, 컴퓨터공학',
        'major2': '소프트웨어공학, 컴퓨터공학',
        'personality1': '호기심 많고 논리적인 문제 해결을 즐기는 사람 🤓',
        'personality2': '혼자 집중해서 작업하는 걸 좋아하는 사람 👨‍💻'
    },

    # ---------------- ENFJ ----------------
    'ENFJ': {
        'career1': '교사 👩‍🏫✨',
        'career2': '홍보·PR 전문가 📣💫',
        'description1': '사람을 이끄는 힘이 있는 ENFJ! 학생들을 따뜻하게 가르칠 수 있어.',
        'description2': '말 잘하고 사람들 앞에 나서는 거 좋아? 그럼 PR 분야가 딱!',
        'major1': '교육학, 국어교육, 영어교육',
        'major2': '광고홍보학, 커뮤니케이션학',
        'personality1': '사람을 돕고 이끄는 걸 좋아하는 사람 🙌',
        'personality2': '말주변 좋고 밝게 에너지를 주는 사람 😄'
    },

    # ---------------- ENFP ----------------
    'ENFP': {
        'career1': '마케터 📣🔥',
        'career2': '행사 기획자 🎉✨',
        'description1': '아이디어 뿜뿜 ENFP! 마케팅에서 그 재능이 폭발해요.',
        'description2': '활발한 에너지로 분위기 띄우는 ENFP는 행사기획도 찰떡!',
        'major1': '광고홍보학, 경영학',
        'major2': '이벤트 기획, 문화콘텐츠학',
        'personality1': '창의적인 걸 좋아하고 사람들과 소통하는 걸 좋아하는 사람 🙌',
        'personality2': '활기차고 조직 분위기를 이끄는 사람 😆'
    },

    # ---------------- ENTJ ----------------
    'ENTJ': {
        'career1': '경영자·리더 💼🔥',
        'career2': '프로젝트 매니저 📋🚀',
        'description1': '타고난 리더 ENTJ! 조직을 이끌고 결정하는 데 능숙해.',
        'description2': '사람들과 협업하고 계획을 이끄는 PM 역할은 ENTJ에게 완벽!',
        'major1': '경영학, 경제학',
        'major2': '산업공학, 경영학',
        'personality1': '목표 지향적이고 추진력 강한 사람 💥',
        'personality2': '상황 판단 빠르고 리더 역할을 좋아하는 사람 👑'
    },

    # ---------------- ENTP ----------------
    'ENTP': {
        'career1': '창업가 🚀💡',
        'career2': '크리에이터 🎥🎤',
        'description1': '새로운 아이디어에 미치는 ENTP는 스타트업 창업에 최적화!',
        'description2': '말빨 + 창의력 → 크리에이터 재능 넘침!',
        'major1': '경영학, 경제학, 미디어학',
        'major2': '영상제작, 디자인, 커뮤니케이션학',
        'personality1': '새로운 걸 좋아하고 도전 정신 강한 사람 🔥',
        'personality2': '재치 있고 말 잘하며 남들과 다른 창의성을 가진 사람 🎤'
    },

    # ---------------- ISFJ ----------------
    'ISFJ': {
        'career1': '간호사 🏥💗',
        'career2': '행정직 공무원 🗂️📘',
        'description1': '세심하고 따뜻한 ISFJ는 돌봄 직무에 찰떡!',
        'description2': '책임감 강한 ISFJ는 공무원 같은 안정적인 직무도 잘 맞아.',
        'major1': '간호학, 보건학',
        'major2': '행정학, 사회복지학',
        'personality1': '꼼꼼하고 배려심 깊은 사람 💕',
        'personality2': '책임감 강하고 안정적인 환경을 좋아하는 사람 📘'
    },

    # ---------------- ISFP ----------------
    'ISFP': {
        'career1': '패션 디자이너 👗🎨',
        'career2': '사진작가 📸✨',
        'description1': '감각적인 ISFP는 패션 분야에서 개성을 마음껏 발휘할 수 있어!',
        'description2': '섬세한 관찰력을 가진 ISFP는 사진작가도 잘 맞아!',
        'major1': '패션디자인학, 의상학',
        'major2': '사진학, 디자인',
        'personality1': '예술 감각 뛰어나고 섬세한 사람 🎨',
        'personality2': '혼자 몰입해서 작업하는 걸 좋아하는 사람 📸'
    },

    # ---------------- ISTJ ----------------
    'ISTJ': {
        'career1': '회계사 📘📊',
        'career2': '법률 전문가 ⚖️📚',
        'description1': '정확하고 신중한 ISTJ는 회계 분야에서 능력을 발휘해!',
        'description2': '원칙을 중시하는 ISTJ는 법조계와 찰떡궁합!',
        'major1': '회계학, 경영학',
        'major2': '법학, 행정학',
        'personality1': '꼼꼼하고 책임감 강한 사람 👍',
        'personality2': '공정함과 규칙을 중시하는 사람 ⚖️'
    },

    # ---------------- ISTP ----------------
    'ISTP': {
        'career1': '엔지니어 🛠️⚙️',
        'career2': '파일럿 ✈️🔥',
        'description1': '손재주 좋고 기계 좋아하는 ISTP! 엔지니어는 거의 천직!',
        'description2': '위기 대처 능력 좋은 ISTP는 파일럿도 매우 잘 맞아!',
        'major1': '기계공학, 전자공학, 자동차공학',
        'major2': '항공운항학, 항공정비학',
        'personality1': '실용적이고 문제 해결 능력 좋은 사람 🛠️',
        'personality2': '침착하고 집중력 좋은 사람 ✈️'
    },

    # ---------------- ESFJ ----------------
    'ESFJ': {
        'career1': '교사 👩‍🏫💛',
        'career2': '병원 코디네이터 🏥🌼',
        'description1': '따뜻하고 책임감 있는 ESFJ는 교사로서 큰 힘을 발휘해!',
        'description2': '친절하고 배려심 깊은 ESFJ는 병원 업무에도 찰떡!',
        'major1': '교육학, 유아교육과',
        'major2': '보건행정학, 의료서비스학',
        'personality1': '사람을 도와주는 걸 좋아하는 사람 💛',
        'personality2': '친절하고 소통 능력 좋은 사람 🌼'
    },

    # ---------------- ESFP ----------------
    'ESFP': {
        'career1': '배우·연예인 🎤✨',
        'career2': '여행 가이드 🌍😆',
        'description1': '끼 많고 밝은 ESFP는 무대에서 빛나는 타입!',
        'description2': '사람 만나는 거 좋아하면 여행 가이드도 딱!',
        'major1': '연극영화과, 방송연예과',
        'major2': '관광학, 문화콘텐츠학',
        'personality1': '활발하고 표현력 좋은 사람 🎤',
        'personality2': '사교적이고 에너지 넘치는 사람 😆'
    },

    # ---------------- ESTJ ----------------
    'ESTJ': {
        'career1': '군인 🪖🔥',
        'career2': '관리자·팀장 📋💼',
        'description1': '책임감·규율 철저한 ESTJ는 군 조직과 찰떡!',
        'description2': '팀을 관리하고 조직을 운영하는 데 매우 능숙!',
        'major1': '군사학, 행정학',
        'major2': '경영학, 산업공학',
        'personality1': '책임감 강하고 규칙 잘 지키는 사람 🪖',
        'personality2': '리더십 발휘하는 걸 좋아하는 사람 💼'
    },

    # ---------------- ESTP ----------------
    'ESTP': {
        'career1': '세일즈 전문가 💸🔥',
        'career2': '경찰관 🚓💪',
        'description1': '말 잘하고 행동 빠른 ESTP는 영업에서 능력 폭발!',
        'description2': '위기 대응 능력 좋은 ESTP는 경찰직도 찰떡!',
        'major1': '경영학, 마케팅학',
        'major2': '경찰행정학, 범죄학',
        'personality1': '활동적이고 도전적인 사람 🔥',
        'personality2': '용감하고 순간 판단력 좋은 사람 💪'
    }
}


# -------------------------------------------
# 🔽 MBTI 선택 UI
# -------------------------------------------

mbti_list = list(career_paths.keys())
user_mbti = st.selectbox("너의 MBTI를 골라줘! 😎", mbti_list)

st.divider()

# -------------------------------------------
# 🔽 결과 출력
# -------------------------------------------
if user_mbti:
    data = career_paths[user_mbti]

    st.subheader(f"🌟 {user_mbti} 유형 맞춤 진로 추천")

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
