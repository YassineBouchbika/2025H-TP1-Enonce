# Demandez à l'utilisateur d'entrer le niveau de charge actuel de la batterie
niveau_de_charge = int(input("Entrez le niveau de charge actuel de la batterie : "))
# Vérifiez si le niveau de charge est valide
if (niveau_de_charge<0) or (niveau_de_charge>100):
    print("Erreur : niveau de charge invalide.")
else: 
    
# Arrondir le pourcentage à la dizaine la plus proche
    niveau_de_charge_arrondi = round(niveau_de_charge, -1)
 

# Calculer le nombre de barres
    nombre_de_barres = niveau_de_charge_arrondi/10
 

# Afficher la représentation graphique de la charge de la batterie
    batterie = ""
    for i in range(0, 10+1):
        if (i == 0):
            batterie+= "["
        if (i >= 10):
            batterie+="]"
        if (i>=0) and (i<nombre_de_barres):
            batterie+="❚"
        else:
            batterie+=" "
    
    print(batterie)
    print(str(niveau_de_charge)+"%")


            
            



# Exemple d'utilisation :
# Si l'utilisateur entre 76, la sortie sera :
# [❚❚❚❚❚❚❚❚     ]
# 76%