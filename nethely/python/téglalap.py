import math
def kerulet(a,b):
    ossz = 2*(a+b)
    return ossz
def terulet(a,b):
    ossz =a*b
    return ossz
def atlo(a,b):
    ossz =math.sqrt(a*a+b*b)
    return ossz
#főprogram
x = int(input("Adja meg az a oldalát a teglalapnak!"))
y = int(input("Adja meg a b oldalát a téglalapnak!"))
print("K:",kerulet(x,y),"\nT:",terulet(x,y),"\nd:",atlo(x,y))