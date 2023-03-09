import re
## attention, les chemins d'imports sont calculés
# depuis le programme PRINCIPAL
# chemin global depuis la racine du projet
from utils.helpers.decorators import type_ctrl
# chemin relatif
# from .helpers.decorators import type_ctrl

INT_PATTERN = "^-?[0-9]+$"

def is_int(_str: str) -> bool:
     return (
          _str.isnumeric()
          or _str.startswith("-") and _str[1:].isnumeric())

# strictement équivalent à:
# calcul_moyenne = type_ctrl(calcul_moyenne)

@type_ctrl
def calcul_moyenne(values: list, precision: int=2):
    # filtered = list(filter(is_int, values))
    filtered = list(filter(
        lambda v: re.match(INT_PATTERN, v), 
        values))
    converted = list(map(int, filtered))
    issues = list(set(values) - set(filtered))
    print(issues)
    return round(sum(converted)/len(converted), precision)


# planquer des tests
if __name__ == "__main__":
     calcul_moyenne(["0"])