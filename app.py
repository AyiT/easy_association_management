import streamlit as st
import pandas as pd
import datetime

st.set_page_config(page_title="Mini CRM")

# Charger les données
@st.cache_data
def load_data():
    try:
        df = pd.read_csv("contacts.csv")
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Nom", "Email", "Téléphone", "Tag", "Note", "Dernier contact", "Relancer le"])
    return df

df = load_data()

#ajout contact
st.sidebar.header("Ajouter un contact")

with st.sidebar.form(key="add_contact"):
    nom = st.text_input("Nom")
    email = st.text_input("Email")
    tel = st.text_input("Téléphone")
    tag = st.text_input("Tag (adhérent, prospect...)")
    note = st.text_area("Note")
    dernier_contact = st.date_input("Dernier contact", datetime.date.today())
    relance = st.date_input("Relancer le", dernier_contact + datetime.timedelta(days=30))
    submit = st.form_submit_button("Ajouter")

if submit:
    new_row = pd.DataFrame([[nom, email, tel, tag, note, dernier_contact, relance]], columns=df.columns)
    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv("contacts.csv", index=False)
    st.success("Contact ajouté !")


st.title("Mes contacts")

filtre_tag = st.selectbox("Filtrer par tag", options=["Tous"] + list(df["Tag"].unique()))
if filtre_tag != "Tous":
    df = df[df["Tag"] == filtre_tag]

st.dataframe(df)

aujourdhui = datetime.date.today()
relances = df[df["Relancer le"] <= pd.to_datetime(aujourdhui)]

if not relances.empty:
    st.warning("📌 Contacts à relancer aujourd’hui ou en retard :")
    st.table(relances[["Nom", "Email", "Relancer le"]])

st.download_button("📤 Exporter en CSV", df.to_csv(index=False), file_name="crm_contacts.csv", mime="text/csv")