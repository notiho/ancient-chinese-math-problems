"""
今有物，不知其數。三三數之，賸二；五五數之，賸三；七七數之，賸二。問：物幾何？
術曰：三三數之，賸二，置一百四十；五五數之，賸三，置六十三；七七數之，賸二，置三十。并之，得二百三十三，以二百一十減之，即得。凡三三數之，賸一，則置七十；五五數之，賸一，則置二十一；七七數之，賸一，則置十五。一百六以上，以一百五減之，即得。
答曰： a 。
"""

"""
This is a classic Chinese Remainder Theorem problem. Let's translate the problem into Python code to compute the value of the unknown `a`.


"""


from fractions import Fraction

# Given conditions:
# x ≡ 2 (mod 3)
# x ≡ 3 (mod 5)
# x ≡ 2 (mod 7)

# Using the method described in the problem:
# Coefficients for each modulus:
mod_3 = 140  # 2 * (5 * 7)
mod_5 = 63   # 3 * (3 * 7)
mod_7 = 30   # 2 * (3 * 5)

# Combine the results:
result = mod_3 + mod_5 + mod_7  # 140 + 63 + 30 = 233

# Reduce the result modulo the product of the moduli (3 * 5 * 7 = 105):
a = result % 105  # 233 % 105 = 23

# The answer:
a  # a = 23


"""


The value of `a` is `23`.
"""


"""
"""
