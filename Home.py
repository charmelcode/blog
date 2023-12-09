import base64
import streamlit as st
from PIL import Image
import plotly.express as px

def app():   
  # ---- HEADER SECTION ----
  with st.container():
    st.title("MAIN PAGE")
    st.subheader("ALL ABOUT BADMINTON")
    st.title("To train hard is the best way to become the best version of yourself!")
    st.write(
            "If you dare to win, we should also dare to lose!"
            )
    
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
  background-image: url("data:image/png;base64,{img1}");
  background-position: center; 
  background-repeat: no-repeat;
  background-size: 100%;
  background-attachment: local;
   }}
  [data-testid="stSidebar"] > div:first-child {{
  background-image: url("data:image/png;base64,{img}");
  background-position: left; 
  background-repeat: no-repeat;
  background-size: 150%;
  background-attachment: local;
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
