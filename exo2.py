# Demandez à l'utilisateur d'entrer le niveau de charge actuel de la batterie
niveau_de_charge = float(input("Entrez le niveau de charge actuel de la batterie : "))
# Vérifiez si le niveau de charge est valide
if (niveau_de_charge<0) or (niveau_de_charge>100):
    print("Erreur : niveau de charge invalide.")
else: 
# Arrondir le pourcentage à la dizaine la plus proche
    niveau_de_charge_arrondi = round(niveau_de_charge)

# Calculer le nombre de barres
    nombre_de_barres = int(round(niveau_de_charge_arrondi/10))
    espace_vide = 10 - nombre_de_barres

# Afficher la représentation graphique de la charge de la batterie
    batterie = "[" + "❚"*nombre_de_barres + " "*espace_vide + "]"
    print(batterie)
    print(str(int(niveau_de_charge))+"%")


            
            



# Exemple d'utilisation :
# Si l'utilisateur entre 76, la sortie sera :
# [❚❚❚❚❚❚❚❚     ]
# 76%