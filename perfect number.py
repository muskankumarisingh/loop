num=int(input("enter the number"))
i=1
sum=0
while i<num:
	if num%i==0:
		sum=sum+i
	i=i+1
if sum==num:
	print("sum is a perfect number")
else:
	print("sum is not a perfect number")