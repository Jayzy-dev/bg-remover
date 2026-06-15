import streamlit as st
from rembg import remove
from PIL import Image
import io

st.set_page_config(page_title="Background Remover", layout="centered")

st.title("✂️ مزيل الخلفية الذكي")
st.write("ارفع صورتك وسأقوم بإزالة الخلفية فوراً!")

uploaded_file = st.file_uploader("اختر صورة...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="الصورة الأصلية", use_container_width=True)
    
    with st.spinner('جاري معالجة الصورة... قد يستغرق هذا بضع ثوانٍ'):
        # إزالة الخلفية
        output = remove(image)
        st.image(output, caption="النتيجة بدون خلفية", use_container_width=True)
        
        # زر التحميل
        buf = io.BytesIO()
        output.save(buf, format="PNG")
        st.download_button("📥 تحميل الصورة", buf.getvalue(), "no_bg.png", "image/png")
else:
    st.info("بانتظار رفع الصورة للبدء...")
