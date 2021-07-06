num=int(input("enter the number"))
sum=0
i=num
while i>0:
	digit=i%10
	sum=sum+digit**3
	i//=10
if num==sum:
	print("num is an armstrong number")
else:
	print("num is not an armstrong number")