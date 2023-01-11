# la bibliothèque numpy ne marche pas, je vais donc utiliser la bibliothèque random
import random
import matplotlib.pyplot as plt
tirages = []
histo = []
temp = 0
x = int(input("Entrez le nombre de tirages :"))
seed = int(input("Entrez la seed :"))
random.seed(seed)

for i in range(x):
    print("tirage n°", i+1)
    for j in range(0, 5):
        n = int(random.uniform(1, 46))
        tirages.append(n)
    tirages = list(set(tirages))

    while len(tirages) != 5:
        n = int(random.uniform(1, 46))
        tirages.append(n)
        tirages = list(set(tirages))
    for k in range (0, 5):
        histo.append(tirages[k])
    print(tirages)
    tirages = []
    print("---------------------------")
plt.hist(histo, 45, edgecolor = "black")
plt.xlabel("Numéros")
plt.ylabel("Nombres de tirages")
plt.title("Tirages du loto")
plt.show()
# il y'a 1221759 combinaisons possibles par tirages
