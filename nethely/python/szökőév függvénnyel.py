def szokoev(szam):
    if (szam % 400==0):
      return True
    elif (szam % 4 ==0 and szam % 100 !=0):
        return True
    else:
        return False
#főprogram
for x in range (1,4):
    y = int (input("Kérek egy évszámot! "))
    if szokoev(y):
        print("Az év szökőév volt!")
    else:
        print("Az év nem szökőév volt!")