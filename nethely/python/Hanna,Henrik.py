def jon(a):
    if a ==0:
        print("egyikük sem jön kosarazni.")
    elif a==1:
        print("csak az egyikük jön kosarazni.")
    else:
        print("mind a ketten jönnek kosarazni")
y=0
if input ("Jön Henrik ma kosarazni? (igen/nem)\n") == "igen":
    y+=1
if  input ("Jön Hanna ma kosarazni? (igen/nem)\n") == "igen":
    y+=1
jon(y)