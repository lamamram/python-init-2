# %%
# programme principal
## import avec espace de nom
# import tools
## import sans espace de nom
# écriture + rapide mais conflit de nom possible
# aliasing possible pour régler les conflits

## dans les 2 cas, TOUT le contenu du module est exécuté
from tools import parse_template as parse_tpl

parse_template = 0

tpl = """
name: {{name}}
age: {{age}}
"""

user = {"name": "LAMAM", "age": 40}

# tools.parse_template(tpl, user)
parse_tpl(tpl, user)

# %%
