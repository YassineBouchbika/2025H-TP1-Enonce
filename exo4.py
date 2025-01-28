import math
secondes = int(input("Entrez un nombre de secondes : "))
resteDeSeconde = 0
# Ne pas modifier.
annees = semaines = jours = heures = minutes = 0

# TODO: Assigner à la variable "annees" le nombre d'années
annees = math.floor(secondes / (60*60*24*365))
resteDeSeconde = (secondes % (60*60*24*365))
print("le reste est: ", resteDeSeconde)
# TODO: Assigner à la variable "semaines" le nombre de semaines restantes
semaines = math.floor(resteDeSeconde/ (60*60*24*7))
resteDeSeconde = (secondes % (60*60*24*365))
# TODO: Assigner à la variable "jours" le nombre de jours restants
jours = math.floor(secondes % ((60*60*24*7) / (60*60*24*7)))
# TODO: Assigner à la variable "heures" le nombre d'heures restantes

# TODO: Assigner à la variable "minutes" le nombre de minutes restantes

# TODO: Assigner à la variable "secondes" le nombre de secondes restantes

# TODO: Afficher le nombres d'années, semaines, jours, heures, minutes et secondes
# Exemple: print(annees, semaines, jours, heures, minutes, secondes)
print(str(annees) + " an(s), " + str(semaines) + " sem(s), " + str(jours) + " jour(s), " )
