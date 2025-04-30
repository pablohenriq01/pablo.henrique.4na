#api key : AIzaSyCBG6JDBgmVTyoJdF7rzpL7SoUcpY0YkWY

import streamlit as st
import google.generativeai as genai

GEMINI_API_KEY = "AIzaSyCBG6JDBgmVTyoJdF7rzpL7SoUcpY0YkWY"


genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel()

if "historico" not in st.session_state:
    st.session_state.historico = []

st.title("Desafio utilizando chatbot com Gemini")

st.markdown(
    """
    <style>
    body {
        background-color: #f0f8ff; 
        color: #333; 
    }
    .stTextInput > div > div > input {
        border: 2px solid #4682b4; 
        border-radius: 5px;
        padding: 10px;
    }
    .stButton > button {
        background-color: #4682b4; 
        color: white;
        border-radius: 5px;
        padding: 8px 15px;
        border: none;
    }
    .stButton > button:hover {
        background-color: #5e97cb; 
    }
    .remetente-voce {
        background-color: white;
        color: #333;
        padding: 8px;
        border-radius: 5px;
        margin-bottom: 5px;
        border: 1px solid #ccc;                                                
    }
    .remetente-gemini {
        background-color: #e0f2f7;                                                 
        color: #1a237e;
        padding: 8px;
        border-radius: 5px;
        margin-bottom: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

entrada = st.text_input("Você:", key="mensagem_usuario")

if st.button("Enviar") and entrada:
    try:
        resposta = model.generate_content(entrada)
        st.session_state.historico.append(("Você", entrada))
        st.session_state.historico.append(("Gemini", resposta.text))
    except Exception as e:
        st.error(f"Erro ao chamar Gemini: {e}")



for remetente, mensagem in st.session_state.historico:
    if remetente == "Você":
        st.markdown(f"<div class='remetente-voce'>**{remetente}:** {mensagem}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='remetente-gemini'>**{remetente}:** {mensagem}</div>", unsafe_allow_html=True)