szam= int(input("Hány órás visszaszámlálást tervezünk? "))
for x in range (szam, 0, -1):
    print("Visszaszámlálás: ", x)
    if input("Fel kell függeszteni a visszaszámlálást (i/n)? ")=="i":
        szam+=1
print("A rakéta a visszaszámlálást követően ennyi órával indult:", szam)