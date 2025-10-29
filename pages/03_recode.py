import streamlit as st
from datetime import datetime, timedelta

st.markdown("## ⏰ 약 복용 알림 및 기록")

# 세션 상태 초기화
if "records" not in st.session_state:
    st.session_state["records"] = []

# 입력
with st.form("record_form"):
    name = st.text_input("약 이름 💊")
    count = st.number_input("복용 개수 (정/포)", min_value=1, max_value=10, value=1)
    time_taken = st.time_input("복용 시각", datetime.now().time())
    interval = st.number_input("다음 복용까지 (시간)", min_value=1, max_value=24, value=6)
    submitted = st.form_submit_button("✅ 복용 기록 추가")

    if submitted:
        if name.strip() == "":
            st.warning("약 이름을 입력해주세요.")
        else:
            record = {
                "약 이름": name,
                "복용 개수": count,
                "복용 시각": datetime.combine(datetime.today(), time_taken),
                "다음 복용 시간": datetime.combine(datetime.today(), time_taken) + timedelta(hours=interval)
            }
            st.session_state["records"].append(record)
            st.success(f"{name} 복용 기록이 추가되었습니다!")

# 기록 표시
st.markdown("---")
if not st.session_state["records"]:
    st.info("아직 복용 기록이 없습니다.")
else:
    for r in st.session_state["records"]:
        st.markdown(f"""
        💊 **{r['약 이름']}**
        - 복용 개수: {r['복용 개수']} 정  
        - 복용 시각: {r['복용 시각'].strftime('%H:%M')}  
        - 다음 복용: ⏰ {r['다음 복용 시간'].strftime('%H:%M')}
        """)

    if st.button("🗑️ 모든 기록 삭제"):
        st.session_state["records"].clear()
        st.warning("모든 복용 기록이 삭제되었습니다.")
