import random
def gon(szam, ker):
    if szam > ker:
        return "Kisebbre gondoltam!"
    elif szam== ker:
        return "ELTALÁLTA!"
    else:
        return "Nagyobbra gondoltam!"
#főprogram
rando = random.randint(1,5)
beker = int(input("Gondoltam egy számra 1 és 5 között\nKérem, adjon meg egy egész számot: "))  
print(gon(beker,rando))