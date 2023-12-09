import base64
import streamlit as st
import plotly.express as px
from PIL import Image

def app():
    df = px.data.iris()
    @st.cache_data
    def get_img_as_base64(file):
        with open(file, "rb") as f:
          data = f.read()
        return base64.b64encode(data).decode()

    img = get_img_as_base64("c1.jpg")
    img1 = get_img_as_base64("c2.jpg")
    img2 = get_img_as_base64("c3.jpg")
    img3 = get_img_as_base64("c4.jpg")
    img4 = get_img_as_base64("c5.jpg")

    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
    background-image: url("data:image/png;base64,{img3}");
    background-position: left; 
    background-repeat: repeat;
    background-size: 70%;
    background-attachment: fixed;
    }}
    [data-testid="stSidebar"] > div:first-child {{
    background-image: url("data:image/png;base64,{img}");
    background-position: left; 
    background-repeat: no-repeat;
    background-size: 120%;
    background-attachment: fixed;
    }}

    [data-testid="stHeader"] {{
    background: rgba(0,0,0,0);
    }}

    [data-testid="stToolbar"] {{
    right: 2rem;
    }}
    </style>
    """

    st.markdown(page_bg_img, unsafe_allow_html=True)

    st.title("About the Author")

    # ---- LOAD ASSETS ----
    img_contact_form = Image.open("c3.jpg")

    # ---- AUTHOR'S BACKGROUND ----
    with st.container():
        st.write("---")
        left_column, right_column = st.columns([1,2])
        
        with right_column:
            st.header("AUTHOR'S PROFILE")
            st.write(
                """
                PERSONAL INFORMATION
                
                Hellow, I am Charmel G. Tebe and I'm 18 years of age.
                Elementary: ANAO-AON CENTRAL ELEMENTARY SCHOOL
                High School: SAN FRANCISCO NATIONAL HIGH SCHOOL 
                College: SURIGAO DEL NORTE STATE UNIVERSITY
                Live: Poblacion, San Francisco, Surigao del Norte
                I'm currently studying in Surigao del Norte State
                I'm the only child
                """
            )
            
        with left_column:
            st.image(img_contact_form)
