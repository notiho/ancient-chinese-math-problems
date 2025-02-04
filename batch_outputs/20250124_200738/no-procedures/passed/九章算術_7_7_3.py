"""
今有共買犬，人出五，不足九十；人出五十，適足。問︰人數、犬價各幾何？
荅曰： a人 ，犬價 b 。
"""

#----- content starts here -----
"""
Suppose a group of people collectively buys a dog. If each person contributes 5, the total is 90 less than the required amount. If each person contributes 50, the total is exactly enough.
Question: how many people are there, and what is the price of the dog?

Answer: there are *a* people, and the price of the dog is *b*.
"""

# Let the number of people be x and the price of the dog be y
# Equation 1: 5x + 90 = y
# Equation 2: 50x = y

# Solve for x and y
from fractions import Fraction

# From Equation 2: y = 50x
# Substitute into Equation 1: 5x + 90 = 50x
# Simplify: 45x = 90
a = Fraction(90, 45)  # Number of people

# Substitute x into Equation 2 to find y
b = 50 * a  # Price of the dog

a, b  # Return the results#----- content ends here -----

"""
"""
