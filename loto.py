# la bibliothèque numpy ne marche pas, je vais donc utiliser la bibliothèque random
import random
print("Entrez le nombre de tirages :")
x = input(int())
random.seed(486)
for i in range(8):
    for i in range(0, 5):
        n = int(random.uniform(1, 46))
        print(n)
    print("___")