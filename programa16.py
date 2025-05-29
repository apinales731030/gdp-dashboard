import streamlit as st
import random

st.set_page_config(page_title="🥠 Galleta de la Fortuna", layout="centered")
st.title("🥠 Tu galleta de la fortuna digital")

# Frases estilo "galleta china"
FORTUNAS = [
    "La suerte sonríe a quienes se atreven.",
    "Tu sonrisa ilumina más de lo que imaginas.",
    "Una sorpresa agradable está en camino.",
    "Hoy es un buen día para empezar algo nuevo.",
    "Pronto recibirás una respuesta que esperabas.",
    "Tu amabilidad cambiará el día de alguien más.",
    "La paciencia es el arte de confiar en el tiempo.",
    "Alguien piensa en ti con cariño.",
    "Todo lo que das, vuelve multiplicado.",
    "Un cambio pequeño hoy traerá grandes resultados mañana.",
    "Tendrás claridad en medio de la confusión.",
    "No temas hacer preguntas importantes.",
    "Una buena noticia llegará sin avisar.",
    "El silencio también puede ser una respuesta valiosa.",
]

# Entrada del usuario
user_input = st.chat_input("Rompe la galleta escribiendo algo...")

if user_input:
    st.chat_message("user").write(user_input)
    fortuna = random.choice(FORTUNAS)
    st.chat_message("assistant").write(f"🥠 *{fortuna}*")
