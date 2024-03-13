import math
import random


# Functions declaration -----------------------------------------
def get_prime_factors(n):
    factors = dict()
    
    # Remove all the factors of 2
    while n % 2 == 0:
        factors[2] = (factors[2] + 1) if 2 in factors else 1
        n = n // 2
    
    # Check for odd prime factors starting from 3
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors[i] = (factors[i] + 1) if i in factors else 1
            n = n // i
    
    # If the remaining number is greater than 2, it's a prime factor
    if n > 2:
        factors[n] = 1
    
    return factors


def get_random_number(n_digits):
    n = ''
    for i in range(n_digits):
        if i == 0:
            n = n + str(random.randint(1,9))
        else:
            n = n + str(random.randint(0,9))
    return int(n)


def get_next_prime_number(base_number):
    counter = 0
    for i in range(0, 400):
        number = base_number + i
        prime_factors = get_prime_factors(number)
        if len(prime_factors) == 1:
            return (number, counter)
        counter += 1


def get_previous_prime_number(base_number):
    counter = 0
    for i in range(0, 400):
        number = base_number - i
        prime_factors = get_prime_factors(number)
        if len(prime_factors) == 1:
            return (number, counter)
        counter += 1


# Run main module -------------------------------------

n_digits = 7
n_iteration = 1000

furthest_number = None
max_steps_required = 0

required_steps_list = []
for idx in range(n_iteration):
    number = get_random_number(n_digits)
    # print(number)
    steps_required = get_next_prime_number(number)[1]
    if steps_required > max_steps_required:
        furthest_number = number
        max_steps_required = steps_required
    required_steps_list.append(steps_required)

furthest_number = get_previous_prime_number(furthest_number)[0] + 1
max_steps_required = get_next_prime_number(furthest_number)[1]


average_steps_required = int(sum(required_steps_list) / len(required_steps_list))

print(f"In average, for numbers with {n_digits} digits, {average_steps_required} steps needed to find next prime number.") 
print(f"furthest number from a prime number with {n_digits} digits is {furthest_number} which requires {max_steps_required} steps to find next prime number.")



# ------------------------------------------------------
n_digits = 7
interval = 170

required_steps_list = []
for number in range(10**(n_digits-1), 10**(n_digits)-1, interval):
    steps_needed = get_next_prime_number(number)[1]
    required_steps_list.append(steps_needed)

average_steps_required = int(sum(required_steps_list) / len(required_steps_list))

print(f"In average, for numbers with {n_digits} digits, {average_steps_required} steps needed to find next prime number.")


# Next task: find a number with 12 digits that has no prime number in its next 180 numbers.(187)
# top record: 817582555950 , 187

get_next_prime_number(817582555950)
# get_previous_prime_number(817582555950)




# Calculate ratio of numbers with n digits which are smaller than greatest n digits number:
# ---------------------------------------------------------------------------------------------

# we have a 2 digits number of numbers with 2 digits -> we have a n digits number of numbers with n digits
# how many percentage of numbers smaller than the greatest n digits number have n digits?
# n = 1  ->  100%
# n = 2  ->  90.90%
# n = 3  ->  90.09%
# n = 4  ->  90.01%



def get_percentage_of_numbers_with_n_digits_smaller_than_greatest_n_digits_number(n):
    p = (((10**n) - 1) - (10**(n-1)) + 1)/ ((10**n) - 1)
    return p



d = dict()

for n in range(1,15):
    p = get_percentage_of_numbers_with_n_digits_smaller_than_greatest_n_digits_number(n)
    d[n] = p

d