def osszead(a,b):
    ossz=a+b
    return ossz
def kivon(a,b):
    ossz=a-b
    return ossz
def szorzas(a,b):
    ossz=a*b
    return ossz
def osztas(a,b):
    ossz=a/b
    return ossz
#főprogram
x = int(input("Kérek egy számot"))
y = int(input("Kérek egy második számot"))
print(osszead(x,y))
x = int(input("Kérek egy számot"))
y = int(input("Kérek egy második számot"))
print(kivon(x,y))
x = int(input("Kérek egy számot"))
y = int(input("Kérek egy második számot"))
print(szorzas(x,y))
x = int(input("Kérek egy számot"))
y = int(input("Kérek egy második számot"))
print(osztas(x,y))