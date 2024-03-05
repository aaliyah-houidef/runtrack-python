montant_initial_de_l_investissement = 20000
taux_de_rendement_annuel = 5

gain_annuel = (montant_initial_de_l_investissement * taux_de_rendement_annuel) / 100
print(f"le gain annuel est de {gain_annuel} euros")

montant_initial_de_l_investissement += 5000
taux_de_rendement_annuel += 2

nouveau_gain_annuel = (montant_initial_de_l_investissement * taux_de_rendement_annuel) / 100
print(f"le nouveau gain annuel est de {nouveau_gain_annuel} euros")

retraitinvest = 10
montant_final_investissement = montant_initial_de_l_investissement - (montant_initial_de_l_investissement*retraitinvest/100)
retraitrend = 1
rendedement_final_annuel = taux_de_rendement_annuel - (taux_de_rendement_annuel*retraitrend/100)

gain_final = (montant_final_investissement*rendedement_final_annuel)/100
print(f"le gain final est de {gain_final}euros")