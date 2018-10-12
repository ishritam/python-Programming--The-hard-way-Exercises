from sys import argv  #import unpacks from the library
script,Filename=argv
txt=open(Filename) #open the file you typed, and store it in "txt" variable

print(txt.read())  #it will read the tex variable and print it
txt.close()
print("*"*30,"_"*10,"*"*30)

print(script)   # name of the script
Filename = input("Give me the file name >>")   #ask you for the filename and save it in a variable name called "Filename"
txt1=open(Filename)  #it will open the input file name
print(txt1.read())    #read the text1 value i.e your filename and print what is in that file
txt1.close()

