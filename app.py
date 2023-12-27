import streamlit as st 
from googletrans import Translator
from languages import *


with st.sidebar:
    st.header("SELAMAT DATANG!!!")
    st.write("Produk ini berupa penerjemah bahasa yang bisa menerjemahkan dari bahasa indonesia keberbagai bahasa")
    st.write("-----------------------------")
    st.write("framework yang digunakan dalam produk ini adalah Streamlit.")
    st.write("-----------------------------")
    st.write("Streamlit adalah alat yang inovatif dan mudah digunakan untuk membuat website interaktif dengan bahasa pemrograman Python.")

st.title("Aplikasi Penerjemah Bahasa")
source_text = st.text_area("Masukan Kata/kalimat yang ingin diterjemah:")
target_language = st.selectbox("Pilih Bahasa:", languages)
translate = st.button('Terjemahkan')
if translate:
    translator = Translator()
    out = translator.translate(source_text,dest=target_language)
    st.write(out.text)
    
                               







