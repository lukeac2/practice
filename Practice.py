file = open("new.txt", "w")
listd = ["Zero" ,"Sqeezed " ,"Lemonade ", "Grandma ", " Gameplay ", "Mechanics ", "Walkers ", "Extreme ", "Produced "]
file.writelines(listd)
file.close()
listd.sort()
file=open("new.txt", "w")
file.writelines(listd)
file.close()
file=open("new.txt","r")
print(file.read())


