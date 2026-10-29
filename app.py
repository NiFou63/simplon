import plotly.express as px
import pandas as pd


données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')


# Création de la colonne chiffre d'affaires
données['ca'] = données['prix'] * données['qte']

# Graphique 1 : Quantité vendue par région (déjà existant)
figure_region = px.pie(données, values='qte', names='region', title='Quantité vendue par région')

# Graphique 2 : Ventes par produit (quantité totale)
figure_produit_qte = px.bar(
    données.groupby('produit')['qte'].sum().reset_index(), 
    x='produit', y='qte', color='produit',
    title='Quantité vendue par produit'
)

# Graphique 3 : Chiffre d'affaires par produit (prix * quantité)
figure_produit_ca = px.bar(
    données.groupby('produit')['ca'].sum().reset_index(), 
    x='produit', y='ca', color='produit',
    title='Chiffre d''affaires par produit'
)


# Sauvegarde des graphiques en HTML
figure_region.write_html('ventes-par-region.html')
figure_produit_qte.write_html('ventes-par-produit-quantite.html')
figure_produit_ca.write_html('ventes-par-produit-chiffre-affaires.html')

print('Graphiques générés avec succès !')
