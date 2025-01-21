"""
今有物，不知其數。三三數之，賸二；五五數之，賸三；七七數之，賸二。問：物幾何？
答曰： a 。
"""

"""
Suppose there is an unknown number of objects. When counted in groups of 3, there is a remainder of 2. When counted in groups of 5, there is a remainder of 3. When counted in groups of 7, there is a remainder of 2.
Question: how many objects are there?

Answer: *a*.
"""

# Using the Chinese Remainder Theorem to solve:
# Let the unknown number be x.
# x ≡ 2 (mod 3)
# x ≡ 3 (mod 5)
# x ≡ 2 (mod 7)

# Step 1: Find the least common multiple of the moduli (3, 5, 7)
moduli = [3, 5, 7]
lcm = 3 * 5 * 7  # Since 3, 5, and 7 are coprime, their LCM is their product.

# Step 2: Solve the system of congruences
# Start with x ≡ 2 (mod 3)
x = 2
while True:
    # Check if x satisfies the other two congruences
    if x % 5 == 3 and x % 7 == 2:
        break
    x += 3  # Increment by the modulus of the first congruence

# The answer is:
a = x  # The smallest positive solution
"""
"""
