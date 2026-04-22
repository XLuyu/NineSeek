import streamlit as st
from sqlalchemy import text 

conn = st.connection('proj_db', type='sql')
query = conn.query
with conn.session as s:
    s.execute(text('CREATE TABLE IF NOT EXISTS proj (pid INTEGER PRIMARY KEY AUTOINCREMENT, \
                                                paper_year INT, paper_no INT, field_paper_no INT, \
                                                tech_maturity TEXT, tech_leader_year INT, manu_maturity TEXT, \
                                                incidence_rate REAL, five_year_mortality_rate REAL, trial_no INT, \
                                                patent_cover TEXT, patent_type TEXT, patent_content TEXT, patent_series TEXT, \
                                                patent_state TEXT, patent_alike INT, patent_year INT, patent_holder TEXT, \
                                                firm_alike INT, cost_per_unit INT, outcome TEXT, industrial_standard TEXT, \
                                                market_per_year INT, china_order TEXT, china_market_type TEXT, \
                                                global_order TEXT, EU_US_market_type TEXT, top2_marketshare REAL \
                                                );'))
    s.commit()


def record(kwargs):
    with conn.session as s:
        s.execute(text("""
            INSERT INTO proj (
                paper_year, paper_no, field_paper_no,
                tech_maturity, tech_leader_year, manu_maturity,
                incidence_rate, five_year_mortality_rate,
                trial_no, patent_cover, patent_type,
                patent_content, patent_series, patent_state,
                patent_alike, patent_year, patent_holder,
                firm_alike, cost_per_unit, outcome,
                industrial_standard, market_per_year,
                china_order, china_market_type,
                global_order, EU_US_market_type, top2_marketshare
            ) VALUES (
                :paper_year, :paper_no, :field_paper_no,
                :tech_maturity, :tech_leader_year, :manu_maturity,
                :incidence_rate, :five_year_mortality_rate,
                :trial_no, :patent_cover, :patent_type,
                :patent_content, :patent_series, :patent_state,
                :patent_alike, :patent_year, :patent_holder,
                :firm_alike, :cost_per_unit, :outcome,
                :industrial_standard, :market_per_year,
                :china_order, :china_market_type,
                :global_order, :EU_US_market_type, :top2_marketshare
            )
        """), kwargs)
        s.commit()