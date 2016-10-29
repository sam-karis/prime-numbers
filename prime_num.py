def generate_prime(n):
	prime = []
	for num in range(2, n+1):
		for i in range(2, num):
			if (num % i ==0):
				break
	        else:
	         	prime.append(num)
	return prime

print (generate_prime(20))