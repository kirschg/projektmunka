x= int(input("Kérek egy számot "))
szam = int(input("Kérek egy másik számot "))
if szam==x:
    print("A két szám egyenlő")
else:
    print("A nagyobb szám: ", max(x,szam))