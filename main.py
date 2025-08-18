import streamlit as st
import time

# 페이지 설정
st.set_page_config(page_title="MBTI 진로 추천", page_icon="🌟", layout="centered")

# 스타일
st.markdown("""
    <style>
    .main-title {
        text-align: center;
        font-size: 2.5em;
        font-weight: 600;
        color: #2c3e50;
    }
    .subtitle {
        text-align: center;
        font-size: 1.1em;
        color: #7f8c8d;
        margin-bottom: 2em;
    }
    .job-box {
        background-color: #ffffff;
        padding: 1.2em;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        margin-bottom: 1.5em;
    }
    </style>
""", unsafe_allow_html=True)

# 제목
st.markdown("<div class='main-title'>🔍 MBTI 진로 추천기</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>당신의 성격에 꼭 맞는 직업을 찾아드릴게요.</div>", unsafe_allow_html=True)

# MBTI 데이터 (직업 + 이유)
mbti_careers = {
    "INFJ": [
        {"job": "🧠 심리상담사", "reason": "깊은 공감 능력과 타인에 대한 이해가 뛰어나기 때문이에요."},
        {"job": "✍️ 작가", "reason": "내면의 풍부한 감성을 글로 풀어내는 데 탁월해요."},
        {"job": "🔍 인문학 연구자", "reason": "깊이 있는 사고와 분석 능력으로 복잡한 주제를 탐구할 수 있어요."}
    ],
    "ENTP": [
        {"job": "🚀 창업가", "reason": "도전 정신과 창의력으로 새로운 가치를 만들어내는 데 강점이 있어요."},
        {"job": "🎯 광고 기획자", "reason": "톡톡 튀는 아이디어와 말솜씨로 사람들의 마음을 움직일 수 있어요."},
        {"job": "🧠 정치 컨설턴트", "reason": "빠른 판단력과 전략적 사고로 세상을 읽는 능력이 뛰어나요."}
    ],
    "ISFJ": [
        {"job": "💉 간호사", "reason": "사람을 돌보고 헌신하는 태도가 직업과 잘 맞아요."},
        {"job": "📚 초등학교 교사", "reason": "아이들을 세심하게 돌보고, 정성껏 가르칠 수 있어요."},
        {"job": "🤝 사회복지사", "reason": "타인을 위해 조용히 헌신하는 당신에게 딱이에요."}
    ],
    # 다른 MBTI도 필요하면 추가 가능!
}

# MBTI 선택
selected = st.selectbox("당신의 MBTI 유형을 선택하세요", list(mbti_careers.keys()))

# 버튼 클릭 시 결과 출력
if st.button("🔎 추천 직업 보기"):
    with st.spinner("당신의 성향을 분석 중입니다... 💭"):
        time.sleep(2)  # 로딩 연출

    st.markdown("## 🎯 당신에게 어울리는 직업은...")

    for career in mbti_careers[selected]:
        time.sleep(1.2)  # 등장 템포 조절

        with st.container():
            st.markdown(f"""
            <div class='job-box'>
                <h4 style='margin-bottom: 0.3em;'>{career['job']}</h4>
                <p style='color: #555;'>{career['reason']}</p>
            </div>
            """, unsafe_allow_html=True)

    st.success("✔️ 진로 탐색의 첫걸음을 응원해요!")

# 푸터
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<div style='text-align:center; color:gray;'>© 2025 MBTI Career Matcher</div>", unsafe_allow_html=True)
