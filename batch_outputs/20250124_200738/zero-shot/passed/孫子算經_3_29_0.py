"""
今有雉、兔同籠，上有三十五頭，下有九十四足。問：雉、兔各幾何？
術曰：上置三十五頭，下置九十四足。半其足，得四十七，以少減多，再命之，上三除下三，上五除下五，下有一除上一，下有二除上二，即得。
答曰：雉 a ，兔 b 。
"""

"""
This is a classic Chinese math problem known as the "chicken and rabbit problem." Let's translate it into Python code to compute the values of the unknowns `a` (number of chickens) and `b` (number of rabbits). Chickens have 2 legs, and rabbits have 4 legs. The total number of heads is 35, and the total number of legs is 94.


"""

#----- content starts here -----

from fractions import Fraction

# Total heads
heads = 35

# Total legs
legs = 94

# Solve using the method described in the problem
# Half the total legs
half_legs = Fraction(legs, 2)

# Subtract heads from half the legs to find the number of rabbits
b = half_legs - heads

# Subtract rabbits from total heads to find the number of chickens
a = heads - b

# Results
a, b
#----- content ends here -----


"""


Here, `a` represents the number of chickens, and `b` represents the number of rabbits. The solution will compute their values using the given method.
"""


"""
"""
