
save = open("D:/YesNo.txt").read()
print(save)
saveFile = open("D:/YesNo.txt","w")
saveFile.write("Hi I am Shritam")
print("*"*10)
saveFile.close()
save1 = open("D:/YesNo.txt","a")
save1.write("\n Hi I am Second Line")
saveFile.close()

open("D:/YesNo.txt").read()
# close()