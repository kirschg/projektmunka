import random
#46. kiír egy számot 1-től 6-ig ameddig nem kap 6-ot
szam = random.randint(1,6)
while szam!= 6:
    print(szam)
    szam = random.randint(1,6)
print(szam)

#47. beadott számról eldönti hogy prím szám e
y=0
szam= int(input("Kérek egy számot!"))
for x in range(1, szam):
    if(szam%x==0):
        y+=1
if(y<=2):
    print("Ez egy prím szám!")
else:
    print("Ez nem egy prím szám!")

#48. két beadott szövegből eldönti a rövidebbet

x= input("Kérek egy szót!")
y= input("Kérek egy másik szót!")

if(len(x)<len(y)):
    print(x,"A rövidebb szó!")
else:
    print(y,"A rövidebb szó!")

#49. két beadott szöveget eldönti hogy azonosak e

x= input("Kérek egy szót!")
y= input("Kérek egy másik szót!")

if(x==y):
    print("A két beadott szó azonos!")
else:
    print("A két beadott szó nem azonos!")

#50. két beadott szövegből eldönti a hosszabb
x= input("Kérek egy szót!")
y= input("Kérek egy másik szót!")

if(len(x)>len(y)):
    print(x,"A hosszabb szó!")
else:
    print(y,"A hosszabb szó!")


