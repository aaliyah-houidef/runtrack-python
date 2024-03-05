nom_du_produit = "Captive"
prix_unitaire = 20
quantite_en_stock = 100

print(f"informations du produit :")
print(f"nom du produit : {nom_du_produit}")
print(f"prix unitaire : {prix_unitaire}")
print(f"quantite en stock : {quantite_en_stock}")

augmentation_prix = 0.10
prix_unitaire *= (1+augmentation_prix)

print(f"\ninformations du produits apres l'inflation :")
print(f"nom du produit : {nom_du_produit}")
print(f"nouveau prix unitaire (apres inflation) : {prix_unitaire} euros")
print(f"quantite en stock: {quantite_en_stock} unités" )

quantite_demandee = int(input("\ncombien d\'unites souhaitez-vous acheter? :"))

if quantite_demandee <= quantite_en_stock:

    quantite_en_stock -= quantite_demandee
    montant_total = quantite_demandee * prix_unitaire
    print(f"\nachat reussi ! vous avez achete {quantite_demandee} unites pour un montant de {montant_total} euros.")
    print(f"quantite restante en stock : {quantite_en_stock} unites")
else:
    print("achat impossible. la quantite demandee n'est pas disponible en stock.")
    
ajout_en_stock = int(input("\ncombien de produits souhaitez vous ajouter au stock? :"))
quantite_en_stock += ajout_en_stock
stock_apres_ajout = ajout_en_stock + quantite_en_stock
stock_apres_ajout = quantite_en_stock
print(f"vous venez d\'ajouter {ajout_en_stock} unites!")
print(f"stock apres ajout {stock_apres_ajout}")