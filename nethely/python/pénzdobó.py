import random
def erme():
    return random.choice(["fej","írás"])
#főprogram
x=0
for szam in range (1,4):
    y=erme()
    if input("Érme fel lett dobva, fej vagy írás?(fej/írás) ") ==y:
        print("Helyes tipp,", y, "volt.")
        x+=1
    else:
        print("Nem találtad el,",y,"volt.")
print (x, "alkalommal volt helyes a tipped.")