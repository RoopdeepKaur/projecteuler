from math import sqrt, floor


def num_prime(n):
    max_possible_factor = int( floor( sqrt(n) ) )
    possible_factors = range( 2, max_possible_factor+1 )
    divisible_factors = [ n % i == 0 for i in possible_factors ]
    return not any( divisible_factors )


def nth_prime(n):
    number = 1
    new = 2

    while number < n:
        new += 1
        if num_prime(new):
            number += 1
    return new


if __name__ == "__main__":
    print(nth_prime(10001))
