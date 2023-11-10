import random
def talalat(szam):
    match szam:
        case 0: 
            return"0 helyes számja volt az ötöslottóra."
        case 1: 
            return"1-ese volt az ötöslottón."
        case 2: 
            return"2-ese volt az ötöslottón."
        case 3: 
            return"3-ese volt az ötöslottón."
        case 4: 
            return"4-ese volt az ötöslottón."
        case 5: 
            return "Megnyerte az főnyereményt!"
#főprogram
#lista feltöltése
lotto=[]
napi=[]
for x in range (52):
    rando= []
    rando = random.sample(range(1,91),5)
    '''
    for y in range (5):
        rando = random.randint(1,90)
        Has = False
        for z in range(len(napi)):
            if rando==napi[z-1]:
                Has = True
        if Has == True:
            y-=1
        else:
        napi.append(rando)
    print(napi)
    '''
    lotto.append(rando)
#2. feladat:
rando = random.randint(1,52)
keres=[]
while len(keres)!=5:
    Has = False
    y =(int(input("Kérek egy számot az ötöslottóra. ")))
    for z in range(len(keres)):
        if y==keres[z-1]:
            Has = True
    if Has == True:
        print("Két megadott szám ne legyen ugyan az!")
    else:
        if y > 0 and y < 91:
            keres.append(y)
        else:
            print("A szám legyen 1 és 90 között.")
    
#3. feladat:
print("Eheti nyerő számok:",sorted(lotto[rando]))
#4. feladat:
maxim = []
count = 0
ind = 0
for x in range (91):
    maxim.append(0)
    for y in range (52):
        for z in range(5):
            if x == lotto[y-1][z-1]:
                maxim[x-1] +=1
for x in range (1,90):
    if maxim[x-1]> count:
        count = maxim[x]
        ind = x
print(ind, "a leggyakoribb szám.")
for x in range (1,90):
    if maxim[x-1]< count:
        count = maxim[x]
        ind = x
print(ind, "a legritkább szám.")
#5. feladat:
count = 0
for x in range (0,4):
    if lotto[rando][x]==keres[x]:
        count+=1
print(talalat(count))
#6. feladat:
for x in range(0,51):
    count = 0
    for y in range (0,4):
        
        for z in range (0,4):
            if lotto[x][y]==keres[z]:
                count+=1
    print(talalat(count))