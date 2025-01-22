import math

# Constante de gravité
g = 9.8

# Demander la vitesse initiale de la boule
# Demander la vitesse initiale de la boule
vitesse_initiale = float(input("Vitesse initiale (en m/s): "))

# Demander l'angle de lancement
angle = float(input("Angle de lancer (en degrés): "))

# Convertir l'angle en radians
angle_rad = angle*math.pi/180

# Calculer la distance maximale en x
distance_maximale = float((vitesse_initiale**2*math.sin(2*angle_rad)/g))
distance_finale = round(distance_maximale, 2)

# Afficher la distance maximale arrondie à 2 chiffres après la virgule
print("Distance parcourue:", str(distance_finale)+"m")

# Exemple:
# Pour une vitesse initiale de 10 m/s et un angle de 45 degrés
# La distance parcourue serait de 10.20m
