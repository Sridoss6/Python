sample input="aviation"
sample output=a=2 b=2
**************************************
Program :
***********
mystr="aviation"
vowels="aeiou"
count=""
for vowel in vowels:
	for char in mystr:
		if(vowel==char):
			count=count+char
	len_char=len(count)					
	if(len_char>1):
		print(vowel,"=",len_char)
	count=""
					
		
