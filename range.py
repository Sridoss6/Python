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
