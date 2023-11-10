#31. 3 számból a legkisebb kiírása
szam = int(input("Kérek egy számot!"))
x= int(input("Kérek még egy számot!"))
x=min (szam,x)
szam= int(input("Kérek egy harmadik számot!"))
x=min (szam,x)
print(x)

#32. Megadjuk egy háromszög 3 oldalát és megmonja hogy egy valós három szög e
szam = int(input("Kérek egy háromszög oldalt!"))
x= int(input("Kérek még egy oldalt!"))
y = int(input("Kérek egy harmadik oldalt!"))

if (max(szam, x, y)< (szam+x+y)-max(szam,x,y)):
    print("Szerkeszthető a háromszög!")
else:
    print("Ez a háromszög nem szerkeszthető!")

#33. beadunk három számot, másodfokú egyenletbe beírja
import math
szam = int(input("Kérek egy számot!"))
x= int(input("Kérek még egy számot!"))
y = int(input("Kérek egy harmadik számot!"))
y=(x*x)-(4*szam*y)
szam*=2
if(y>0):
    print((math.sqrt(y)+(-x))/szam)
    print((math.sqrt(y)-(-x))/szam)
else: 
    if(y==0):
        print((math.sqrt(y)+(-x))/szam)
    else:
        print("Nincs megoldás a valós számok között!")
    
#34. beadunk két számot, kiad egy derékszögű háromszög harmadik oldalát

szam = int(input("Kérek egy számot!"))
x= int(input("Kérek még egy számot!"))

print(round(math.sqrt((szam*szam)+(x*x)),2))

#35. 1-től 10-ig a számok reciprokja
for x in range(1,11):
    print(1/x)

#36. beadott adatok hatványozása
szam = int(input("Kérek egy számot!"))
x= int(input("Kérek még egy számot!"))

print(pow(szam,x))

#37. csak pozitív számot ír ki
szam = int(input("Kérek egy számot!"))

if(szam/1 == abs(szam)):
    print(szam)
else:
    print("nem pozitív szám")

#38. két beadott számnak kiírja a számegyenesen belüli távolságukat
szam = int(input("Kérek egy számot!"))
x= int(input("Kérek még egy számot!"))

print(abs(szam-x) , "egységre állnak a számok egymástól")

#39. két beadott számnak kiírja az átlagát
szam = int(input("Kérek egy számot!"))
x= int(input("Kérek még egy számot!"))

print((szam+x)/2)

#40. beolvas két számot ameddig nem több az összegük 100-nál
szam = int(input("Kérek egy számot!"))
x= int(input("Kérek még egy számot!"))

while szam+x <100:
    szam = int(input("Kérek két új számot!"))
    x= int(input())  
print("A két szám összege több mint 100!")

#41. beolvas számot ameddig nem több tíznél, aztán kiírja a beadott számok összegét
szam = int(input("Kérek egy számot!"))
x= 0

while szam+x <10:
    x+=szam
    szam = int(input("Kérek egy új számot!"))
    
print(x+szam)

#42. kiír egy számot 1-től 100-ig
import random
szam = random.randint(1,100)
print(szam)

#43. kiír egy számot 10-től 50-ig
szam = random.randint(10,50)
print(szam)

#44. kiír egy számot 132-től 147-ig
szam = random.randint(132,147)
print(szam)

#45. kiír egy számot 132-től 148-ig ha páros
szam = random.randint(132,147)
if(szam%2==0):
    print(szam)
