def atment(b):
    if b>=48:
        return True
    else:
        return False
#főprogram
x = input("Adja meg a vizsgázó nevét!")
while x != "":
    y = int(input("Adja meg a vizsgázó pontszámát!"))
    if atment(y):
        print(x, "vizsája sikeres.")
    else:
        print(x, "vizsája sikertelen.")
    x = input("Adja meg a vizsgázó nevét!")