from sys import argv
script,input_file=argv

def file(f):
	print(f.read())

new= open(input_file)
file(new)

def rewind(f):
	f.seek(0)

print("try to know what .seek does?")

rewind(new)
current_file=1
def file_(current_file,f):
	print(current_file,f.readline())
file_(current_file,new)

print("*"*20)

current_file=current_file+1
file_(current_file,new)


current_file=current_file+1
file_(current_file,new)


new.close()