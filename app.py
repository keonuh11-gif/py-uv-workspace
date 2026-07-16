

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# 차트 시각화 소개
st.title("📊 튜토리얼 5: 차트 시각화")




# 예시용 숫자 데이터 생성
data = pd.DataFrame({
    "x": [1,2,3,4,5],
    "y": [-0.5, 1, -1, 2 , 0]
})




# matplotlib로 선 그래프를 생성
fig, ax = plt.subplots()
ax.plot(data["x"], data["y"], marker='o')


# Streamlit 차트 렌더링
st.pyplot(fig)

# np.random.randn(10, 2) : 정규분포를 따르는 난수를 10행 2열로 구함
chart_data = pd.DataFrame(np.random.randn(10, 2), columns=["s", "t"])
st.line_chart(chart_data, width=0, height=300, use_container_width=True)

data = {"Year": [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
        "Sales": [100, 150, 200, 180, 150, 130, 200, 250, 270],
        "Revenue": [50, 80, 120, 90, 100, 80, 150, 200, 220]}
df = pd.DataFrame(data)
sns.set_palette("Set2")           # 그래프의 기본 색상 테마를 'Set2'로 설정
fig = plt.figure(figsize=(10, 6)) # 다중라인 그래프 그리기

plt.title("Sales and Revenue Trend")
plt.xlabel("Year")
plt.ylabel("Amount")

sns.lineplot(x="Year", y="Sales", data=df, marker="o", label="Sales")
sns.lineplot(x="Year", y="Revenue", data=df, marker="o", label="Revenue")
plt.legend(loc="lower center")           # 범례
st.pyplot(fig)
