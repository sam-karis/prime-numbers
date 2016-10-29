"""
this is my first function for boot camp 11
that generate prime generate prime numbers
"""
def generate_prime_numbers(n):
	prime_list = []
	for num in range(2,n+1):
		if test_if_is_a_prime(num):
			prime_list.append(num)
	return prime_list
"""check whether a number is a prime or not
to return true or False
"""
def test_if_is_a_prime(number):
	if number > 1:
		for j in range(2, number):
			if not number % j:
				return False
		else:
			return True
	else:
		return False
		
print (generate_prime_numbers(20))