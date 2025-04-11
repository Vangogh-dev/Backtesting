import pandas as pd
from datetime import datetime

# Lecture du fichier CSV sans header
df = pd.read_csv("tickers_selection_10yrs.csv", header=None)

# Renommer les colonnes pour plus de clarté.
df.columns = ["Amazon_Date", "Amazon_Price", "Apple_Date", "Apple_Price", "Microsoft_Date", "Microsoft_Price"]

# Si vous souhaitez une unique colonne 'Date', renommez 'Amazon_Date'.
df.rename(columns={"Amazon_Date": "Date"}, inplace=True)

def convert_excel_date(val):
    try:
        # Si la valeur est déjà numérique, on la retourne
        if isinstance(val, (float, int)):
            return val
        # Gestion spéciale pour le bug Excel : 2/29/1900
        if val == "2/29/1900":
            return 60
        dt = datetime.strptime(val, "%m/%d/%Y")
        return (dt - datetime(1899, 12, 31)).days
    except ValueError as e:
        print(f"Erreur lors de la conversion de la valeur {val}: {e}")
        return float('nan')  # ou choisir une autre stratégie de gestion d'erreur

# Appliquer la conversion sur la colonne Apple_Price
df["Apple_Price"] = df["Apple_Price"].apply(convert_excel_date)

# Créer le DataFrame final avec 1 colonne Date et 1 colonne par ticker
df_transformed = pd.DataFrame({
    "Date": df["Date"],
    "Amazon": df["Amazon_Price"],
    "Apple": df["Apple_Price"],
    "Microsoft": df["Microsoft_Price"]
})

# Sauvegarder le fichier transformé
df_transformed.to_csv("tickers_transformed.csv", index=False)

print("Fichier transformé créé: tickers_transformed.csv")
