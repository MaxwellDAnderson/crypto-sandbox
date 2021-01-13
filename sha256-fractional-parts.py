# Formula for finding the first 32 bits of the fractional parts of the square roots of the first 8 primes
# First eight prime numbers = 2, 3, 5, 7, 11, 13, 17, 19
# Good references:
# https://stackoverflow.com/questions/4674956/what-are-the-first-32-bits-of-the-fractional-part-of-this-float/4675080
# http://gauss.ececs.uc.edu/Courses/c6055/lectures/Hashing/mdalgs.pdf
# https://qvault.io/2020/07/08/how-sha-2-works-step-by-step-sha-256/

import math

h0 = hex(int(math.modf(math.sqrt(2))[0] * (1 << 32)))

h1 = hex(int(math.modf(math.sqrt(3))[0] * (1 << 32)))

h2 = hex(int(math.modf(math.sqrt(5))[0] * (1 << 32)))

h3 = hex(int(math.modf(math.sqrt(7))[0] * (1 << 32)))

h4 = hex(int(math.modf(math.sqrt(11))[0] * (1 << 32)))

h5 = hex(int(math.modf(math.sqrt(13))[0] * (1 << 32)))

h6 = hex(int(math.modf(math.sqrt(17))[0] * (1 << 32)))

h7 = hex(int(math.modf(math.sqrt(19))[0] * (1 << 32)))

print(h0)
print(h1)
print(h2)
print(h3)
print(h4)
print(h5)
print(h6)
print(h7)
