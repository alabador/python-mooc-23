# Write your solution here
def prime_numbers():
    current_prime = 2
    while True:
        # print("huh", current_prime)
        if check_prime(current_prime) == False:
            current_prime += 1
        else:
            yield current_prime
            current_prime += 1
    
def check_prime(number: int):
    quotients = []
    for x in range(2, number - 1):
        quotients.append(number % x)
    return 0 not in quotients

if __name__ == "__main__":
    numbers = prime_numbers()
    for i in range(8):
        print(next(numbers))
