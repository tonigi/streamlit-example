import streamlit as st
import os
import tempfile
from PIL import Image

st.title("Convert PPTX to PRIN-friendly PNG")

uf=st.file_uploader("Upload a PPTX file. For now 1st slide only, sorry.", 
		['pptx','ppt'])

if uf is not None:
    bd=uf.getvalue()
    #px=tempfile.NamedTemporaryFile(delete=False)
    #px=open(tempfile.TemporaryDirectory().name+uf.name,"wb")
    px=open(uf.name,"wb")
    px.write(bd)
    px.close()
    os.system(f"soffice --headless --convert-to pdf {px.name}")
    pdf_name=px.name.replace(".pptx",".pdf")
    png_name=px.name.replace(".pptx",".png")
    os.system(f"convert -geometry 680x -depth 8 {pdf_name} {png_name}")
    image = Image.open(png_name)
    
    st.subheader("Converted image")
    st.image(image)

    png_data=open(png_name,"rb").read()
    st.download_button("Download the image here", png_data, png_name)
    