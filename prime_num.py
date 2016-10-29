def generate_prime(n):
	for num in range(2, n+1):
		for i in range(2, num):
			if (num % i ==0):
				break
	        else:
	         	print (num)

print (generate_prime(20))