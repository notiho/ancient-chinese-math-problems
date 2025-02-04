"""
今有物，不知其數。三三數之，賸二；五五數之，賸三；七七數之，賸二。問：物幾何？
術曰：三三數之，賸二，置一百四十；五五數之，賸三，置六十三；七七數之，賸二，置三十。并之，得二百三十三，以二百一十減之，即得。凡三三數之，賸一，則置七十；五五數之，賸一，則置二十一；七七數之，賸一，則置十五。一百六以上，以一百五減之，即得。
答曰： a 。
"""

"""
This problem is a classic example of the Chinese Remainder Theorem. The problem states that there is a number that satisfies the following conditions:

1. When divided by 3, the remainder is 2.
2. When divided by 5, the remainder is 3.
3. When divided by 7, the remainder is 2.

We will solve this step by step using the method described in the problem and compute the value of `a`.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Step 1: Define the remainders and moduli
remainder_3 = 2
remainder_5 = 3
remainder_7 = 2

mod_3 = 3
mod_5 = 5
mod_7 = 7

# Step 2: Compute the contributions
contribution_3 = 140  # 3 * 5 * 7 / 3
contribution_5 = 63   # 3 * 5 * 7 / 5
contribution_7 = 30   # 3 * 5 * 7 / 7

# Step 3: Compute the weighted sum
weighted_sum = (remainder_3 * contribution_3 +
                remainder_5 * contribution_5 +
                remainder_7 * contribution_7)

# Step 4: Compute the result modulo 105 (3 * 5 * 7)
a = weighted_sum % (mod_3 * mod_5 * mod_7)

# The result is stored in variable `a`
#----- content ends here -----


"""


After running this code, the variable `a` will contain the solution to the problem.
"""


"""
Variable 'a' has wrong value. Expected: 23, Actual: 4"""
