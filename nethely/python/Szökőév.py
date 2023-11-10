szam = int(input("Kérek egy évszámot!"))

if szam%4==0 and szam%100!=0:
    print("Ez az év egy szökőév")
elif szam%400==0:
    print("Ez az év egy szökőév")
else:
    print("Ez az év nem egy szökőév")