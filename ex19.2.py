from sys import argv
from os.path import exists

script,from_file,to_file= argv

from1=open(from_file)
read=from1.read()

to=open(to_file,'w')
to.write(read)

from1.close()
to.close()

print("\a")