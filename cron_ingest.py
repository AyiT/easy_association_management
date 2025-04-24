import pandas as pd
from datetime import datetime

SOURCE = "export-paiements-yin-ko-02_06_2021-25_04_2025.csv"
DEST = "contacts.csv"

def clean(df):
    df["Nom"] = df["Nom"].str.strip().str.title()
    df["Date ajout"] = datetime.today().strftime("%Y-%m-%d")
    return df

df = pd.read_csv(SOURCE)
df_clean = clean(df)

# Fusion intelligente avec l'existant
df_exist = pd.read_csv(DEST)
df_final = pd.concat([df_exist, df_clean]).drop_duplicates(subset=["Email"])
df_final.to_csv(DEST, index=False)