num=int(input("enter the number"))
sum=0
i=num
while num>0:
	rem=num%10
	sum=sum+rem
	num=num//10
if i%sum==0:
	print("i is a harshad number")
else:
	print("i is not a harshad number")