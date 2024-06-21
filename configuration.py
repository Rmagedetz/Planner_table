import streamlit as st

gs_credit_nails = {
    "type": st.secrets["gs_credit_nails"]["type"],
    "project_id": st.secrets["gs_credit_nails"]["project_id"],
    "private_key_id": st.secrets["gs_credit_nails"]["private_key_id"],
    "private_key": st.secrets["gs_credit_nails"]["private_key"],
    "client_email": st.secrets["gs_credit_nails"]["client_email"],
    "client_id": st.secrets["gs_credit_nails"]["client_id"],
    "auth_uri": st.secrets["gs_credit_nails"]["auth_uri"],
    "token_uri": st.secrets["gs_credit_nails"]["token_uri"],
    "auth_provider_x509_cert_url": st.secrets["gs_credit_nails"]["auth_provider_x509_cert_url"],
    "client_x509_cert_url": st.secrets["gs_credit_nails"]["client_x509_cert_url"]
}

urls = {"ДДВ": {"577РН": "https://docs.google.com/spreadsheets/d/1QFqkbqftePJ5DeLzQin8-XpSauBF4-28/edit?gid"
                         "=1858657956#gid=1858657956",
                "591РН": "https://docs.google.com/spreadsheets/d/1jenAkLi3cMJwFE90JCTULmLT-ZI_hi7y/edit?gid"
                         "=2068022059#gid=2068022059",
                "594РН": "https://docs.google.com/spreadsheets/d/1ifCCKqFgsy10W2tEQv5uzbn5EPutGExz/edit?gid=989782806"
                         "#gid=989782806",
                "597РН": "https://docs.google.com/spreadsheets/d/1sEOi3x4Qv11zszxFGZxPVVS8RMj5uMjF/edit?gid"
                         "=1681075567#gid=1681075567"},
        "ТДВ": {},
        "БМГ": {}}
