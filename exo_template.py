# %%
# exercice : remplacer les clés entourées par "((" et "))"
# dans un texte par les valeurs correspondantes dans un dico

# 1. afficher le contenu entre la première occurence de (( et ))
# 2. remplacer ((key1)) par content1 dans _template
# Hint: regarder la fonction str.replace
# 3. itérer sur _template pour remplacer toutes les slots (())
# par la clé correspondante si celle ci existe ou par N/A

_template = """
lorem ipsum (blabla) ... ((key1)) blabla ....
lorem ipsum (blabla) ... ((key2)) blabla ....
lorem ipsum (blabla) ... ((key3)) blabla ....
lorem ipsum (blabla) ... ((key4)) blabla ....
"""

injections = {
    "key1": "content1",
    "key2": "content2",
    "key3": "content3"
}
# %%
while "((" in _template:
    start_index = _template.index("((") + len("((")
    end_index = _template.index("))")
    key = _template[start_index:end_index]

    _template = _template.replace(
        "((" + key +"))", 
        injections.get(key, "N/A")
    )
# %%
# portage en fonction

# tpl, values: paramètres positionnels / obligatoires
# slot, default: paramètres nommés / optionnels

# : str, ..., : tuple= ...: annotations 
# => purement informatif
# => aide à l'autocomplétion dans les fonctions
def parse_template(tpl: str, values: dict, slot: tuple=("{{", "}}"), default: str="N/A") -> str:
    """
    moteur de template light pour injection de variables
    @param tpl: ...
    """
    while slot[0] in tpl:
        start_index = tpl.index(slot[0]) + len(slot[0])
        end_index = tpl.index(slot[1])
        key = tpl[start_index:end_index]

        tpl = tpl.replace(
            slot[0] + key + slot[1], 
            values.get(key, default)
        )
    return tpl
# %%
# modes d'appels
# appel positionnel
# parse_template(_template, injections, ('((', '))'))
# appel nommé: plus besoin d'ordre
# mais pas d'appel positionnel après des appels nommés
parse_template(_template, values=injections, slot=('((', '))'))

# %%
# annotations + doc
dir(parse_template)
parse_template.__annotations__
parse_template.__doc__
# %%
# *: tout ce qui est à droite doit être nommé à l'appel
# **kwargs: arguments nommés de nb inconnu, optionnels
# arguments placés dans un dictionnaire dans le corps de la fonction
def sql_connect(*,
        host, username, passwd, db_name, 
        port=3306, encoding="utf-8", **opts):
    """
    connexion bdd
    arguments **
    debug: True | False: mode debug
    """
    if "debug" in opts and opts["debug"]:
        print(host, username)

sql_connect(
    host="localhost", 
    username="root", 
    passwd="123456!", 
    db_name="project",
    debug=True)
# %%

# arguements *args: généralisation à n paramètres
# ces arguments sont positionnels, mais on ne connaît pas leur nb
print("un")
print("un", "deux")

def add(a, b):
    return a + b

def add(*nums):
    print(nums, type(nums))
    return sum(nums)

add(1, 2)
add(1, 2, 3, 5)

nbs = (1, 2, 3, 5)

# %%
# utilisation des *args à l'appel
# dispatche une liste ou un tuple dans les arguments d'une fonction
def func(p1, p2):
    return p1, p2

func(*["p1", "p2"])
# %%
