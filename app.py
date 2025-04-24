import streamlit as st
from streamlit_drawable_canvas import st_canvas

st.title("Explota tu creatividad en este tablero!")

with st.siderbar:
  st.subheader("Propiedades del tablero")
  drawing_mode = st.sliderbar.selectbox(
    "Herramienta de Dibujo: ",
    ("freedraw","line","rect","circle","transform","polygon","point"),
)

stroke_width = st.slider("Tamaño del pincel",1,30,15)
stroke_color = st.color_picker("Color","#FFFFFF", key = "pincel")
bg_color = st.color_picker("Color del fondo","#000000")

canvas_result = st.canvas(
  fill_color = "rgba(255,165,0,0.3)",
  stroke_Width = "stroke_width",
  stroke_color = "stroke_color",
  background_color = bg_color,
  height = 500,
  width = 800,
  drawing_mode = drawing_mode,
  key = "canvas",
)
