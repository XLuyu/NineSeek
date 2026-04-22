import streamlit as st
import time
current_year = time.localtime().tm_year

def make(D):
    with D:
        st.subheader("创新性", divider='violet')
        paper_year = st.number_input("相关文献最早年份", value=2024)
        paper_no = st.number_input("相关技术文献数量", value=8)
        field_paper_no = st.number_input("所在领域文献数量", value=24)
    return {k:v for k,v in locals().items() if k in "paper_year paper_no field_paper_no".split()}

def score_v0(args):
    for k,py in [(5,60),(10,80),(20,100),(30,60),(40,40),(1000,10)]:
        if (current_year-args['paper_year'])<k: break
    for k,pn in [(50,80),(100,100),(200,60),(500,40),(1e8,10)]:
        if args['paper_no']<k: break
    for k,fpn in [(5000,100),(20000,80),(50000,60),(100000,40),(1e8,10)]:
        if args['field_paper_no']<k:  break
    return 0.3*py+0.6*pn+0.1*fpn