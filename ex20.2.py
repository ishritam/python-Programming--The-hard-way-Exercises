from sys import argv
script,input_file=argv

def fun(f):
	print(f.readline())

def seek(f):
	f.seek(0)
new= open(input_file)
seek(new)
fun(new)

fun(new)

fun(new)

new.close()
