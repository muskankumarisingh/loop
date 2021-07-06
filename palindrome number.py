n=int(input("Enter the number:"))
i=n
sum=0
while(n>0):
    digit=n%10
    sum=sum*10+digit
    n=n//10
if(i==sum):
    print("i is a palindrome number")
else:
    print("i is not a palindrome")