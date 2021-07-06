n=int(input('enter any number'))
i=1 
c=0
while True:
	if i%2==0:
		print(i)
		c+=1
	i+=1
	if c==n:
		break