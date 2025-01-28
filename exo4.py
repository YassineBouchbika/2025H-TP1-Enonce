import math
secondes = int(input("Entrez un nombre de secondes : "))
resteDeSeconde = 0
# Ne pas modifier.
annees = semaines = jours = heures = minutes = 0

# TODO: Assigner à la variable "annees" le nombre d'années
annees = math.floor(secondes / (60*60*24*365))
# TODO: Assigner à la variable "semaines" le nombre de semaines restantes
resteDeSeconde = (secondes % (60*60*24*365))
semaines = math.floor(resteDeSeconde / (60*60*24*7))
# TODO: Assigner à la variable "jours" le nombre de jours restants
resteDeSeconde = resteDeSeconde % (60*60*24*7)
jours = math.floor(resteDeSeconde / (60*60*24))
# TODO: Assigner à la variable "heures" le nombre d'heures restantes
resteDeSeconde = resteDeSeconde % (60*60*24)
heures = math.floor(resteDeSeconde / (60*60))
# TODO: Assigner à la variable "minutes" le nombre de minutes restantes
resteDeSeconde = resteDeSeconde % (60*60)
minutes = math.floor(resteDeSeconde / (60))
# TODO: Assigner à la variable "secondes" le nombre de secondes restantes
resteDeSeconde = resteDeSeconde % (60)
secondes = math.floor(resteDeSeconde)
# TODO: Afficher le nombres d'années, semaines, jours, heures, minutes et secondes
# Exemple: print(annees, semaines, jours, heures, minutes, secondes)
print(annees, semaines, jours, heures, minutes, secondes)

#print(str(annees) + " an(s), " + str(semaines) + " sem(s), " + str(jours) + " jour(s), " + str(heures) + " heure(s), " + str(minutes) + " minute(s), " + str(secondes) + " secondes(s), " )
