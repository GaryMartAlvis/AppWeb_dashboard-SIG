import streamlit as st 

def app():
    # Título y subtítulo de la presentación
    st.title('Dashboard-SIG')
    st.subheader('Desarrollo de APP Web - Sistema de Información Gerencial')
    
    # Línea de división 
    st.write('---')

    st.write("""
    
    A continuación, presento propuesta de trabajo para el desarrollo de la aplicación web que albergará el Sistema de Información Gerencial de la Cooperativa San Martín de Porres denominada APP Dashboard-SIG. 
    
    La APP Dashboard-SIG será una herramienta de visualización de datos la cual se concibe como una solución integral para la inteligencia de negocios a nivel instituncional.

    """)

    # Titulo de bloque
    st.markdown("<h3 style='text-align: center; margin-top: 2rem;'>Dashboard-SIG, versión Excel Actual</h3>", unsafe_allow_html=True)
    
    # Ilustración 
    st.image('img\\dashboard.jpg')

    st.write("<p style='margin-top: 2rem;'>Esta propuesta comprende tres apartados destinados a ilustrar y dimensionar el trabajo a realizar, al mismo tiempo que justificará el esfuerzo y la dedicación que se requerirá para obtener los beneficios que implica la incorporación de una APP Web como herramienta de trabajo.</p>",unsafe_allow_html=True)

    # Creación de 3 columnas para contenido
    col1, col2, col3 = st.columns(3)

    # Contenido de la columna 1
    with col1:
        st.markdown("""
        <div style='text-align: center;'>
            <h2>1️⃣</h2>
            <h3>Tecnología</h3>
            <p>En este apartado se presentará la tecnología principal que servirá como base del proyecto. Se justificará la elección de esta tecnología, explicando sus ventajas y potencial, el cual se manifestará de manera evidente en las etapas finales del proyecto.</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Contenido de la columna 2
    with col2:
        st.markdown("""
        <div style='text-align: center;'>
            <h2>2️⃣</h2>
            <h3>Plan de trabajo</h3>
            <p>Aquí se expondrá el plan de trabajo propuesto para abordar el desarrollo e implementación de la APP Web en sus distintas etapas. Se comenzará con el desarrollo del MVP (Producto Mínimo Viable) en un escenario de uso de Intranet Local, detallando las fases y actividades a realizar.</p>
        </div>
        """, unsafe_allow_html=True)

    # Contenido de la columna 1
    with col3:
        st.markdown("""
        <div style='text-align: center;'>
            <h2>3️⃣</h2>
            <h3>Aplicaciones</h3>
            <p>Como apartado final, se presentarán muestras funcionales de la APP Web. Estas demostraciones serán ejemplos de las funcionalidades básicas que el proyecto pretende abordar, ofreciendo una visión clara de cómo será la aplicación en su funcionamiento práctico.</p>
        </div>
        """, unsafe_allow_html=True)
