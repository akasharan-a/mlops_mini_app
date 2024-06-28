import streamlit as st
import requests

st.set_page_config(
    page_title="MLOps Mini App", layout="wide", page_icon="🪄"
)

row0_spacer1, row0_1, row0_spacer2, row0_2, row0_spacer3 = st.columns((.1, 2.3, .1, 1.3, .1))

tag_desc = {'crim': ['Per capita crime rate by town', 0.0, 90.0],
 'zn': ['Proportion of residential land zoned for lots over 25,000 sq.ft.',
  0.0,
  100.0],
 'indus': ['Proportion of non-retail business acres per town.', 0.0, 28.0],
 'chas': ['Charles river dummy variable (1 if tract bounds river; 0 otherwise)',
  0,
  1],
 'nox': ['Nitric oxides concentration (parts per 10 million)', 0.0, 0.90],
 'rm': ['Average number of rooms per dwelling', 0.0, 9.0],
 'age': ['Proportion of owner-occupied units built prior to 1940', 1, 100],
 'dis': ['Weighted distances to five boston employment centres',
  1.0,
  15.0],
 'rad': ['Index of accessibility to radial highways', 1,30],
 'tax': ['Full-value property-tax rate per $10,000', 100, 800],
 'ptratio': ['Pupil-teacher ratio by town', 10.0, 22.0],
 'b': ['1000(bk-0.63)^2 where bk is the proportion of blacks by town',
  0.10,
  400.0],
 'lstat': ['% lower status of the population', 1.0, 50.0],
 'medv': ["Median value of owner-occupied homes in $1000's", 5.0, 50.0]}

with row0_1:
    st.title('MLOps Mini App')
with st.sidebar:    
    st.header("Inputs")
    for t in tag_desc:
        st.slider(tag_desc[t][0], min_value=tag_desc[t][1], max_value=tag_desc[t][2],key=t)
    submit_button = st.button('Submit')

if submit_button:
    st.write(f"submit_button")
    x_vals = {t:st.session_state[t] for t in tag_desc}    
    st.write(x_vals)
    req = requests.post('http://127.0.0.1:8000/predict/',json=x_vals)

    st.write(f"Prediction : {req.json()['prediction']}")
