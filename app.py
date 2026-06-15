import streamlit as st
from removebg import RemoveBg
import os

st.title("أداة إزالة الخلفية الاحترافية")

# الحصول على الـ API Key من إعدادات Streamlit الآمنة
api_key = st.secrets["REMOVE_BG_API_KEY"]

uploaded_file = st.file_uploader("اختر صورة...", type=["jpg", "png"])

if uploaded_file is not None:
    with open(uploaded_file.name, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    rmbg = RemoveBg(api_key, "error_log.txt")
    rmbg.remove_background_from_img_file(uploaded_file.name)
    
    st.image(f"{uploaded_file.name}_no_bg.png", caption='النتيجة')
