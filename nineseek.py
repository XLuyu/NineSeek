import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import D1_novelty
import D2_tech
import D3_clinic
import D4_patent
import D5_industry
import D6_market
import DB_utils
dimension = ["创新性", "技术成熟度", "临床价值", "专利价值", "产业价值", "市场前景"]

st.title("求索引擎", text_alignment='center')
st.caption("六维ATMP项目早筛评估系统", text_alignment='center')
# st.set_page_config(layout="wide")

#layout
D1, D2, D3 = st.columns(3, border=True)
D4 = st.columns(1, border=True)[0]
D5 = st.columns(1, border=True)[0]
D6 = st.columns(1, border=True)[0]

# widgets
D1_data = D1_novelty.make(D1)
D2_data = D2_tech.make(D2)
D3_data = D3_clinic.make(D3)
D4_data = D4_patent.make(D4)
D5_data = D5_industry.make(D5)
D6_data = D6_market.make(D6)

# compute
D1_score = D1_novelty.score_v0(D1_data)
D2_score = D2_tech.score_v0(D2_data)
D3_score = D3_clinic.score_v0(D3_data)
D4_score = D4_patent.score_v0(D4_data)
D5_score = D5_industry.score_v0(D5_data)
D6_score = D6_market.score_v0(D6_data)

scores = [D1_score, D2_score, D3_score, D4_score, D5_score, D6_score]
final_score = np.array([0.1, 0.24, 0.24, 0.14, 0.2, 0.08])*scores

# show result
@st.dialog("评估结果")
def show_result(scores):
    if st.radio("图表", ["雷达图", "柱状图"])=="雷达图":
        label = ["%s(%.2d)"%(name, s) for name, s in zip(dimension, scores)]
        fig = px.line_polar(r=scores, theta=label, line_close=True).update_traces(fill='toself')
        st.plotly_chart(fig)
    else:
        fig = px.bar(y=scores, x=dimension, text_auto=True, labels={"x": "评价维度", "y": "得分"})
        st.plotly_chart(fig)
    
if st.button("评估", type="primary", width='stretch'):
    kvs = {**D1_data, **D2_data, **D3_data, **D4_data, **D5_data, **D6_data}
    st.write(kvs)
    DB_utils.record(kvs)
    show_result(scores)

df = DB_utils.query("SELECT * FROM proj", ttl=0)
# st.dataframe(df)
