import streamlit as st
import Calcula_media as Cm


imagem1 = st.image("C:\\Users\\Aluno_Programador3\\Desktop\\I_LOVE_PASTAS\\projeto_1\\OIP.webp")


st.title("Calculadora Escolar para as :blue[férias] :sunglasses:")

nome_do_meliante = st.text_input("Qual o nome do Individuo")

nota_slider1 = st.slider(min_value=0.0, max_value=10.0,label="Qual a nota do aluno em Mátematica",step=0.25)
nota_slider2 = st.slider(min_value=0.0, max_value=10.0,label="Qual a nota do aluno em Portgues",step=0.25)
nota_slider3 = st.slider(min_value=0.0, max_value=10.0,label="Qual a nota do aluno em Idiomas",step=0.25)
nota_slider4 = st.slider(min_value=0.0, max_value=10.0,label="Qual a nota do aluno em Fisica",step=0.25)


