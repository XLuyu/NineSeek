import streamlit as st

def make(D):
    with D:
        st.subheader("专利价值", divider='orange')
        D41, D42, D43 = st.columns(3)
        with D41:
            st.write(f"<span style='font-size:14px;'>专利覆盖度</span>", unsafe_allow_html=True)
            with st.container(border=True):
                patent_PCT = st.checkbox("PCT专利")
                patent_CN = st.checkbox("中国专利")
                patent_US = st.checkbox("美国专利")
                patent_EU = st.checkbox("欧洲专利")
                patent_cover = "".join("01"[i] for i in [patent_PCT, patent_CN, patent_US, patent_EU])
            patent_type = st.radio("专利类型", ["发明专利", "实用新型"])
            patent_content = st.radio("专利内容", ['保护关键物质组分', '保护平台方法'])
        with D42:
            patent_series = st.radio("专利成系列与否", ['已成系列','大致呈系列','专利孤岛','单个专利'])
            patent_state = st.radio("专利状态", ['授权','公开','实审','受理','未启动/驳回'])
        with D43:
            patent_alike = st.number_input("相似专利数", value=0)
            patent_year = st.number_input("关键专利申请时间", value=2025)
            patent_holder = st.radio("项目主导者与项目专利相关性", ['主要发明人','协助发明人','非发明人'])
    return {k:v for k,v in locals().items() if k in 
            "patent_cover patent_type patent_content patent_series patent_state patent_alike patent_year patent_holder".split()}

def score_v0(kv):
    pcv = sum([j for i,j in zip(kv['patent_cover'],[40,20,20,20]) if i=="1"])
    pt = {"发明专利":100,"实用新型":40}[kv['patent_type']]
    pct = {"保护关键物质组分":70,"保护平台方法":30}[kv['patent_content']]
    psr = {"已成系列":100,"大致呈系列":80,"专利孤岛":40,"单个专利":20}[kv['patent_series']]
    pst = {"授权":100,"公开":80,"实审":60,"受理":40,"未启动/驳回":0}[kv['patent_state']]
    for k, pa in [(2,100),(5,80),(8,60),(20,40),(1e8,20)]:
        if kv['patent_alike']<=k: break
    for k, py in [(2016,20),(2018,40),(2020,60),(2023,80),(1e8,100)]:
        if kv['patent_year']<k: break
    ph = {"主要发明人":100,"协助发明人":40,"非发明人":0}[kv['patent_holder']]
    return 0.08*pcv+0.07*pt+0.2*pct+0.06*psr+0.16*pst+0.2*pa+0.13*py+0.1*ph