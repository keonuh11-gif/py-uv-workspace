

import streamlit as st
import pandas as pd

st.title('통계')

name = st.text_input('이름을 입력하세요')

major = st.text_input('전공을 입력하세요')

student_id = st.number_input('학번을 입력하세요', min_value=0)


header = ['학번', '이름', '전공']
students = [
#         ['202601', '홍길동', '컴퓨터공학'],
#         ['202602', '이순신', '데이터사이언스'],
#         ['202603', '유관순', '인공지능학']
]

df = pd.DataFrame(students, columns=header)

if "students" not in st.session_state:
    st.session_state.students = []

if st.button("학생 정보 출력"):
    st.session_state.students.append([student_id, name, major])

    df = pd.DataFrame(
        st.session_state.students,
        columns=["학번", "이름", "전공"]
    )

    st.dataframe(df)
