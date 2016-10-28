def generate_prime_numbers(n):
	prime_list = []
	for num in range(2,n+1):
		if test_prime(num):
			prime_list.append(num)
	return prime_list
		
def test_prime(number):
	if number > 1:
		for j in range(2, number):
			if not number % j:
				return False
		else:
			return True
	else:
		return False
		
print (generate_prime_numbers(10))