szam= int(input("Hány óra van most? "))
if szam <16 and szam >=8:
    print("A bolt nyitva van.\nEnnyi órád van még odaérni: ", abs(szam-16))
else:
    print("A bolt zárva van.")