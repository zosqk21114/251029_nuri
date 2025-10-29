import streamlit as st

st.set_page_config(page_title="💊 AI 약 도우미", page_icon="💊", layout="centered")

st.markdown("""
<h1 style='text-align:center;'>💊 AI 기반 약 추천 도우미</h1>
<p style='text-align:center; font-size:18px;'>
AI가 증상을 분석해 맞는 약을 추천하고, 복용 기록까지 도와드려요 🤖
</p>
""", unsafe_allow_html=True)

st.markdown("---")
st.markdown("""
### 📚 메뉴 안내
- 💊 **증상별 약 추천** : 증상을 입력하면 AI가 약을 추천합니다.  
- 🔍 **약 상세정보** : 각 약의 성분, 복용법, 주의사항을 볼 수 있습니다.  
- ⏰ **복용 알림 및 기록** : 복용한 약을 기록하고, 다음 복용 시간도 확인할 수 있습니다.
""")

st.markdown("""
<hr>
<p style='text-align:center; color:gray; font-size:13px;'>
Made with ❤️ using Streamlit
</p>
""", unsafe_allow_html=True)
