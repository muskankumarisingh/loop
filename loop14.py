n=int(input("enter number"))
a=2
c=1
while a>0:
	i=2
	while i<a:
		if a%i==0:
			break
		i+=1
	else:
		print(a)
		if c==n:
			break
		c+=1
	a+=1

Loop prime number user jitna  dale utna woo first se print kare Jaise 5 daale to first five prime number de