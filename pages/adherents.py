import streamlit as st
import pandas as pd
import datetime

st.set_page_config(page_title="Easy Asso")

# Charger les données
@st.cache_data
def load_data():
    try:
        df = pd.read_csv("contacts.csv")
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Nom", "Email", "Téléphone", "Statut", "Etat", "Note", "Dernier contact", "Relancer le"])
    return df

df = load_data()

#ajout contact
st.sidebar.header("Ajouter un contact")

with st.sidebar.form(key="add_contact"):
    nom = st.text_input("Nom")
    email = st.text_input("Email")
    tel = st.text_input("Téléphone")
    statut = st.text_input("Statut (adhérent, prospect, résilié)")
    etat = st.text_input("Etat (actif, inactif...)")
    note = st.text_area("Note")
    dernier_contact = st.date_input("Dernier contact", datetime.date.today())
    relance = st.date_input("Relancer le", dernier_contact + datetime.timedelta(days=30))
    submit = st.form_submit_button("Ajouter")

if submit:
    new_row = pd.DataFrame([[nom, email, tel, tag, note, dernier_contact, relance]], columns=df.columns)
    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv("contacts.csv", index=False)
    st.success("Contact ajouté !")


#Tableau Adhérents
st.title("Adhérents")

filtre_statut = st.selectbox("Filtrer par statut", options=["Tous"] + list(df["Statut"].unique()))
if filtre_statut != "Tous":
    df = df[df["Statut"] == filtre_statut]

filtre_etat = st.selectbox("Filtrer par état", options=["Tous"] + list(df["Etat"].unique()))
if filtre_etat != "Tous":
   df = df[df["Etat"] == filtre_etat]

st.dataframe(df)

aujourdhui = datetime.date.today()
relances = df[df["Relancer le"] <= pd.to_datetime(aujourdhui)]

if not relances.empty:
    st.warning("📌 Contacts à relancer aujourd’hui ou en retard :")
    st.table(relances[["Nom", "Email", "Relancer le"]])


#Bouton de relance
st.download_button("📤 Exporter en CSV", df.to_csv(index=False), file_name="crm_contacts.csv", mime="text/csv")