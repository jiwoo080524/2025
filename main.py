import streamlit as st

# 페이지 세팅
st.set_page_config(page_title="MBTI Career Matcher", page_icon="🧭", layout="centered")

# 스타일링용 HTML (모던하고 미니멀하게)
st.markdown("""
    <style>
    html, body {
        background-color: #f8f9fa;
    }
    .main-title {
        text-align: center;
        font-size: 3rem;
        font-weight: 600;
        color: #2c3e50;
        margin-bottom: 0.2em;
    }
    .subtitle {
        text-align: center;
        font-size: 1.2rem;
        color: #7f8c8d;
        margin-bottom: 2em;
    }
    .career-box {
        background-color: white;
        border-radius: 10px;
        padding: 1.5em;
        margin: 1em 0;
        box-shadow: 0 4px 8px rgba(0,0,0,0.05);
    }
    .career-box h3 {
        color: #34495e;
        font-size: 1.2rem;
    }
    .career-item {
        font-size: 1.05rem;
        padding: 0.3em 0;
    }
    .footer {
        text-align: center;
        color: #bdc3c7;
        font-size: 0.9rem;
        margin-top: 3em;
    }
    </style>
""", unsafe_allow_html=True)

# 메인 타이틀
st.markdown("<div class='main-title'>🔎 Find Your Fit</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>MBTI로 알아보는 나에게 딱 맞는 진로 ✨</div>", unsafe_allow_html=True)

# MBTI 데이터
mbti_jobs = {
    "ISTJ": ["회계사 📊", "공무원 🏛️", "군인 🪖"],
    "ISFJ": ["간호사 💉", "초등학교 교사 📚", "사회복지사 🤝"],
    "INFJ": ["심리상담사 🧠", "작가 ✍️", "인문학 연구자 🔍"],
    "INTJ": ["전략기획가 📈", "데이터 분석가 🧮", "과학자 🔬"],

    "ISTP": ["기계 엔지니어 🔧", "정비사 🛠️", "경찰 🚓"],
    "ISFP": ["패션 디자이너 👗", "플로리스트 🌸", "물리치료사 🧘‍♀️"],
    "INFP": ["작가 📖", "아동 상담가 🧒", "예술가 🎨"],
    "INTP": ["연구원 🔬", "프로그래머 💻", "대학 교수 🏫"],

    "ESTP": ["영업 전문가 💼", "이벤트 기획자 🎉", "소방관 🚒"],
    "ESFP": ["배우 🎭", "MC 🎙️", "여행 가이드 🌍"],
    "ENFP": ["마케팅 전문가 📢", "기자 🗞️", "교사 👩‍🏫"],
    "ENTP": ["창업가 🚀", "광고 기획자 🎯", "정치 컨설턴트 🧠"],

    "ESTJ": ["기업 관리자 🏢", "생산 관리자 ⚙️", "군 간부 🎖️"],
    "ESFJ": ["간호사 👩‍⚕️", "고객 서비스 매니저 🙋", "식품 영양사 🥗"],
    "ENFJ": ["교사 👨‍🏫", "HR 매니저 🤝", "상담사 🧏"],
    "ENTJ": ["CEO 🧑‍💼", "전략 컨설턴트 📌", "변호사 ⚖️"]
}

# MBTI 선택
selected = st.selectbox("🌱 당신의 MBTI를 선택하세요", list(mbti_jobs.keys()))

# 결과 박스
if selected:
    st.markdown(f"<div class='career-box'>", unsafe_allow_html=True)
    st.markdown(f"<h3>{selected} 유형에게 추천하는 직업은...</h3>", unsafe_allow_html=True)
    
    for job in mbti_jobs[selected]:
        st.markdown(f"<div class='career-item'>✅ {job}</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# 푸터
st.markdown("<div class='footer'>© 2025 MBTI Career Matcher · Designed with ❤️ by ChatGPT</div>", unsafe_allow_html=True)
