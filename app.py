# hello_streamlit.py
import streamlit as st


import time
import numpy as np
import pandas as pd




# 제목 추가
st.title("🎉 내 첫 번째 Streamlit 앱!")

# 텍스트 추가
st.write("안녕하세요! Streamlit으로 만든 웹 애플리케이션입니다.")

# 버튼 추가
if st.button("클릭해보세요!"):
    st.success("버튼이 클릭되었습니다! 🎊")

if st.button("이 버튼은 클릭할 수 없습니다"):
    st.markdown("축하축하")


left, middle, right = st.columns(3)
if left.button("Plain button", width="stretch"):
    left.markdown("You clicked the plain button.")
if middle.button("Emoji button", icon="😃", width="stretch"):
    middle.markdown("You clicked the emoji button.")
if right.button("Material button", icon=":material/mood:", width="stretch"):
    right.markdown("You clicked the Material button.")


_LOREM_IPSUM = """
Lorem ipsum dolor sit amet, **consectetur adipiscing** elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
"""

if st.button("click here") :
    st.success(_LOREM_IPSUM)


st.badge("New")
st.badge("Success", icon=":material/check:", color="green")
if st.button ("click here !!") :
    st.badge("test", icon="✨", color="red")

st.markdown(
    ":violet-badge[:material/star: Favorite] :orange-badge[⚠️ Needs review] :gray-badge[Deprecated]"
)


# 세션 상태 초기화
if "show_message" not in st.session_state:
    st.session_state.show_message = False

# 버튼 클릭 시 상태 토글
if st.button("메시지 토글"):
    st.session_state.show_message = not st.session_state.show_message

# 상태에 따라 메시지 표시
if st.session_state.show_message:
    st.success("🎉 Good job!")
