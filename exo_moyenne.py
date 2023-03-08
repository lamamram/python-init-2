# %%
# faire un calcul de moyenne arithmétique
# 1. saisir d'un coup une série de nombres espacé par "," avec input
# ex. de saisie: 1,2.6,truc,...
# 2. analyser chaque valeur de la saisie pour déterminer s'il s'agît
# d'un nombre (commencer par entier, puis entier relatif)
# HINT: regarder la fonction str.isnumeric()
# 3. les valeurs numériques sont converties dans la même liste
# 4. calcul de la moyenne, 
# uniquement s'il n'y a pas eu erreur de saisie

DELIM = ","
# values = input(f"veuillez saisir des entiers sépars par {DELIM}: ").split(DELIM)
values = input(f"veuillez saisir des entiers sépars par {DELIM}: ")
values = values.split(DELIM)
issues = []
for i, val in enumerate(values):
    # if val.isnumeric() or val[0] == "-" and val[1:].isnumeric():
    if val.isnumeric() or val.startswith("-") and val[1:].isnumeric():
        values[i] = int(val)
    else:
        issues.append(val)

if not issues and values:
    moy = sum(values) / len(values)
    print(f"moyenne de {values}: {round(moy, 2)}")
else:
    print(f"{set(issues)}: pas des ints !")

# %%
import sys
# idem en interrompant la boucle dès qu'une erreur de conversion survient
DELIM = ","
values = input(f"veuillez saisir des entiers sépars par {DELIM}: ")
values = values.split(DELIM)
if not values:
    print("liste vide!!")
    sys.exit(0)

for i, val in enumerate(values):
    # if val.isnumeric() or val[0] == "-" and val[1:].isnumeric():
    if val.isnumeric() or val.startswith("-") and val[1:].isnumeric():
        values[i] = int(val)
    else:
        print(f"{val} non convertible !!")
        break
# si la boucle se termine normalement
# for: l'itérable est entièrement consommé
# while: on sort sur la condition fausse
# => si on ne rencontre jamais break
else:
    moy = sum(values) / len(values)
    print(f"moyenne de {values}: {round(moy, 2)}")

# %%
