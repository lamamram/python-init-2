# %%
# un module est un fichier d'extension .py
import re

INT_PATTERN = "^-?[0-9]+$"

def is_int(_str: str) -> bool:
     return (
          _str.isnumeric()
          or _str.startswith("-") and _str[1:].isnumeric())

def calcul_moyenne(values: list, precision: int=2):
    # filtered = list(filter(is_int, values))
    filtered = list(filter(
        lambda v: re.match(INT_PATTERN, v), 
        values))
    converted = list(map(int, filtered))
    issues = list(set(values) - set(filtered))
    print(issues)
    return round(sum(converted)/len(converted), precision)


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
            str(values.get(key, default))
        )
    return tpl

print("coucou")