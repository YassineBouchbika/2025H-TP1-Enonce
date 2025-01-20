# Demander le nom complet de l'utilisateur
nom_complet = input("Veuillez entrer votre nom complet: ")
# Demander l'âge de l'utilisateur
âge = int(input("Veuillez entrez votre âge: "))

# Définir l'année actuelle
année_actuelle = 2025
# Calculer l'année de naissance
année_de_naissance = année_actuelle-âge

# Afficher un message de bienvenue avec le nom complet
print("Bonjour", nom_complet)
# Afficher l'année de naissance
print(année_de_naissance)