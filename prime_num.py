def generate_prime(n):
    prime = []
    for num in range(2, n+1):
        is_prime = False
        for i in range(2, num):
            if (num % i == 0):
                break
        else:
            is_prime = True
        if is_prime:
            prime.append(num)
    return prime


print(generate_prime(20))
