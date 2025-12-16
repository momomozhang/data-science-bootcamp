import streamlit as st
from api import fetch_data

st.title("Pokemon Informationen")

name = st.text_input("Name des Pokemons von Interesse?")

if name:
    data = fetch_data(name)

    if data:
        st.header("Informationen")

        st.subheader(f"Name des Pokemons: {data['name']}")

        if data.get("sprites", {}).get("front_default"):
            st.image(data["sprites"]["front_default"])

        col1, col2 = st.columns(2)
        with col1:
            st.metric("Gewicht", data["weight"])
        with col2:
            st.metric("Größe", data["height"])

        st.subheader("Fähigkeiten:")
        for ability in data["abilities"]:
            st.write(f"- {ability['ability']['name']}")
    else:
        st.error("Pokemon nicht gefunden. Bitte versuche es erneut.")
