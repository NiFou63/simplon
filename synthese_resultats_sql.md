# Synthèse des résultats d’analyse obtenus

## Le chiffre d'affaires total

```sql
select sum(prix*qte) as chiffre_affaires_total from ventes
```
Après une commande select, on indique le résultat à obtenir par colonne.
Ici on aura une colonne chiffre_affaires_total
Comme on utilise la fonction sum, sql va parcourir chaque ligne de la table et sommer le résultat de la multiplication des colonnes prix et qte


## Les ventes par produit

```sql
SELECT 
    produit, 
    SUM(qte) AS total_quantite_vente, 
    SUM(prix * qte) AS chiffre_d_affaires_produit
FROM ventes
GROUP BY produit;
```
Après une commande select, on indique le résultat à obtenir par colonne.
Ici on aura une colonne produit, une colonne total_quantite_vente et une colonne chiffre_d_affaires_produit
Comme on indique en sortie la colonne produit existante, sql sait que les colonnes calculées qui suivent doivent être calculées par produit et la commande "group by" est essentielle pour indiquer de le faire en groupant par produit, sinon on aurait un cumul de tout sur le premier produit rencontré dans les lignes de la table.


## Les ventes par région.
```sql
SELECT 
    region, 
    SUM(qte) AS total_quantite_vente, 
    SUM(prix * qte) AS chiffre_d_affaires_region
FROM ventes
GROUP BY region;
```
Même principe que la requête précédente sauf qu'on le fait par région