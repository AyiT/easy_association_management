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
    new_row = pd.DataFrame([[nom, email, tel, statut, etat, note, dernier_contact, relance]], columns=df.columns)
    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv("contacts.csv", index=False)
    st.success("Contact ajouté !")