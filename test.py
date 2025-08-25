import streamlit as st

st.set_page_config(page_title="건강검진 결과 해석 도우미", layout="centered")

# -----------------------
# 세션 상태 관리
# -----------------------
if "page" not in st.session_state:
    st.session_state.page = "input"

# -----------------------
# 판별 함수들
# -----------------------
def interpret_bp(sbp, dbp):
    if sbp < 120 and dbp < 80:
        return "정상", "🟢", "정상 혈압입니다. 유지하세요."
    elif sbp < 140 or dbp < 90:
        return "경계", "🟡", "고혈압 전단계입니다. 식이요법과 운동을 권장합니다."
    else:
        return "위험", "🔴", "고혈압 가능성이 있습니다. 의료기관 상담을 추천합니다."

def interpret_glucose(glu):
    if glu < 100:
        return "정상", "🟢", "정상 혈당입니다."
    elif glu < 126:
        return "경계", "🟡", "공복 혈당이 높습니다. 식이 조절이 필요합니다."
    else:
        return "위험", "🔴", "당뇨병 가능성이 있습니다. 검사와 관리가 필요합니다."

def interpret_chol_total(val):
    if val < 200:
        return "정상", "🟢", "정상 콜레스테롤 수치입니다."
    elif val < 240:
        return "경계", "🟡", "조금 높은 수치입니다. 식습관 개선이 필요합니다."
    else:
        return "위험", "🔴", "높은 콜레스테롤입니다. 심혈관 질환 위험이 있습니다."

def interpret_hdl(hdl, gender):
    threshold = 40 if gender == "남성" else 50
    if hdl >= threshold:
        return "정상", "🟢", "좋은 HDL 수치입니다."
    else:
        return "위험", "🔴", "HDL 수치가 낮아 심혈관 질환 위험이 있습니다."

def interpret_ldl(val):
    if val < 100:
        return "정상", "🟢", "LDL 수치가 양호합니다."
    elif val < 130:
        return "경계", "🟡", "조금 높습니다. 주의가 필요합니다."
    else:
        return "위험", "🔴", "높은 LDL 수치입니다. 관리가 필요합니다."

def interpret_tg(val):
    if val < 150:
        return "정상", "🟢", "정상 중성지방 수치입니다."
    elif val < 200:
        return "경계", "🟡", "조금 높습니다. 식이 관리가 필요합니다."
    else:
        return "위험", "🔴", "높은 중성지방 수치입니다. 주의가 필요합니다."

# -----------------------
# 결과 저장 + 페이지 전환 함수
# -----------------------
def save_and_go_result(sbp, dbp, glucose, chol_total, hdl, ldl, tg, gender):
    st.session_state.results = {
        "혈압": interpret_bp(sbp, dbp),
        "공복 혈당": interpret_glucose(glucose),
        "총 콜레스테롤": interpret_chol_total(chol_total),
        "HDL 콜레스테롤": interpret_hdl(hdl, gender),
        "LDL 콜레스테롤": interpret_ldl(ldl),
        "중성지방": interpret_tg(tg),
    }
    st.session_state.page = "result"

# -----------------------
# 입력 페이지
# -----------------------
if st.session_state.page == "input":
    st.title("🩺 건강검진 결과 해석 도우미")
    st.markdown("검진 수치를 입력하면, 정상 여부와 건강 관리 팁을 제공해드립니다.")

    with st.form("health_form"):
        col1, col2 = st.columns(2)
        with col1:
            age = st.number_input("나이", min_value=0, max_value=120, value=30)
            sbp = st.number_input("수축기 혈압 (mmHg)", value=120)
            glucose = st.number_input("공복 혈당 (mg/dL)", value=90)
            chol_total = st.number_input("총 콜레스테롤 (mg/dL)", value=180)
        with col2:
            gender = st.selectbox("성별", ["남성", "여성"])
            dbp = st.number_input("이완기 혈압 (mmHg)", value=80)
            hdl = st.number_input("HDL 콜레스테롤 (mg/dL)", value=50)
            ldl = st.number_input("LDL 콜레스테롤 (mg/dL)", value=100)
            tg = st.number_input("중성지방 (mg/dL)", value=120)

        submitted = st.form_submit_button(
            "🔍 결과 분석",
            on_click=save_and_go_result,
            args=(sbp, dbp, glucose, chol_total, hdl, ldl, tg, gender)
        )

# -----------------------
# 결과 페이지 (항목별만 출력)
# -----------------------
elif st.session_state.page == "result":
    st.title("📋 분석 결과")

    results = st.session_state.get("results", {})
    color_map = {"정상": "green", "경계": "orange", "위험": "red"}

    for name, (level, icon, message) in results.items():
        st.markdown(f"### {icon} {name} - :{color_map[level]}[{level}]")
        st.write(f"➡️ {message}")
        st.divider()

    if st.button("⬅️ 다시 입력하기"):
        st.session_state.page = "input"
        elif st.session_state.page == "result":
    st.title("📋 분석 결과")

    results = st.session_state.get("results", {})
    color_map = {"정상": "green", "경계": "orange", "위험": "red"}

    # ✅ 결과 요약 계산
    summary_counts = {"정상": 0, "경계": 0, "위험": 0}
    for _, (level, _, _) in results.items():
        summary_counts[level] += 1

    total = sum(summary_counts.values())

    # ✅ 요약 메시지 생성
    if summary_counts["위험"] > 0:
        summary_msg = "⚠️ 건강 위험 요소가 있습니다. 전문가 상담이 필요합니다."
    elif summary_counts["경계"] > 0:
        summary_msg = "🟡 일부 수치가 경계입니다. 생활습관 개선을 권장합니다."
    else:
        summary_msg = "🟢 전반적으로 건강한 상태입니다. 현재 상태를 유지하세요!"

    # ✅ 결과 요약 출력
    with st.expander("📊 건강 상태 요약 보기", expanded=True):
        st.markdown(f"""
        - ✅ 정상 항목: **{summary_counts['정상']}개**
        - ⚠️ 경계 항목: **{summary_counts['경계']}개**
        - 🔴 위험 항목: **{summary_counts['위험']}개**
        """)
        st.markdown(f"**📌 종합 평가:** {summary_msg}")

    st.divider()

    # ✅ 개별 항목 출력
    for name, (level, icon, message) in results.items():
        st.markdown(f"### {icon} {name} - :{color_map[level]}[{level}]")
        st.write(f"➡️ {message}")
        st.divider()

    if st.button("⬅️ 다시 입력하기"):
        st.session_state.page = "input"

