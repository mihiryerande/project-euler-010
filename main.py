# Problem 10:
#     Summation of Primes
#
# Description:
#     The sum of the primes below 10 is
#         2 + 3 + 5 + 7 = 17
#
#     Find the sum of all the primes below two million.

def main(n: int) -> int:
    """
    Returns the sum of all primes less than `n`.

    Args:
        n (int): Natural number

    Returns:
        (int): Sum of all primes less than `n`

    Raises:
        AssertError: if incorrect params are given
    """
    assert type(n) == int and n > 0

    # Maintain a sieve 'mask' indicating which numbers are prime,
    #   where index `i` represents number i+1
    # Faster to step through mask and overwrite,
    #   rather than checking for divisibility of elements
    sieve = [True for _ in range(n)]
    sieve[0] = False  # 1 is not prime

    i = 1  # Start iterating from number 2
    while i < len(sieve):
        p = i+1  # Next largest prime
        for j in range(i+p, len(sieve), p):
            sieve[j] = False
        i += 1

    ps = list(map(lambda yi: yi[0]+1, filter(lambda xi: xi[1], enumerate(sieve))))
    return sum(ps)


if __name__ == '__main__':
    num = int(input('Enter a natural number: '))
    total = main(num)
    print('Sum of primes below {}:'.format(num))
    print('  {}'.format(total))
