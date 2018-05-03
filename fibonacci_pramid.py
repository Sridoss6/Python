Write a program to below format 
sample output:
****************************

0 
0 1 
0 1 1 
0 1 1 2 
0 1 1 2 3 
0 1 1 2 3 5 
5 3 2 1 1 0 
3 2 1 1 0 
2 1 1 0 
1 1 0 
1 0 
0 

******************************
Program:
*************
for i in range(1,7):
	a=0
	b=1
	for j in range(i):
		x=a
		y=b
		a=y
		b=x+y
		print(x,end=" ")	
	print()

for i in range(6,0,-1):
	lis=[]
	a=0
	b=1
	for j in range(i):
		x=a
		y=b
		a=y
		b=x+y
		lis.append(x)
	my_len=len(lis)
	k=1
	for s in range(my_len,0,-1):
		val=s-k
		print(lis[val],end=" ")
	print()
		
