# num = str(input("Enter your String:"))
# for i in range(len(num)):
	# for j in range(i+1):
		# print(num[j],end ="")
	# print()
	

	
# num = str(input("Enter the string:"))
# for row in range(len(num)):
	# for col in range(row+1):
		# print(num[col],end="")
	
	# print()
# num=1	
# for row in range(0,4):
	# for col in range(row+1):
		# print(num,end="")
		# num +=1
	# print()
	
	
# num=1
# inp = int(input("Enter the number of rows:"))
# for row in range(0,inp):
	# for col in range(row+1):
		# print(num,end=" ")
		# num +=1
	# print()
	

# *
# * *
# * * *
# * * * *
# * * * * *
# ---------------------------	
# num= int(input("Print the number of rows:"))
# for row in range(1,num+1):
	# for col in range(row):
		# print("*",end=" ")
	# print()
	
# 1 2 3 4 5
# 2 3 4 5
# 3 4 5
# 4 5
# 5
# -------------------
# num= int(input("Print the number of rows:"))	
# for row in range(1, num+1):
	# print(row,end=" ")
	# for col in range(row+1,num+1):
		# print(col,end=" ")

	# print()
	
# for i in range(0):
	# print(i)
	
	
	
	
	
	
	
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# ----------------------
# num = int(input("Enter the no. of rows:"))
# for row in range(1,num+1):
	# for col in range(1,row):                              
		# print(col,end=" ")
	# print()

	
	
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# ----------------------
# num = int(input("Enter the no. of rows:"))	
# for row in range(1,num+1):
	# for col in range(row):
		# print(row, end = " ")
	# print()
	
# num = int(input("Enter the no. of rows:"))	
# for i in range(1,num+1):
	# print("i"*i)
	
# num = int(input("Enter the no. of rows:"))
# n=1	
# for i in range(1,num+1):
	# for j in range(1,i+1):
		# print(n,end=" ")
		# n += 1
	# print()
	
# num = int(input("Enter the no. of rows:"))
# for i in range(1,num+1):
	# for j in range(1,i+1):
		# print(j, end=" ")
	# print()
	

	
# num = int(input("Enter the no. of rows:"))
# for i in range(1,num+1):
	# for j in range(1,i+1):
		# print(i,end= " ")
		
	# print()
	
	
# num = int(input("Enter the no. of rows:"))
# for i in range(1,num+1):
	# for j in range(1,num-i+1):
		# print(" ",end=" ")
	# for j in range(i,0,-1):
		# print(j,end=" ")
	# for j in range(2,i+1):
		# print(j,end=" ")
	
	# print()
# num = int(input("Enter the no. of rows:"))
# for row in range(1,num+1):
	# for col in range(1,num-row+1):
		# print(" ",end=" ")
	# for col in range(row,0,-1):
		# print(col,end=" ")
	# for col in range(2,row+1):
		# print(col,end=" ")
	
	# print()


# for i in range(7):
	# for j in range(5):
		# if ((j==0 or j==4) and i!=0) or ((i==0 or i==3) and(j>0 and j<4)):
			# print("*",end="")
		# else:
			# print(end=" ")
	# print()

# for i in range(7):
	# for j in range(5):
		# if ((j==0 or j==4) and i!=0) or ((i==0 or i==3) and (j>0 and j<4)):
			# print("*",end="")
		# else:
			# print(end=" ")
	# print()

# for i in range(7):
	# for j in range(5):
		# if (j==0 or j==4) or ((i==3) and (j>0 and j<4)):
			# print("*", end="")
			
		# else:
			# print(end=" ")
	# print()


# for i in range(7):
	# for j in range(5):
		# if ((j==0 or j==4) and i!=6) or (i==6 and (j>0 and j<4)):
			# print("*",end="")
		# else:
			# print(end=" ")
		
	# print()

# for i in range(7):
	# for j in range(5):
		# if (j==0) or ((i==0 or i==3 or i==6) and (j>0 and j<4)):
			# print("*",end="")
		# else:
			# print(end=" ")
		
	# print()

# for i in range(7):
	# for j in range(5):
		# if (j==2) or (i==0 or i==6):
			# print("*",end="")
		# else:
			# print(end=" ")
		
	# print()

# for i in range(7):
	# for j in range(5):
		# if ((j==0 or j==4) and i!=0 and i!=6) or (i==0 or i==6) and (j>0 and j<4):
			# print("*",end="")
		# else:
			# print(end=" ")
		
	# print()


# print("\\VOWELS\\")
# for i in range(7):
	# for j in range(5):
		# if ((j==0 or j==4) and i!=0) or (i==0 or i==3) and(j>0 and j<4):
			# print("*",end="")
			
		# else:
			# print(end=" ")
			

	# print()

# print()


# print("-"*10)

# for i in range(7):
	# for j in range(5):
		# if (j==0) or (i==0 or i==3 or i==6):
			# print("*",end="")
			
		# else:
			# print(end=" ")
			

	# print()

# print()


# print("-"*10)			
# for i in range(7):
	# for j in range(5):
		# if (j==2) or (i==0 or i==6):
			# print("*",end="")
			
		# else:
			# print(end=" ")
			

	# print()

# print()


# print("-"*10)

# for i in range(7):
	# for j in range(5):
		# if ((j==0 or j==4) and (i!=0 and i!=6)) or (i==0 or i==6) and (j>0 and j<4):
			# print("*",end="")
			
		# else:
			# print(end=" ")
			

	# print()

# print()


# print("-"*10)			
						
# for i in range(7):
	# for j in range(5):
		# if ((j==0 or j==4) and i!=6) or (i==6) and (j>0 and j<4):
			# print("*",end="")
			
		# else:
			# print(end=" ")
			

	# print()

# print()


# print("-"*10)			
			
			
# for i in range(7):
	# for j in range(5):
		# if ((i==0) and j!=0) or ((i==3) and (j!=0 or j!=4)) or ((i==6) and(j!=4)) or ((i==4 or i==5) and(j==4)) or((i==1 or i==2)and j==0) :
			# print("*",end="")
		# else:
			# print(end=" " )
	# print()
			
			
# for i in range(5):
	# for j in range(5):
		# if ((j==0 or j==4) and (i!=0 and i!=3 and i!=4)) or ((i==0 or i==3) and (j==1 or j==3)) or ((i==1 or i==4) and j==2):
			# print("*",end="")
		# else:
			# print(end=" " )
	# print()
						
			
# for i in range(6):
	# for j in range(7):
		# if (i==0 and (j%3 !=0)) or (i==1 and (j%3 == 0)) or (i-j==2) or (i+j==8):
			# print("*",end="")
		# else:
			# print(end=" " )
	# print()
						
		
			
# for i in range(4):
	# for j in range(7):
		# if (i==j)or(i+j==6):
			# print("*",end="")
		# else:
			# print(end=" " )
	# print()
						
# COMBO=(3,2,6)
# combo_found=False
# for i in range(10):
	# if combo_found:
		# break
	# for j in range(10):
		# if combo_found:
			# break
		# for k in range(10):
			# if (i,j,k)== COMBO:
				# print(f"COMBO Found {COMBO}")
				# combo_found= True
				# break
			# print(i,j,k)
			
			
# import time
# import threading
# def square(num):
	# print("Calculate Square:")
	# for i in num:
		# time.sleep(0.2)
		# print ("Square:",i**2)
	
# def cube(num):
	# print("Calculate Cube:")
	# for i in num:
		# time.sleep(0.2)
		# print ("Cube:",i**3)
# arr=[2,3,4,5,6,7]
# t= time.time()

# t1= threading.Thread (target= square , args=(arr,))
# t2= threading.Thread (target= cube , args=(arr,))

# t1.start()
# t2.start()

# t1.join()
# t2.join()
# print("Execution time is: ",time.time()-t)


# import time
# import threading
# import multiprocessing

# def shown():
	# print("Swaned!")
	
# if __name__=="__main__":
	# for i in range(100):
		# t1= threading.Thread(target=shown , args=())
		# t1.start()
		# t1.join()

	# for i in range(10):
		# p1=multiprocessing.Process(target=shown)
		# p1.start()
		# p1.join()
from multiprocessing import Pool
def square(num):
	return num**2
if __name__=="__main__":
	arr=[2,3,4,5,6]
	p=Pool()
	data = p.map(square,arr)
	# print([square(i) for i in arr if i])
	print(data)















			
			
			
			
			
			
			
			
			
			
			