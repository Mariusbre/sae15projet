tri = []
print("Entrez les valeurs à trier")
for i in range(6):
    tri.append(int(input()))
a = len(tri)
for i in range(1, a):
    temp = tri[i]
    while i > 0 and tri[i-1] > tri[i]:
        tri[i] = tri[i-1]
        i = i-1
        tri[i] = temp
print(tri)