# %%
# instanciation litérale

dico = {
    "k": "v",
    3.14: "pi",
    (-2.13, 43.34543): "PARIS",
    2: [1, 2, 3]
}

# accès aux valeurs par clé
dico["k"], dico[(-2.13, 43.34543)]
# %%
# similitude entre un dico et une liste de tuples
items = [("k1", "v1"), ("k2", "v2")]

dico = dict(items)
# %%
# 3 façons de boucler sur un dico
list(dico)
for k in dico:
    print(k)

dico.values()
for v in dico.values():
    print(v)

dico.items()
for k, v in dico.items():
    print(k,v)
# %%
# à partir de 2 listes
keys = ["k1", "k2"]
values = ["v1", "v2"]

dico = dict(zip(keys, values))
# %%
if "k3" in dico:
    dico["k3"]
else:
    "dflt"

dico.get("k3", "dflt")

del dico["k1"]
dico
# %%
