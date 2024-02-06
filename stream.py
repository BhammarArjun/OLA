import streamlit as st
import pickle

# Sidebar

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

# Main content

st.title("The Features are based on data")
col1, col2 = st.columns(2)
with col1:
    st.subheader('Age of Driver?', divider='blue')
    age = st.number_input('Age')

with col2:
    st.subheader('Monthly income of Driver?', divider='green')
    income = st.number_input('Income')


col1, col2 = st.columns(2)
with col1:
    st.subheader('Education Level?', divider='orange')
    education = st.radio(
    "Please select from below",
    [0,1, 2],
    captions = ["Upto 10th", "12th", "Graduation"])
with col2:
    st.subheader('Quaterly Rating?', divider='violet')
    qrating = st.radio(
    "Higher is Better",
    [1,2, 3, 4])


col1, col2 = st.columns(2)
with col1:
    st.subheader('Current Grade?', divider='rainbow')
    grade = st.selectbox(
    'Higher is Better !',
    (1, 2, 3,4,5))

with col2:
    st.subheader('Joining Designation', divider='blue')
    designation = st.selectbox(
    'Higher is Better!',
    (1, 2, 3,4,5))

col1, col2 = st.columns(2)
with col1:
    st.subheader('FirstReport lead?', divider='green')
    frl = st.slider('How many days driver took to report?', -100, 300, 2)

with col2:
    st.subheader('Service Days', divider='grey')
    service = st.slider('Number of days on duty?', 1, 700, 2)

st.divider()

st.write("Press the below button to compute the prediction !")

@st.cache_resource(ttl=360)
def load_model():
    with open('model.pkl', 'rb') as handle:
        model = pickle.load(handle)
    with open('df.pkl', 'rb') as handle:
        df = pickle.load(handle)
    with open('chart.pkl', 'rb') as handle:
        chart = pickle.load(handle)
    
    return model, df,chart

model,df,chart = load_model()
tot = [age, education, income, designation, grade, qrating, frl, service]

def get_prediction(tot):
    ans = model.predict([tot])

    if ans == 1:
        out = 'Churn'
    else:
        out = "Not Churn"
    
    return out

col1, col2 = st.columns(2)

if st.button("Predict"):
    ans = get_prediction(tot)
    st.title(f"Prediction is -- '{ans}'")
    st.plotly_chart(chart,theme="streamlit", use_container_width=True)


