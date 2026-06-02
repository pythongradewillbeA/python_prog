import streamlit as st
import streamlit.components.v1 as components

# 1. 페이지 기본 설정 (와이드 레이아웃, 타이틀 & 이모지 설정)
st.set_page_config(
    page_title="나의 하루 플래너 🌸",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Streamlit 기본 헤더, 푸터, 여백 제거하여 풀스크린 느낌 강조
hide_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
.block-container {
    padding-top: 0rem;
    padding-bottom: 0rem;
    padding-left: 0rem;
    padding-right: 0rem;
}
iframe {
    border-radius: 16px;
}
</style>
"""
st.markdown(hide_style, unsafe_allow_html=True)

# 3. todo.html 파일 읽기
try:
    with open("todo.html", "r", encoding="utf-8") as f:
        html_code = f.read()
except FileNotFoundError:
    st.error("todo.html 파일을 찾을 수 없습니다. 프로젝트 폴더에 todo.html 파일이 있는지 확인해 주세요!")
    html_code = None

# 4. Streamlit HTML 컴포넌트로 플래너 렌더링
if html_code:
    # 모바일 및 데스크탑 화면에서 모두 넉넉하게 스크롤 가능하도록 높이(height) 설정
    components.html(html_code, height=1300, scrolling=True)
