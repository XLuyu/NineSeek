import streamlit as st

def make(D):
    with D:
        st.subheader("临床价值", divider='blue')
        incidence_rate = st.number_input("发病率", value=0.0001, format="%.6f")
        five_year_mortality_rate = st.number_input("5年死亡率", value=0.2)
        trial_no = st.number_input("Clinicaltrial.gov注册相关临床试验数", value=3)
    return {k:v for k,v in locals().items() if k in "incidence_rate five_year_mortality_rate trial_no".split()}

def score_v0(kv):
    for k,ir in [(0.000005,20),(0.00005,40),(0.0001,60),(0.05,80),(1e8,100)]:
        if kv['incidence_rate']<k: break
    for k,fymr in [(0.1,10),(0.2,40),(0.4,60),(0.6,80),(1e8,100)]:
        if kv['five_year_mortality_rate']<k: break
    for k,tn in [(2,20),(5,60),(10,80),(50,100),(75,60),(100,40),(1e8,20)]:
        if kv['trial_no']<=k:  break
    return 0.46*ir+0.42*fymr+0.12*tn