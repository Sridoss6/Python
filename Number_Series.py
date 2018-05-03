Write the Program that gets n and print the below series until n.
*****************************************************************
Sample Output:0 1 3 6 11 19

n=int(input("Enter the range:"))
a=0
b=1
for i in range(n):
	x=a
	y=b
	a=y
	b=x+y+2
	if(x<n):
		print(x,end=" ")
	else:
		break
print()	
