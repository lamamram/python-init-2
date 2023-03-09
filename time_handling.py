# %%
from datetime import datetime, timedelta

# %%
# instanciations
values = [2023, 3, 9, 16, 32]
dt = datetime(*values)

now = datetime.now()
now

# p pour parse str
dt = datetime.strptime("2023-03-09 16:33", "%Y-%m-%d %H:%M")
dt.strftime("%d/%m/%Y")

# timestamp: nb de second depuis le 1er jancier 1970 à 00:00:00.000
# Temps UNIX
dt = datetime.fromtimestamp(53 * 86400 * 365)
dt
# %%
# gestion de durées

milestone = datetime(2023, 4, 14, 14)
remains = milestone - datetime.now()
remains

# %%
cuisson_oeuf_coque = timedelta(minutes=3)

a_table = datetime.now() + cuisson_oeuf_coque
a_table
# %%
