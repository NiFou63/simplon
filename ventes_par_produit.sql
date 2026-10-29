SELECT 
    produit, 
    SUM(qte) AS total_quantite_vente, 
    SUM(prix * qte) AS chiffre_d_affaires_produit
FROM ventes
GROUP BY produit;
