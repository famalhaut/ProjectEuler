"""
Prime permutations
Problem 49 
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual 
in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are 
permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this 
property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
"""
from common.primes import primes_gen


def problem():
    digits = {}
    result = ''
    for prime in primes_gen():
        if 10 ** 3 < prime:
            key = tuple(sorted(str(prime)))
            if key in digits:
                digits[key].add(prime)
            else:
                digits[key] = {prime, }
        if 10 ** 4 < prime:
            break

    for nums in digits.values():
        permuts = sorted(nums)
        for i, fst in enumerate(permuts[0:-2]):
            for snd in permuts[i + 1:-1]:
                if (2 * snd - fst) in nums:
                    print(fst, snd, 2 * snd - fst)
                    if fst != 1487:
                        result = ''.join(map(str, [fst, snd, 2 * snd - fst]))
    return result


if __name__ == '__main__':
    print('Answer:', problem())
