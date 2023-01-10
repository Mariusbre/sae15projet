# la bibliothèque numpy ne marche pas, je vais donc utiliser la bibliothèque random
import random
print("Entrez le nombre de tirages :")
tirages = []
x = int(input())
random.seed(5)
for i in range(x):
    print("tirage n°", i+1)
    for j in range(0, 5):
        n = int(random.uniform(1, 46))
        tirages.append(n)
    tirages = list(set(tirages))
    if len(tirages) != 5:
        n = int(random.uniform(1, 46))
        tirages.append(n)
    print(tirages)
    tirages = []
    print("____________")
# il y'a 1370754 combinaisons possibles par tirages
