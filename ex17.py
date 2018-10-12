from sys import argv     #for argv
from os.path import exists  #to define if its exists or not 
script,from_f,to_f=argv  #define with var argv

print(f"Does the file exist{exists(from_f)}")   #used exists for the conformation of the file

new=open(from_f)  #open the exist file
read=new.read()  #read it and store it in a variable

tofile=open(to_f,'w')  #open a new file with write 'w' mode
tofile.write(read)  #write what ever you rad 

new.close() #close both
tofile.close()

print("\a")



















from sys import argv
from os.path import exists
script,filename,newfile = argv
openf = open(filename)
read = openf.read()                      # don't use keyword as Variable
print(f"Yes Filename exist {exists(filename)}")
print(f"Yes newfile exist {exists(newfile)}")
print(f"Hi {script} ,{filename} ,{newfile}")

opennew = open(newfile,'w')
print(f"Yes newfile exist {exists(newfile)}")
opennew.write(read)