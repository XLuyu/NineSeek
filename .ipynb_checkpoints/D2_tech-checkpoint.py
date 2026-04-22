import streamlit as st

def make(D):
    with D:
        st.subheader("技术成熟度", divider='red')
        tech_maturity = st.selectbox("技术成熟度", ['上市','临床验证','GLP临床前验证','非GLP动物实验','体外实验验证','概念阶段/未进行生物学研究'])
        tech_leader_year = st.number_input("项目主导人从事该研究年限", value=3)
        manu_maturity = st.selectbox("生产成熟度", ['规模化生产','中试','小试','实验室制备/组装成功','合成/组装中'])
    return {k:v for k,v in locals().items() if k in "tech_maturity tech_leader_year manu_maturity".split()}


def score_v0(kv):
    tm = {'上市':20,'临床验证':100,'GLP临床前验证':80,'非GLP动物实验':60,'体外实验验证':40,'概念阶段/未进行生物学研究':20}[kv['tech_maturity']]
    for k,tl in [(2,10),(5,40),(10,60),(20,80),(1000,100)]:
        if kv['tech_leader_year']<=k: break
    mm = {'规模化生产':100,'中试':80,'小试':60,'实验室制备/组装成功':40,'合成/组装中':20}[kv['manu_maturity']]
    return 0.35*tm+0.4*tl+0.25*mm