def szo(szo):
    if (szo[0]=="a" or szo[0]=="A"):
      return True
    else:
        return False
#főprogram
x=input("Kérek egy szót! ")
while x !="":
    if szo(x):
        print("Ez a szó a betűvel kezdődik.")
    else:
        print("Ez a szó nem a betűvel kezdődik.")
    x=input("Kérek egy szót! ")