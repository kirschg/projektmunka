def hat(szam):
    if szam<=5 and szam>=-5:
        return True
    else:
        return False
#főprogram
x = int(input("Kérek egy számot! "))
y = 0
while hat(x):
    y += x
    print(x , "\n" , y)
    x = int(input("Kérek egy számot!"))