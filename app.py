import streamlit as st
from streamlit_drawable_canvas import st_canvas

st.title("Explota tu creatividad en este tablero!")

with st.sidebar:
  st.subheader("Propiedades del tablero")
  #height_tablero = st.slider("Altura del liezo:", 100, 500, 300)
  #width_tablero = st.slider("Anchura del liezo:", 100, 500, 300)
  stroke_width = st.slider("Tamaño del pincel",1,30,15)
  stroke_color = st.color_picker("Color","#FFFFFF", key = "pincel")
  bg_color = st.color_picker("Color del fondo","#000000", key = "bg")  
  drawing_mode = st.sidebar.selectbox(
    "Herramienta de Dibujo: ",
    ("freedraw","line","rect","circle","transform","polygon","point"),
)

canvas_result = st_canvas(
  fill_color = "rgba(255,165,0,0.3)",
  stroke_width = stroke_width,
  stroke_color = stroke_color,
  background_color = bg_color,
  height = 700,
  width = 500,
  drawing_mode = drawing_mode,
  key = "canvas",
)
