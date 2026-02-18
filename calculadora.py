import streamlit as st

st.set_page_config(page_title="Salud 3º ESO", page_icon="🏥")

st.title("Calculadora de Rebajas🏷️📉")
st.markdown("Holas, introduce tus datos")
st.write("---") # Línea separadora

st.sidebar.header("Tus Datos")
precio = st.sidebar.number_input("Precio Original", min_value=0, max_value=500, value=50)
descuento_porcentaje = st.sidebar.slider("Porcentaje de la Rebaja", 0, 100, 50)

if st.button("Calcular ahora"):
   
    rebaja = precio * (1 - descuento_porcentaje / 100)
   
    col1, col2 = st.columns(2)
   
    with col1:
        st.metric(label="Tu Precio Final es:", value=f"{rebaja:.2f}")
        st.markdown(''':grey[Te Ahorras:]''')
        st.write(f"{precio*descuento_porcentaje/100:.2f}")
       
    with col2:
        if descuento_porcentaje >= 50:
            st.warning("🤑 Demasiado Barato")        
        if descuento_porcentaje <= 50:
            st.warning("💩Mierdón, pero bueno...")
    st.write("---")
    st.info("Fórmula utilizada:")
    st.latex(r''' Rebaja = \frac{precio * porcentaje}{100} ''')
