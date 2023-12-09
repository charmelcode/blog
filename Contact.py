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
    img5 = get_img_as_base64("c6.jpg")
    img6 = get_img_as_base64("c7.jpg")

    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
    background-image: url("data:image/png;base64,{img5}");
    background-position: left; 
    background-repeat: repeat;
    background-size: 70%;
    background-attachment: fixed;
    }}
    [data-testid="stSidebar"] > div:first-child {{
    background-image: url("data:image/png;base64,{img}");
    background-position: left; 
    background-repeat: repeat;
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
    st.title("For Queries") 
    
    # ---- LOAD ASSETS ----

    # ---- CONTACT ----
    cols, cols1 = st.columns(2)
    with cols:
        with st.container():
            st.write("---")
            st.header("HOLD TIGHT!")
            st.write("##")
            st.write(
                " Open Up here"
            )

            # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
            contact_form = """
            <form action="https://formsubmit.co/YOUR@MAIL.COM" method="POST">
                <input type="hidden" name="_captcha" value="false">
                <input type="text" name="name" placeholder="Your name" required>
                <input type="email" name="email" placeholder="Your email" required>
                <textarea name="message" placeholder="Your message here" required></textarea>
                <button type="submit">Send</button>
            </form>
            """
            left_column, right_column = st.columns(2)
            with left_column:
                st.markdown(contact_form, unsafe_allow_html=True)
            with right_column:
                st.empty()

