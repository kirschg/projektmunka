def paros(szam):
    if szam%2!=0:
        return True
    else:
        return False
#főprogram
x=int(input("Kérek egy számot! "))
while paros(x):
    print("Ez a szám nem páros.")
    x=int(input("Kérek egy számot! "))
print("Ez a szám páros.")