import streamlit as st
from rembg import remove
from PIL import Image
import io

st.title("أداة إزالة الخلفية المجانية")

uploaded_file = st.file_uploader("ارفع صورتك هنا...", type=["jpg", "png", "jpeg"])

if uploaded_file:
    # قراءة الصورة
    input_image = Image.open(uploaded_file)

    # المعالجة (مجانية تماماً!)
    with st.spinner('جاري إزالة الخلفية...'):
        output_image = remove(input_image)

    # عرض النتيجة
    st.image(output_image, caption='تمت إزالة الخلفية بنجاح')

    # زر التحميل
    buf = io.BytesIO()
    output_image.save(buf, format="PNG")
    byte_im = buf.getvalue()

    st.download_button(
        label="تحميل الصورة",
        data=byte_im,
        file_name="no_bg.png",
        mime="image/png"
    )
