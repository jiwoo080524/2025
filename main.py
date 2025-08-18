import streamlit as st
import time

st.set_page_config(page_title="MBTI 진로 추천기", page_icon="🌟", layout="centered")

st.markdown("""
    <style>
    .main-title {
        text-align: center;
        font-size: 2.5em;
        font-weight: 600;
        color: #2c3e50;
        margin-bottom: 0.1em;
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

st.markdown("<div class='main-title'>🔍 MBTI 진로 추천기</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>당신의 성격에 꼭 맞는 직업을 찾아드릴게요.</div>", unsafe_allow_html=True)

mbti_careers = {
    "ISTJ": [
        {"job": "📊 회계사", "reason": "세심한 성격과 꼼꼼함 덕분에 숫자 관리에 강합니다."},
        {"job": "🏛️ 공무원", "reason": "규칙을 잘 지키고 책임감이 강해 안정적인 직업에 적합합니다."},
        {"job": "🪖 군인", "reason": "조직 내 질서를 중시하며 임무 완수에 집중합니다."}
    ],
    "ISFJ": [
        {"job": "💉 간호사", "reason": "남을 돕는 마음이 강하고, 세심한 배려가 빛납니다."},
        {"job": "📚 초등학교 교사", "reason": "아이들을 세심히 챙기며 인내심이 많습니다."},
        {"job": "🤝 사회복지사", "reason": "타인의 고충을 이해하고 돕는 데 열정적입니다."}
    ],
    "INFJ": [
        {"job": "🧠 심리상담사", "reason": "깊은 공감과 통찰력으로 타인을 도울 수 있습니다."},
        {"job": "✍️ 작가", "reason": "풍부한 내면세계와 표현력이 뛰어납니다."},
        {"job": "🔍 인문학 연구자", "reason": "깊이 있는 사고와 분석력을 활용해 학문적 탐구에 적합합니다."}
    ],
    "INTJ": [
        {"job": "📈 전략기획가", "reason": "논리적이고 미래를 내다보는 능력이 뛰어납니다."},
        {"job": "🧮 데이터 분석가", "reason": "복잡한 문제를 체계적으로 해결하는 데 강합니다."},
        {"job": "🔬 과학자", "reason": "호기심과 분석력을 바탕으로 새로운 지식을 창출합니다."}
    ],
    "ISTP": [
        {"job": "🔧 기계 엔지니어", "reason": "실용적 문제 해결 능력이 뛰어나고 손재주가 좋습니다."},
        {"job": "🛠️ 정비사", "reason": "도구를 활용해 직접 문제를 해결하는 데 능숙합니다."},
        {"job": "🚓 경찰", "reason": "신속한 판단력과 현실적 대응능력을 갖추고 있습니다."}
    ],
    "ISFP": [
        {"job": "👗 패션 디자이너", "reason": "창의적이고 감각적인 표현력이 뛰어납니다."},
        {"job": "🌸 플로리스트", "reason": "자연과 미적 감각을 살려 아름다움을 창조합니다."},
        {"job": "🧘‍♀️ 물리치료사", "reason": "사람을 돌보는 따뜻한 마음과 기술이 조화를 이룹니다."}
    ],
    "INFP": [
        {"job": "📖 작가", "reason": "풍부한 감수성과 상상력으로 이야기를 만듭니다."},
        {"job": "🧒 아동 상담가", "reason": "섬세한 공감 능력으로 아이들의 마음을 이해합니다."},
        {"job": "🎨 예술가", "reason": "독창적이고 깊은 감성으로 작품을 창조합니다."}
    ],
    "INTP": [
        {"job": "🔬 연구원", "reason": "호기심과 논리적 사고로 문제를 분석하고 해결합니다."},
        {"job": "💻 프로그래머", "reason": "체계적이고 창의적인 코딩 능력을 갖추고 있습니다."},
        {"job": "🏫 대학 교수", "reason": "지식을 탐구하고 전달하는 데 열정적입니다."}
    ],
    "ESTP": [
        {"job": "💼 영업 전문가", "reason": "사교적이며 즉각적 대응 능력이 뛰어납니다."},
        {"job": "🎉 이벤트 기획자", "reason": "활발하고 창의적으로 행사를 이끌어갑니다."},
        {"job": "🚒 소방관", "reason": "빠른 판단과 용기로 위기 상황을 대응합니다."}
    ],
    "ESFP": [
        {"job": "🎭 배우", "reason": "표현력이 풍부하고 사람들과 소통하는 것을 즐깁니다."},
        {"job": "🎙️ MC", "reason": "즉흥적이고 밝은 에너지로 무대를 빛냅니다."},
        {"job": "🌍 여행 가이드", "reason": "사람들과의 교류와 새로운 경험을 좋아합니다."}
    ],
    "ENFP": [
        {"job": "📢 마케팅 전문가", "reason": "창의적 아이디어와 사람을 끄는 능력이 탁월합니다."},
        {"job": "🗞️ 기자", "reason": "다양한 주제를 탐구하고 전달하는 데 능숙합니다."},
        {"job": "👩‍🏫 교사", "reason": "열정적으로 학생과 소통하고 영감을 줍니다."}
    ],
    "ENTP": [
        {"job": "🚀 창업가", "reason": "도전 정신과 창의력으로 새로운 기회를 만듭니다."},
        {"job": "🎯 광고 기획자", "reason": "기발한 아이디어로 사람들의 관심을 이끌어냅니다."},
        {"job": "🧠 정치 컨설턴트", "reason": "전략적 사고로 복잡한 문제를 해결합니다."}
    ],
    "ESTJ": [
        {"job": "🏢 기업 관리자", "reason": "조직 운영과 계획에 뛰어난 실행력을 보입니다."},
        {"job": "⚙️ 생산 관리자", "reason": "효율적인 시스템 관리와 문제 해결이 강점입니다."},
        {"job": "🎖️ 군 간부", "reason": "강한 책임감과 리더십으로 조직을 이끕니다."}
    ],
    "ESFJ": [
        {"job": "👩‍⚕️ 간호사", "reason": "사람들을 돌보고 돕는 데 헌신적입니다."},
        {"job": "🙋 고객 서비스 매니저", "reason": "사교적이고 서비스 정신이 뛰어납니다."},
        {"job": "🥗 식품 영양사", "reason": "건강과 웰빙에 관심이 많고 배려심이 깊습니다."}
    ],
    "ENFJ": [
        {"job": "👨‍🏫 교사", "reason": "사람들과의 소통과 지도에 열정적입니다."},
        {"job": "🤝 HR 매니저", "reason": "조직 내 사람들의 조화를 이끌어냅니다."},
        {"job": "🧏 상담사", "reason": "타인의 고민을 듣고 해결하는 데 뛰어납니다."}
    ],
    "ENTJ": [
        {"job": "🧑‍💼 CEO", "reason": "리더십과 전략적 사고로 조직을 성공으로 이끕니다."},
        {"job": "📌 전략 컨설턴트", "reason": "복잡한 문제를 분석하고 해결책을 제시합니다."},
        {"job": "⚖️ 변호사", "reason": "논리적 사고와 설득력으로 법률 문제를 다룹니다."}
    ]
}

selected = st.selectbox("당신의 MBTI 유형을 선택하세요", list(mbti_careers.keys()))

if st.button("🔎 추천 직업 보기"):
    with st.spinner("당신의 성향을 분석 중입니다... 💭"):
        time.sleep(2)

    st.markdown("## 🎯 당신에게 어울리는 직업은...")

    for career in mbti_careers[selected]:
        time.sleep(1.2)
        st.markdown(f"""
        <div style="
            background-color: #fff;
            padding: 1em 1.2em;
            border-radius: 10px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
            margin-bottom: 1.3em;
        ">
            <h4 style="margin-bottom: 0.2em;">{career['job']}</h4>
            <p style="color: #555; margin-top:0;">{career['reason']}</p>
        </div>
        """, unsafe_allow_html=True)

    st.success("✔️ 진로 탐색의 첫걸음을 응원합니다!")

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<div style='text-align:center; color:gray;'>© 2025 MBTI Career Matcher</div>", unsafe_allow_html=True)
