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