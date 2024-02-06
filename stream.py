import streamlit as st


st.set_page_config(
    page_title="Churn Predictor",
    page_icon="🚕",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.linkedin.com/in/arjun-bhammar-27a351226/',
        'Report a bug': "https://www.linkedin.com/in/arjun-bhammar-27a351226/",
        'About': "# With :heart: from Arjun Bhammar !"
    }
)

st.sidebar.title(':blue[Welcome!] :sunglasses:')
st.sidebar.markdown('''
    :red[This] :orange[is] :green[a] :blue[churn] :violet[prediction]
    :gray[model] --- :rainbow[Try it !]''')

st.sidebar.header('Business Problem:', divider='rainbow')
st.sidebar.markdown("""
The Analytics Department at Ola is addressing the challenge of driver churn, a prevalent issue in the ride-hailing industry. 
High driver turnover, exacerbated by the competitive landscape, can impact operational efficiency and incur significant acquisition costs for new drivers. 
As a data scientist in the department, the focus is on predicting driver attrition. 
The monthly data for a subset of drivers from 2019 and 2020 is analyzed to build a predictive model, 
aiding in the identification of factors influencing driver retention and informing strategies to mitigate churn.
""")

with st.sidebar:
    add_image = st.image('Taxi.jpg')
with st.sidebar:
    st.caption("Photo by Jake Heinemann: https://www.pexels.com/photo/photo-of-yellow-taxi-parked-near-sidewalk-2399254/")
with st.sidebar:
    st.code(f"""
    Made by:
    Arjun Bhammar

    want to connect?
    """)

with st.sidebar:
    st.link_button("LinkedIn", "https://www.linkedin.com/in/arjun-bhammar-27a351226/")
    