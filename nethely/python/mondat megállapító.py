def szo(szo):
    match szo[len(szo)-1]:
        case ".":
            return "Ez egy kijelentő mondat."
        case "?":
            return "Ez egy kérdő mondat."
        case "!":
            return "Ez egy felkiáltó mondat."
        case default:
            return "Ennek a mondatnak nincs mondatvégi jele."
#főprogram
x=input("Kérek egy mondatot! ")
print(szo(x))