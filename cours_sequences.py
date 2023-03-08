# %%
# points communs entre str, list et tuples
# accès aux valeurs par l'opérateur []

# attention: ne pas redéfinir les classes, les fonctions, etc
# print = 2
# str = "coucou"
# unpacking d'affectation
_str, nums = "abcde", [1, 2, 3, 4, 5]
tup = (_str, nums)

# unpacking de variable
_str[0], nums[-1]
# %%

# même comportement vis à vis de certains opérateurs
# fonctions globales

# + concatenation
# répétition
3 * "rien", [0] * 10

# élément dans ensemble

print("de" in _str, 6 not in nums, nums in tup)
[1, 2] in nums
# %%
# fonctions globales
len(_str), len(nums)
# quand c'est possible
min(nums), sum(nums)
# %%
# index et nb d'occurences
expr = "à bon chat bon rat"
expr.index("bon")
expr.index("bon", expr.index("bon") + 1)
expr.count("bon")
# %%
# opérateur de slicing

words = ["un", "tiens", 'vaut', "mieux", 'que', 2]
# indice de début compris, fin non compris
words[1:5]
words[:4]
words[2:]
words[::2]
words[::-1]
# %%
# pour élément dans ensemble
for letter in expr:
    print(letter.upper())

for word in words:
    print(word)
# %%
# itération sur gamme d'entiers
for i in range(10):
    print(i**2)
# %%
# itérer avec l'index et la valeur
# i = 0
for index, word in enumerate(words[:-1]):
    words[index] = word.upper()
    # i += 1
words
# %%
sentence = "bonjour tout le monde"
words = sentence.split()
words

for index, word in enumerate(words):
    words[index] = word.upper()

new_sentence = " ".join(words)
new_sentence
# %%
