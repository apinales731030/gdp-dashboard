import streamlit as st
from openai import OpenAI
  
# Título y descripción
st.sidebar.title("🎓 PROYECTO CURSO: Desarrollo de asistentes virtuales usando Streamlit - - ")
st.sidebar.title("🎓 INSTRUCTOR: DR. JOSÉ NÁPOLES DUARTE  - ")
st.sidebar.title("🎓 ALUMNO: ADÁN PINALES MUNGUÍA  - ")
st.sidebar.title("🎓 FACULTAD DE INGENIERÍA  - UACH  - ")
#st.sidebar.image("https://github.com/apinales731030/gdp-dashboard/blob/main/fi.png?raw=true")
st.sidebar.image("fi.png")
#st.title.("🎓 Asistente del Reglamento para Estudiantes - Facultad de Ingeniería UACH")
st.title("🎓 Asistente del Reglamento para Estudiantes - Facultad de Ingeniería UACH")
 
 
# Obtener clave API desde secretos
openai_api_key = st.secrets["api_key"]
client = OpenAI(api_key=openai_api_key)

# Entrada del usuario
prompt = st.chat_input("¿Tienes dudas sobre tu situación como estudiante?")
if prompt is None:
    st.stop()

with st.chat_message("user", avatar="🎓"):
    st.markdown(prompt)

# Contexto centrado en estudiantes, basado en el reglamento oficial
reglamento_estudiantes = """
Este asistente responde preguntas sobre el Reglamento de la Facultad de Ingeniería de la UACH, específicamente en lo que respecta a los estudiantes.

1. Un alumno que reprueba una materia en todas sus oportunidades (ordinaria y no ordinaria) obtiene una calificación de N.A. (No Acreditada) y debe repetir el curso.
2. Las materias básicas son las fundamentales del plan de estudios de cada carrera, y no pueden ser dadas de baja.
3. No puedes reprobar todas las materias básicas, ya que son condición para avanzar en el programa.
4. Si no asistes al 60% de las clases, pierdes derecho a exámenes no ordinarios.
5. Si no asistes al 80%, pierdes derecho al examen ordinario.
6. Tienes derecho a dos intentos para acreditar una materia: un ordinario y uno no ordinario.
7. El servicio social y las prácticas profesionales son obligatorios para titularte.
8. Los cursos intensivos solo permiten dos materias, requieren 90% de asistencia y no tienen opción de examen no ordinario.
9. Las categorías de alumnos son: Regular, Irregular y Provisional.
10. Puedes revisar exámenes si no estás de acuerdo, mediante solicitud escrita en los 3 días hábiles posteriores a la publicación de la calificación.
11. Las tres materias básicas son: Álgebra, Física y Cálculo Diferencial e Integral
12. Para tener derecho a evaluaciones no ordinarias, el alumno deberá aprobar por lo menos el 50% de su carga académica, siempre y cuando curse dos o más materias; en caso contrario, deberá repetir la materia no acreditada.

Este asistente no reemplaza al reglamento oficial, pero te orienta de forma clara.
"""

# Combinamos contexto con la pregunta del usuario
promptfinal = reglamento_estudiantes + "\n\nPregunta del estudiante: " + prompt

# Llamada a OpenAI
stream = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "Eres un asistente experto en el reglamento universitario enfocado en ayudar a estudiantes de la Facultad de Ingeniería de la UACH."},
        {"role": "user", "content": promptfinal}
    ],
    max_tokens=800,
    temperature=0.2,
)

respuesta = stream.choices[0].message.content

# Mostrar respuesta del asistente
with st.chat_message("assistant", avatar="📘"):
    st.write(respuesta)
