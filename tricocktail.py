tri = []
print("Entrez les valeurs à trier")
for i in range(10):
    tri.append(int(input()))

debut = 0
temp = True
fin = len(tri)-1
while temp:
    temp = False
    for j in range(debut, fin):
        if tri[j] > tri[j+1]:
            tri[j], tri[j+1] = tri[j+1], tri[j]
            temp = True
    for j in range(len(tri)-2, -1, -1):
        if tri[j] > tri[j+1]:
            tri[j], tri[j+1] = tri[j+1], tri[j]
            temp = True

print(tri)