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
# version en programmtion foncitonnelle
# filter filtre un itérable d'après les valeurs de retour d'une fonction
# sur ses éléments
# map applique une fonction à chaque élém. d'un itérable et retourne les
# données transformée

# pour des transformations en une expression
# on utilisera des lambda qui sont des fonctions sans noms, 
# => à usage unique
import re

int_pattern = "^-?[0-9]+$"

def is_int(_str: str) -> bool:
     return (
          _str.isnumeric()
          or _str.startswith("-") and _str[1:].isnumeric())

def calcul_moyenne(values: list, precision: int=2):
    # filtered = list(filter(is_int, values))
    filtered = list(filter(
        lambda v: re.match(int_pattern, v), 
        values))
    converted = list(map(int, filtered))
    issues = list(set(values) - set(filtered))
    print(issues)
    return round(sum(converted)/len(converted), precision)

calcul_moyenne(["1", "-4", "two"])
# %%
rows = ["row_1", "row_20", "row_13", "row_6"]
# rows.sort()
sorted(
    rows, 
    key=lambda r: int(r[4:]), 
    reverse=True
)

# %%
