Sample Output:

192.168.0.0

192.168.0.1

192.168.0.255
..........
..........
192.168.1.0

192.168.1.1

192.168.1.255
************************************
Program:
*********
i=0
n=255
s=2
ip="192.168."

while(i < s):
	j=0
	while(j <= n):
		print(ip,end="")
		print(i,end="")
		
		if(j<=n):
			print(".",end="")
			print(j)
			j=j+1
		print()
	i=i+1	
			
	
	


	


