line1= input("Enter the First line") #input the lines
line2= input("Enter the Second line")
line3= input("Enter the Third line")
line4= input("Enter the Fourth line")

text= input("Enter the filename: ") 
open = open(text,'w') #use 'w' for write in a file
open.write(line1) #write 
open.write("\n")
open.write(line2)
open.write("\n")
open.write(line3)
open.write("\n")
open.write(line4)


#open.truncate()
open.close()
