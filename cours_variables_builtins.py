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
