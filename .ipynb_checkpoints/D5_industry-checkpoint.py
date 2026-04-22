import streamlit as st

def make(D):
    with D:
        st.subheader("产业价值", divider='yellow')
        D1, D2, D3 = st.columns(3)
        firm_alike = D1.number_input("中国相同或相似公司数", value=0)
        cost_per_unit = D1.number_input("预估单例生产成本", value=1000)
        outcome = D2.radio("预计成果", ['临床药物或三类医疗器械','创新原辅料','新工艺原辅料','二类及以下医疗器械',
                                    '降低生产成本≥50%','降低生产成本＜50%','提升纯度至＞99%'])
        industrial_standard = D3.radio("行业标准", ['主持编写','参与编写','无标准','有标准，未参与标准制定'])
    return {k:v for k,v in locals().items() if k in "firm_alike cost_per_unit outcome industrial_standard".split()}

def score_v0(kv):
    for k,fa in [(2,100),(5,80),(10,60),(20,40),(1e8,10)]:
        if kv['firm_alike']<=k: break
    for k,cpu in [(1e4,100),(5e4,80),(1e5,60),(3e5,40),(1e8,20)]:
        if kv['cost_per_unit']<=k: break
    ot = {"临床药物或三类医疗器械":100,"创新原辅料":60,"新工艺原辅料":40,"二类及以下医疗器械":40,
          "降低生产成本≥50%":40,"降低生产成本＜50%":20,"提升纯度至＞99%":20}[kv['outcome']]
    ids = {"主持编写":100,"参与编写":40,"无标准":20,"有标准，未参与标准制定":10}[kv['industrial_standard']]
    return 0.15*fa+0.25*cpu+0.48*ot+0.12*ids