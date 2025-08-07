import streamlit as st

st.title("Clasificación ICC 2022 de la Leucemia Mieloide Aguda")
st.markdown("Basado en el artículo: [DOI:10.1182/blood.2022015850](https://doi.org/10.1182/blood.2022015850)")

# Pregunta inicial
blastos = st.radio("\n¿Tiene diez o más blastos en médula ósea?", ["sí", "no"])

if blastos == "no":
    st.info("El paciente tiene una neoplasia mielodisplásica a clasificar. Consulte el algoritmo diagnóstico específico para SMD.")
else:
    citogenetica = st.radio("¿Tiene una alteración citogenética recurrente?", ["sí", "no"])

    if citogenetica == "sí":
        st.success("Clasificación final: LMA con alteración citogenética recurrente")

    else:
        TP53 = st.radio("¿Tiene mutación de TP53?", ["sí", "no"])

        if TP53 == "sí":
            TP53_blastos = st.radio("¿Tiene 20% o más blastos en médula ósea?", ["sí", "no"])
            if TP53_blastos == "sí":
                st.success("Clasificación final: LMA con mutación de TP53")
            else:
                st.success("Clasificación final: LMA/SMD con mutación de TP53")

        else:
            mol_displasia = st.radio("¿Tiene una alteración molecular asociada a displasia?", ["sí", "no"])

            if mol_displasia == "sí":
                mol_displasia_blastos = st.radio("¿Tiene 20% o más blastos en médula ósea?", ["sí", "no"])
                if mol_displasia_blastos == "sí":
                    st.success("Clasificación final: LMA con alteración molecular asociada a displasia")
                else:
                    st.success("Clasificación final: LMA/SMD con alteración molecular asociada a displasia")

            else:
                citog_displasia = st.radio("¿Tiene una alteración citogenética asociada a displasia?", ["sí", "no"])

                if citog_displasia == "sí":
                    citog_displasia_blastos = st.radio("¿Tiene 20% o más blastos en médula ósea?", ["sí", "no"])
                    if citog_displasia_blastos == "sí":
                        st.success("Clasificación final: LMA con alteración citogenética asociada a displasia")
                    else:
                        st.success("Clasificación final: LMA/SMD con alteración citogenética asociada a displasia")
                else:
                    st.success("Clasificación final: LMA no clasificada (NOS)")
