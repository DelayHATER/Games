import streamlit as st
import streamlit.components.v1 as components

# 페이지 설정
st.set_page_config(page_title="버블버블 퍼즐 러너", layout="wide")

# index.html 파일을 읽어서 Streamlit 앱 화면에 웹 게임으로 렌더링
with open("index.html", "r", encoding="utf-8") as f:
    html_code = f.read()

# HTML 게임을 아이프레임(웹뷰) 형태로 출력 (높이 설정)
components.html(html_code, height=850, scrolling=True)
