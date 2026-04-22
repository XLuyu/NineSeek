import streamlit as st

def make(D):
    market_per_year, top2_marketshare, china_order, china_market_type, global_order, EU_US_market_type = [0,0]+[""]*4
    with D:
        st.subheader("市场前景预期", divider='green')
        cla = st.radio("产品分类", ["药/械分类", "药物或化妆品原辅料分类"])
        D61, D62 = st.columns(2)
        if cla=="药/械分类":
            market_per_year = st.number_input("中国潜在获得治疗人数/年", value=10000)
            china_order = D61.radio("中国上市顺位预期", ['1','1＜顺位≤3','顺位＞3','三类医疗器械','改良创新药','仿制药或二类及以下医疗器械'])
            global_order = D62.radio("全球上市顺位预期", ['1','1＜顺位≤3','顺位＞3','三类医疗器械','改良创新药','仿制药或二类及以下医疗器械'])
        else:
            china_market_type = D61.radio("预计中国市场性质", ['新兴市场','快速成长市场','成熟市场','边缘市场'])
            EU_US_market_type = D62.radio("预计欧美市场性质", ['新兴市场','快速成长市场','成熟市场','边缘市场'])
            top2_marketshare = st.number_input("全球前2名供应商市场份额占比之和", value=50.0, min_value=0.0, max_value=100.0)
    return {k:v for k,v in locals().items() if k in "market_per_year china_order china_market_type global_order EU_US_market_type top2_marketshare".split()}
    
def score_v0(kv):
    if kv['market_per_year']:
        for k,mpy in [(2e3,20),(2e4,40),(1e5,60),(1e6,80),(1e8,100)]:
            if market_per_year<=k: break
        co = {"1":100,"1＜顺位≤3":80,"顺位＞3":60,"三类医疗器械":40,"改良创新药":40,"仿制药或二类及以下医疗器械":20}[china_order]
        go = {"1":100,"1＜顺位≤3":80,"顺位＞3":60,"三类医疗器械":40,"改良创新药":40,"仿制药或二类及以下医疗器械":20}[global_order]
        return 0.6*mpy+0.3*co+0.1*go
    else: 
        cm = {"新兴市场":80,"快速成长市场":100,"成熟市场":60,"边缘市场":40}[china_market_type]
        gm = {"新兴市场":80,"快速成长市场":100,"成熟市场":60,"边缘市场":40}[EU_US_market_type]
        for k,tms in [(20,100),(40,80),(60,60),(80,40),(100,20)]:
            if top2_marketshare<=k: break
        return 0.58*cm+0.32*gm+0.1*tms