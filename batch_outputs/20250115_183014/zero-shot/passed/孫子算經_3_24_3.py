"""
今有物，不知其數。三三數之，賸二；五五數之，賸三；七七數之，賸二。問：物幾何？
術曰：三三數之，賸二，置一百四十；五五數之，賸三，置六十三；七七數之，賸二，置三十。并之，得二百三十三，以二百一十減之，即得。凡三三數之，賸一，則置七十；五五數之，賸一，則置二十一；七七數之，賸一，則置十五。一百六以上，以一百五減之，即得。
答曰： a 。
"""

"""
This is a classic Chinese remainder theorem problem. The problem is asking for a number \( a \) that satisfies the following congruences:

1. \( a \equiv 2 \pmod{3} \)
2. \( a \equiv 3 \pmod{5} \)
3. \( a \equiv 2 \pmod{7} \)

We will solve this step by step in Python using the method described in the problem.


"""


from fractions import Fraction

# Given congruences:
# a ≡ 2 (mod 3)
# a ≡ 3 (mod 5)
# a ≡ 2 (mod 7)

# Step 1: Compute the remainders for each modulus
mod_3 = 140  # 2 * (70 from the method described)
mod_5 = 63   # 3 * (21 from the method described)
mod_7 = 30   # 2 * (15 from the method described)

# Step 2: Add these together
a = mod_3 + mod_5 + mod_7  # This gives 233

# Step 3: Reduce modulo 105 (the least common multiple of 3, 5, and 7)
a = a % 105  # Subtract 210 if necessary

# Final result
print(a)  # a = 23


"""


The solution is \( a = 23 \).
"""


"""
"""
