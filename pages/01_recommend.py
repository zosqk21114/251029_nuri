import streamlit as st

# ----------------------------
# 약 데이터
# ----------------------------
medicine_db = {
    "타이레놀": ["두통", "발열", "근육통"],
    "이부프로펜": ["염증", "통증", "생리통"],
    "게보린": ["두통", "치통", "생리통"],
    "겔포스": ["속쓰림", "위통", "소화불량"]
}

# ----------------------------
# 증상 분류 함수
# ----------------------------
def ai_classify_symptom(symptom_text):
    text = symptom_text.lower()
    if any(x in text for x in ["머리", "두통", "열", "통증", "발열"]):
        return ["타이레놀", "이부프로펜", "게보린"]
    elif any(x in text for x in ["속", "위", "소화", "더부룩", "메스꺼움"]):
        return ["겔포스"]
    else:
        return ["타이레놀"]

# ----------------------------
# 페이지 UI
# ----------------------------
st.markdown("## 🤖 AI 기반 증상 분석 + 약 추천")

with st.form("symptom_form"):
    symptom = st.text_area("현재 증상을 입력하세요 💬", placeholder="예: 머리가 아프고 열이 나요")
    submitted = st.form_submit_button("💊 약 추천 받기")

    if submitted:
        if symptom.strip() == "":
            st.warning("⚠️ 증상을 입력해주세요.")
        else:
            recommended = ai_classify_symptom(symptom)
            st.session_state["recommended_medicines"] = recommended
            st.success("💡 추천 결과가 아래에 표시됩니다.")

# ----------------------------
# 추천 결과 표시
# ----------------------------
if "recommended_medicines" in st.session_state:
    st.markdown("### 💊 추천 약 목록")
    for med in st.session_state["recommended_medicines"]:
        st.button(f"🔍 {med} 상세보기", key=med)
