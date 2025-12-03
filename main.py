def mbti_career_recommendation(mbti_type):
    # MBTI 유형에 따른 진로 추천
    career_paths = {
        'INFJ': {
            'career1': '심리상담사',
            'career2': '작가',
            'description1': '사람들의 마음을 이해하고 돕는 것을 좋아하는 INFJ에게 완벽한 직업! 💖 깊은 통찰력을 바탕으로 상담을 통해 타인의 삶을 변화시킬 수 있어요.',
            'description2': '자신의 생각과 감정을 글로 표현하고 싶은 INFJ는 작가로서의 가능성을 타고 나죠. ✍️ 의미 있는 이야기를 통해 다른 사람들에게 영감을 줄 수 있어요.',
            'major1': '심리학, 상담학',
            'major2': '영문학, 창작 글쓰기',
            'personality1': '타인의 감정을 잘 이해하고, 도와주고 싶은 마음이 큰 사람.',
            'personality2': '창의적이고, 내면의 생각을 글로 표현하는 것을 좋아하는 사람.',
        },
        'INTJ': {
            'career1': '연구원',
            'career2': '기업 전략가',
            'description1': '논리적이고 체계적인 사고를 통해 깊이 있는 연구를 할 수 있는 INTJ에게 딱 맞는 직업! 🔬 새로운 아이디어를 찾아내고 문제를 해결하는 것에 능숙해요.',
            'description2': '기업이나 조직에서 전략을 구상하고 미래를 계획하는 일이 매력적인 INTJ! 📊 분석적이고 창의적인 전략을 통해 비즈니스의 성공을 이끌어갈 수 있어요.',
            'major1': '물리학, 공학, 생명과학',
            'major2': '경영학, 경제학',
            'personality1': '논리적이고 분석적인 사고를 통해 문제를 해결하는 것을 좋아하는 사람.',
            'personality2': '미래 지향적이고 창의적인 방법으로 조직을 이끄는 데 관심 있는 사람.',
        },
        'ENFP': {
            'career1': '마케팅 전문가',
            'career2': '행사 기획자',
            'description1': '열정적이고 창의적인 ENFP는 마케팅 전문가로서 새로운 아이디어를 끊임없이 발굴하며, 사람들을 끌어들이는 매력을 가지고 있어요! 📣',
            'description2': '다양한 사람들과 소통하고 창의적인 이벤트를 기획하는 것에 능한 ENFP! 🎉 이벤트 기획자로서 대규모 행사를 성공적으로 이끌 수 있어요.',
            'major1': '마케팅, 커뮤니케이션',
            'major2': '이벤트 기획, 디자인',
            'personality1': '새로운 아이디어를 발굴하고 사람들을 설득하는 것을 좋아하는 사람.',
            'personality2': '다양한 사람들과 소통하며 창의적인 기획을 하는 것을 즐기는 사람.',
        },
        'ISTJ': {
            'career1': '회계사',
            'career2': '법률 전문가',
            'description1': '정확하고 체계적인 일을 좋아하는 ISTJ는 세밀한 주의력이 필요한 회계 업무에 적합해요! 📚 숫자와 데이터를 다루는 데 강한 사람.',
            'description2': '법적 절차를 분석하고 규정을 따르는 일을 좋아하는 ISTJ는 법률 전문가로서 뛰어난 능력을 발휘할 수 있어요! ⚖️ 공정함과 규칙을 중요시하는 사람.',
            'major1': '회계학, 경영학',
            'major2': '법학, 정치학',
            'personality1': '세부적인 사항까지 꼼꼼히 체크하고, 체계적인 일을 선호하는 사람.',
            'personality2': '법적인 규정과 절차에 충실한 일을 좋아하는 사람.',
        }
    }
    
    # 해당 MBTI 유형에 맞는 진로 추천 및 설명 출력
    if mbti_type in career_paths:
        careers = career_paths[mbti_type]
        return f"""
        MBTI 유형: {mbti_type}
        
        🎯 **추천 진로 1**: {careers['career1']}
        설명: {careers['description1']}
        적합한 학과: {careers['major1']}
        성격: {careers['personality1']}
        
        🎯 **추천 진로 2**: {careers['career2']}
        설명: {careers['description2']}
        적합한 학과: {careers['major2']}
        성격: {careers['personality2']}
        """
    else:
        return "해당 MBTI 유형에 대한 정보가 없습니다."

# 예시로 INFJ 유형에 대해 진로 추천을 받아봅니다.
print(mbti_career_recommendation('INFJ'))
