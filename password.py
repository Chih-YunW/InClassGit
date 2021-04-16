import random

def password (n):
	i = 1
	while i <= n:
		a = random.randint(32,126)
		print(chr(a), end = "")

length = input("Please enter a length for the password: ")
length = int(length)
password(length)
print("\n")
