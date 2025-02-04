"""
今有物，不知其數。三三數之，賸二；五五數之，賸三；七七數之，賸二。問：物幾何？
術曰：三三數之，賸二，置一百四十；五五數之，賸三，置六十三；七七數之，賸二，置三十。并之，得二百三十三，以二百一十減之，即得。凡三三數之，賸一，則置七十；五五數之，賸一，則置二十一；七七數之，賸一，則置十五。一百六以上，以一百五減之，即得。
答曰： a 。
"""

"""
This problem is a classic example of the Chinese Remainder Theorem. The problem asks for a number \( a \) that satisfies the following congruences:

\[
a \equiv 2 \pmod{3}
\]
\[
a \equiv 3 \pmod{5}
\]
\[
a \equiv 2 \pmod{7}
\]

We will solve this step by step using the method described in the problem.

Here is the Python code to compute \( a \):


"""


from fractions import Fraction

# Step 1: Define the remainders and moduli
remainder_3 = 2
remainder_5 = 3
remainder_7 = 2

mod_3 = 3
mod_5 = 5
mod_7 = 7

# Step 2: Compute the contributions for each modulus
contribution_3 = 140  # 2 * (5 * 7)
contribution_5 = 63   # 3 * (3 * 7)
contribution_7 = 30   # 2 * (3 * 5)

# Step 3: Add the contributions
total = contribution_3 + contribution_5 + contribution_7

# Step 4: Reduce modulo the product of the moduli (3 * 5 * 7 = 105)
a = total % (mod_3 * mod_5 * mod_7)

# The result is stored in the variable `a`


"""


After running this code, the value of \( a \) will be computed. The solution is:

\[
a = 233 \mod 105 = 23
\]

Thus, \( a = 23 \).
"""


"""
"""
