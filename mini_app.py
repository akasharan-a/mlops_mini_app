import streamlit as st

st.set_page_config(
    page_title="MLOps Mini App", layout="wide", page_icon="🪄"
)

row0_spacer1, row0_1, row0_spacer2, row0_2, row0_spacer3 = st.columns((.1, 2.3, .1, 1.3, .1))
with row0_1:
    st.title('MLOps Mini App')
with st.sidebar:    
    st.header("Feature engineering")
    st.slider('crim', min_value=0, max_value=90)
    
