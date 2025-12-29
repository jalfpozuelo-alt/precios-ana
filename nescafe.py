import streamlit as st
import pandas as pd
from datetime import datetime

# Configuración de página para que parezca una App de iPhone
st.set_page_config(
    page_title="Precios de Nescafé para Ana", 
    page_icon="☕", 
    layout="centered"
)

# Estilo personalizado con CSS para mejorar el aspecto
st.markdown("""
    <style>
    .main { background-color: #f5f5f7; }
    .stMetric { 
        background-color: white; 
        padding: 15px; 
        border-radius: 15px; 
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    h1 { color: #1d1d1f; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
    </style>
    """, unsafe_allow_html=True)

# Título personalizado
st.title("☕ Precios de Nescafé para Ana")
st.write(f"📅 Consulta del día: **{datetime.now().strftime('%d/%m/%Y')}**")

st.divider()

# --- DATOS REALES ---
# Aquí es donde el script de búsqueda pondrá los datos automáticamente
datos = [
    {"Super": "Alcampo", "Precio": 7.93, "Logo": "🏪"},
    {"Super": "Lidl", "Precio": 7.15, "Logo": "🟡"},
    {"Super": "Ahorramas", "Precio": 8.45, "Logo": "🔴"},
    {"Super": "Mercadona", "Precio": 8.45, "Logo": "🟢"},
    {"Super": "Carrefour", "Precio": 8.45, "Logo": "🔵"},
    {"Super": "Dia", "Precio": 8.45, "Logo": "⚪"}
]

df = pd.DataFrame(datos)
mejor_precio = df["Precio"].min()

# --- RESUMEN DESTACADO ---
st.subheader("📍 El mejor precio hoy")
col1, col2 = st.columns(2)

with col1:
    tienda_top = df.loc[df["Precio"].idxmin(), "Super"]
    st.metric(label="Mínimo Actual", value=f"{mejor_precio} €", delta="¡Ahorro!")

with col2:
    ahorro_total = round(df["Precio"].max() - mejor_precio, 2)
    st.metric(label="Ahorras hasta", value=f"{ahorro_total} €", delta_color="normal")

st.divider()

# --- LISTA DETALLADA ---
st.subheader("🛒 Comparativa por tienda")

# Ordenamos por precio para que Ana vea lo más barato arriba
df_ordenado = df.sort_values(by="Precio")

for _, row in df_ordenado.iterrows():
    # Si es el más barato, ponemos un borde verde
    if row["Precio"] == mejor_precio:
        st.success(f"**{row['Logo']} {row['Super']}** \t → \t **{row['Precio']} €** (RECOMENDADO)")
    else:
        st.info(f"**{row['Logo']} {row['Super']}** \t → \t {row['Precio']} €")

# --- CONSEJO FINAL ---
st.warning(f"💡 **Consejo para Ana:** Si vas a **{tienda_top}**, el bote te sale {ahorro_total}€ más barato que en Ahorramas o Mercadona.")
