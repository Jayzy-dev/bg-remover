from rembg import remove
from PIL import Image
import io
import streamlit as st

uploaded_file = st.file_uploader("ارفع صورتك", type=["jpg", "png"])
if uploaded_file:
    input_image = Image.open(uploaded_file)
    output_image = remove(input_image) # هذا هو السحر المجاني!
    st.image(output_image)
