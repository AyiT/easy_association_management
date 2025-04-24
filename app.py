import streamlit as st
import pandas as pd
import datetime

st.set_page_config(page_title="Easy Asso")

# Charger les données
@st.cache_data
def load_data():
    try:
        df = pd.read_csv("data/export-paiements-yin-ko-02_06_2021-25_04_2025.csv",sep=";")
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Référence commande", "Référence paiement", "Montant total", "Date du paiement", "Statut du paiement", "Versé", "Date du versement", "Nom payeur", "Prénom payeur", "Email payeur", "Date de naissance", "Raison sociale", "SIREN", "Forme juridique", "Campagne", "Type de campagne", "Type", "Montant du tarif", "Montant des options", "Don supplémentaire", "Code Promo", "Montant du code promo", "Moyen de paiement", "Attestation", "Reçu fiscal", "Numéro de reçu", "Adresse payeur", "Code Postal payeur", "Ville payeur", "Pays payeur", "Commentaire"
        
])
       
    return df

df = load_data()



#Tableau Adhérents
st.title("Payement")

filtre_statut = st.selectbox("Filtrer par statut", options=["Tous"] + list(df["Campagne"].unique()))
if filtre_statut != "Tous":
    df = df[df["Campagne"] == filtre_statut]

filtre_statut = st.selectbox("Filtrer par statut", options=["Tous"] + list(df["Statut du paiement"].unique()))
if filtre_statut != "Tous":
    df = df[df["Statut du paiement"] == filtre_statut]



#filtre_etat = st.selectbox("Filtrer par état", options=["Tous"] + list(df["etat"].unique()))
#if filtre_etat != "Tous":
#   df = df[df["Etat"] == filtre_etat]

st.dataframe(df)

aujourdhui = datetime.date.today()
#relances = df[df["Relancer le"] <= pd.to_datetime(aujourdhui)]

#if not relances.empty:
#    st.warning("📌 Contacts à relancer aujourd’hui ou en retard :")
#    st.table(relances[["Nom", "Email", "Relancer le"]])


#Bouton de relance
st.download_button("📤 Exporter en CSV", df.to_csv(index=False), file_name="crm_contacts.csv", mime="text/csv")