import base64
import streamlit as st
import plotly.express as px
from PIL import Image

def app():
  # ---- LOAD ASSETS ----
  img_contact_form2 = Image.open("badminton.jpg")
  # ---- PROJECTS ----
  with st.container():
    st.write("---")
    st.header("THE PAGE")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
      st.image(img_contact_form2)
    with text_column:
      st.subheader("All about Badminton")
      st.write(
            """
           Badminton is a popular racket sport played by individuals or pairs.
           It is played on a rectangular court divided by a net, with players
           using lightweight rackets to hit a shuttlecock back and forth over
           the net. The objective of the game is to hit the shuttlecock over
           the net and land it in the opponent's court, with the aim of making
           it difficult for the opponent to return the shuttlecock. Points are
           scored when the shuttlecock lands on the opponent's court or when the
           opponent commits a fault. Badminton is a fast-paced and physically
           demanding sport that requires agility, speed, and precision.
           It is played at both amateur and professional levels, with international
           competitions such as the Olympics and the World Championships attracting
           top players from around the world.
            """
            )
      st.markdown("[Watch Video...](https://www.youtube.com/watch?v=ejrYU3jYbEg)")

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
  background-image: url("data:image/png;base64,{img4}");
  background-position: center; 
  background-repeat: no-repeat;
  background-size: 150%;
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
