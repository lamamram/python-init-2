# %%
# read /write: haut niveau:  on manipule des strings
# on compte des caractères
f = open(
    "./test_fic.txt", "w", 
    encoding="utf-8")
print(f.write("fèrst row\nsecond row\n"))
f.close()

f = open(
    "./test_fic.txt", "r", 
    encoding="utf-8")
print(f.read(10))
print(f.read(11))
f.close()
# %%
# bas niveau: ouverture en binaire
f = open(
    "./test_fic.txt", "wb")
# raw_str = bytes("frist row\nsecond row\n", "utf-8")
raw_str = b"frist row\nsecond row\n"
print(f.write(raw_str))
f.close()

f = open(
    "./test_fic.txt", "rb")
print(f.read(10))
print(f.read(11))
f.close()
# %%
# gestionnaire de contexte
with open(
    "./test_fic.txt", "r", 
    encoding="utf-8") as f:
    print(f.read(10))
# fichier fermé en sortie de bloc
# f.read(11)
# %%
# les fichiers sont des itérables
with open(
    "./test_fic.txt", "r", 
    encoding="utf-8") as f:
    # for line in f:
    #    print(line)
    print(list(f))
# %%
# itération pas à pas
with open(
    "./test_fic.txt", "r", 
    encoding="utf-8") as f:
    print(next(f))
    for row in f: print(row)
# %%
# conversion de données tabulaires en json
import json
header = ["id", "name", "age"]

data = [
    [1, "joe", 24],
    [2, "jane", 33]
]

# {"id": 1, "name": "joe", "age": 24}
# dans la lambda, header est un paramètre libre
records = list(map(lambda r : dict(zip(header, r)), data))

with open("users.json", "w", encoding="utf-8") as json_f:
    json.dump(records, json_f, indent=2)

json.dumps(records, separators=(",", ":"))
# %%
