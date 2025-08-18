import streamlit as st

# 데이터 예시
mbti_jobs = {
    "INTJ": ["전략 컨설턴트", "과학자", "소프트웨어 개발자"],
    "ENFP": ["마케팅 전문가", "기자", "교사"],
    "ISTJ": ["회계사", "관리자", "경찰"],
    "ESFP": ["이벤트 플래너", "연예인", "판매 전문가"],
    # ... 다른 유형들 추가
}

# Streamlit 앱 시작
st.title("MBTI 기반 진로 추천 웹앱")
st.markdown("당신의 MBTI를 선택하면, 적합한 직업을 추천해드려요!")

# 사용자 입력
mbti_types = list(mbti_jobs.keys())
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요", mbti_types)

# 결과 출력
if selected_mbti:
    st.subheader(f"✅ {selected_mbti} 유형에 어울리는 직업:")
    for job in mbti_jobs[selected_mbti]:
        st.write(f"- {job}")

