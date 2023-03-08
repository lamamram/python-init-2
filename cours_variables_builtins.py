# %%
# convention de nommage
# snake_case pour tout sauf les classes
# PascalCase: pour les classe
# camelCase, kebab-case: niet
# ALL_CAPS : pour les "pseudo" constantes


# pas de déclaration
# création à l'initialisation, i.e la 1ère affectation
ma_variable = "coucou"
# emplacement mém. géré par l'interpréteur
print(id(ma_variable))
# typage dynamique
ma_variable = "oucouc"
print(id(ma_variable))

PI = 3.14159
# %%
# fonctions / mots clés fondamentaux
# affichage sortie standard
print("bonjour", PI + 2, ma_variable)

# saisie depuis l'entrée standard
msg = input("veuillez entrer un message: ")
# "type" d'une variable
# EN PYTHON, TOUT EST OBJECT
print(msg, type(msg))

# %%
# introspection des variables

ma_variable = "coucou"
# liste des attributs d'un objet de classe str
dir(ma_variable)
ma_variable.upper()

# documentation des variables
help(str.upper)
# %%
print("passage par référence")
# emplacment mém.
x = 10
# passage par référence
y = x
print(id(x), id(y))
print(x is y)
x = 20
print(x is y, id(x), id(y))

print("optimisation mém.")

x = 1
y = 1
x is y


# %%
# suppression d'une variable
ma_variable = "coucou"
del ma_variable
print(ma_variable)

# %%
# bestiaire des built ins
# "scalaires"
print(777, type(777))
print(3.14, type(3.14))
print("ok", type("ok"))
print(False, type(False))
print(2j + 1, type(2j + 1))

# structures
# liste: types variables, indexables, itérables
print([1, 2.5, "Hi"], type([1, 2.5, "Hi"]))

# tuple: types variables, indexables, itérables
# ... mais non modifiables
print((1, 2.5, "Hi"), type((1, 2.5, "Hi")))
# dictionnaires: esemble de paires clé / valeur
# accès aux valeurs par des clés de types variable
# non indexable, itérable
print({"key": "value"}, type({"key": "value"}))

# set: ensemble de valeurs uniques: non indexable, itérable
print({"pomme", "poire"}, type({"pomme", "poire"}))


# %%
# peu de conversion implicites
1 + 3.14
# concaténation
"numéro" + str(1)

# concaténation de liste 
# et conversion tuple => liste
list("numéro") + list(("uno",))

# dédoublonnage avec conversion list => set
set([1, 1, 2, 2, 4])
# %%
# 1. saisir un entier compris entre 0 et 86400 (sans contrôle)
# 2. afficher l'heure qu'il est à partir de minuit
# il est xh ymn zs
entry = input("saisir un entier entre 0 et 86400: ")
entry = int(entry)

nb_heures = entry // 3600
nb_minutes = ( entry % 3600 ) // 60
nb_secondes = entry % 60

# suboptimal
# print("il est " + str(nb_heures) + "h " + str(nb_minutes) + "mn")
# print("il est", nb_heures, "h", nb_minutes, "mn")

# templating python2
# print("il est %dh %dmn" % (nb_heures, nb_minutes))

# templating python3
# print("il est {hour}h {min}mn, soit {sec:.2f}".format(hour=nb_heures, min=nb_minutes, sec=entry/3600))

# f-strings
print(f"il est {nb_heures}h {nb_minutes}mn, soit {entry/3600:.2f}h")
# %%
entry = "10000"
# vérifier que entry est une chaine numérique de type entier naturel
if entry.isnumeric():
    entry = int(entry)
    # if 0 <= entry and entry < 86400:
    if 0 <= entry < 86400:
        print("bonne valeur")
    elif entry >= 86400:
        print("hors range !!")
else:
    print(f"{entry} non convertible en int !")
# %%
# opérateur ternaire
# cond = True
cond = 10 < 20
# toutes les valeurs fausses
# 0, 0., "", [], (), {}, set(), False, None
if not cond:
    param = 10
else:
    param = 20

# en c: param = cond ? 10 : 20;
param = 10 if not cond else 20
param
# %%
# %%
# retourne la premère valeur vraie
None or 20

# retourne la dernière valeur vraie
"bonjour" and "les gens"
# %%

# mutables vs immutables
_str, lst = "abcde", [1, 2, 3]
# mutable: opération interne qui ne change pas l'emplacement mém.
print(id(lst))
lst[0] = -1
lst, id(lst)

# immutabilité: impossible de changer en interne
# on change par réafecctation de la variblae contenant
# (1, 2, 3)[0] = -1
# _str[0] = "A"

_str = _str.capitalize()
_str
# %%
# ATTENTION au passage par référence
# pour les mutables => list et dict
lst = [1, 2, 3]
# avec les mutables les opération internes modifient toutes les variables
# qui référence l'emplacement mém.
lst2 = lst
# copie creuse, i.e indépendante en mém.
lst3 = lst.copy()
# idem: lst3 = lst[:]
lst2.append(4)
lst3.append(4)
lst is lst2, lst is lst3
# %%
