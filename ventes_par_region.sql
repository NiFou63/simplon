SELECT 
    region, 
    SUM(qte) AS total_quantite_vente, 
    SUM(prix * qte) AS chiffre_d_affaires_region
FROM ventes
GROUP BY region;
