# %%
# POO: programmation Orientée Objet
# but: fabriquer des objets métiers

# impératif
voltage, current = 1000, 1000

def resistance(u: int, i: int):
    return u / i

# %% 
# version objet
class Resistance:
    # attributs
    voltage = None 
    current = None

    # méthode = attribut de type function
    #les méthodes ont toujours self comme premier argument
    # self désigne l'objet instancié
    def get_resistance(self):
        return self.voltage / self.current

# instanciation
res = Resistance()
# affectation des attributs
res.voltage = 1000
res.current = 1000
# appel à la méthode get_resistance
# pas besoin de paramètre car self = res
res.get_resistance()
# %%
