import streamlit as st
import random

# 🎨 페이지 설정
st.set_page_config(page_title="MBTI 진로 추천 💼✨", page_icon="💫", layout="centered")

# 🎀 타이틀
st.markdown("""
<div style='text-align: center;'>
    <h1 style='font-size: 60px;'>🌟 MBTI 진로 추천 웹앱 💼</h1>
    <p style='font-size: 24px;'>당신의 MBTI 유형에 어울리는 <span style='color:#f39c12;'>반짝반짝✨ 직업</span>을 찾아드려요!</p>
</div>
""", unsafe_allow_html=True)

# 🎯 데이터: MBTI → 직업
mbti_jobs = {
    "ISTJ": ["🧾 회계사", "🏛️ 공무원", "🪖 군인"],
    "ISFJ": ["💉 간호사", "📚 초등학교 교사", "💞 사회복지사"],
    "INFJ": ["🧠 심리상담사", "📝 작가", "🔍 인문학 연구자"],
    "INTJ": ["📊 전략기획가", "📈 데이터 분석가", "🔬 과학자"],

    "ISTP": ["🔧 기계 엔지니어", "🛠️ 정비사", "🚓 경찰"],
    "ISFP": ["👗 패션 디자이너", "🌸 플로리스트", "🧘‍♀️ 물리치료사"],
    "INFP": ["📖 작가", "🧒 아동 상담가", "🎨 예술가"],
    "INTP": ["🔬 연구원", "💻 프로그래머", "🏫 대학 교수"],

    "ESTP": ["💼 영업 전문가", "🎉 이벤트 기획자", "🔥 소방관"],
    "ESFP": ["🎤 배우", "🎙️ MC", "🌍 여행 가이드"],
    "ENFP": ["📢 마케팅 전문가", "🗞️ 기자", "👩‍🏫 교사"],
    "ENTP": ["🚀 창업가", "🎯 광고 기획자", "🧠 정치 컨설턴트"],

    "ESTJ": ["🏢 기업 관리자", "⚙️ 생산 관리자", "🎖️ 군 간부"],
    "ESFJ": ["👩‍⚕️ 간호사", "🙋 고객 서비스 매니저", "🥗 식품 영양사"],
    "ENFJ": ["👨‍🏫 교사", "🤝 HR 매니저", "🧏 상담사"],
    "ENTJ": ["🧑‍💼 CEO", "📌 전략 컨설턴트", "⚖️ 변호사"]
}

# 🌟 선택 박스
st.markdown("### 🔍 당신의 MBTI 유형을 골라주세요!")
selected_mbti = st.selectbox("👇 여기서 선택", list(mbti_jobs.keys()))

# 🎁 결과 출력
if selected_mbti:
    st.markdown("---")
    st.markdown(f"<h2 style='color:#e74c3c;'>🎉 {selected_mbti} 유형 추천 직업 🎯</h2>", unsafe_allow_html=True)
    
    # 무작위 컬러 이펙트
    colors = ["#f39c12", "#9b59b6", "#3498db", "#2ecc71", "#e67e22", "#1abc9c"]
    for job in mbti_jobs[selected_mbti]:
        color = random.choice(colors)
        st.markdown(f"<p style='font-size:22px; color:{color};'>👉 {job}</p>", unsafe_allow_html=True)

    st.markdown("✨ 위의 직업들이 당신과 잘 어울릴 수 있어요! 진로 탐색에 도움이 되길 바래요 💖")

# 👣 푸터
st.markdown("---")
st.markdown("""
<div style='text-align:center; font-size:14px; color:gray;'>
    만든이: ChatGPT | 디자인: 🌈 당신의 상상력
</div>
""", unsafe_allow_html=True)
