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
    voltage = 0 
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
Resistance.voltage, res.voltage
# %%

class Resistance:
    # attributs de classes
    # voltage = None 
    # current = None

    # initialiseur
    def __init__(self, voltage: int, current: int) -> None:
       # attributs d'instance
       self.voltage = voltage
       self.current = current
    
    def get_resistance(self):
        return self.voltage / self.current

# effet de l'init
res = Resistance(voltage=1000, current=1000) 
res.get_resistance()

# %%
# attributs privés et publics
import math

class Resistance:

    def __init__(self, voltage: int, current: int) -> None:
       # attributs privés
       # préfixés par "__"
       # uniquement accessibles et réaffectable dans la classe
       self.__voltage = voltage
       self.set_current(current)
    
    # méthode publique: point d'entrée
    def set_current(self, current: int):
        if current != 0:
            self.__current = current
        else:
            raise ValueError("courant nul !!!")
    
    def get_resistance(self):
        return self.__voltage / self.__current


if __name__ == "__main__":
    # gestion d'erreur: capture d'exceptions
    try:
        res = Resistance(voltage=1000, current=0) 
        # pb des attributs publics, donc accessible et réaffectable depuis
        # l'extérieur de la classe
        # res.current = 0
        # res.set_current(1000)
        res.get_resistance()
    except Exception as e:
        print(e)
# %%
# version alternative
import logging
import math
class Resistance:

    def __init__(self, voltage: int, current: int) -> None:
       self.__voltage = voltage
       self.set_current(current)
    
    # méthode publique: point d'entrée
    def set_current(self, current: int):
        self.__current = current
    
    def get_resistance(self):

        if not self.__current:
            logging.error("courant nul !!")
            return math.inf
        return self.__voltage / self.__current

if __name__ == "__main__":
    logging.basicConfig(
        filename="error.log",
        level=logging.ERROR,
        format="%(asctime)s: %(message)s", 
        datefmt="%Y/%m/%d %I:%M")
    
    res = Resistance(1000, 0)
    print(res.get_resistance())
# %%
