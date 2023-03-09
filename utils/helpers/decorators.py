# décorteur = fonction
# qui prend en pramètre une fonction
# et qui retourne une fonction nommée "wrapper"
# qui rédéfinit la fonciton en paramètre
def type_ctrl(f):
    # signature universelle
    def wrapper(*a, **kw):
        # comportement ajouté
        for param, typ in f.__annotations__:
            print(param, typ) 
        ret = f(*a, **kw)
        # ...
        return ret
    return wrapper