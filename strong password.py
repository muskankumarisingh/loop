password=input("Enter your password: ")
if len(password)<=8 and len(password)>=1:
	if ('@' or '$' or '#' in password):
		if(password>='0' or password<='9'):
			if(password>='a' or password<='z' and password>='A' or password<='Z'):
				print("correct password")
			else:
					print("correct password")
		else:
				print("correct password")
	else:
			print("correct password")
else:
		print("incorrect password")
 
#Strong password