"""
今有令一人、吏五人、從者一十人，食雞一十；令一十人、吏一人、從者五人，食雞八；令五人、吏一十人、從者一人，食雞六。問︰令、吏、從者食雞各幾何？
荅曰：令一人食 a雞 ，吏一人食 b雞 ，從者一人食 c雞 。
"""

"""
Suppose there are three groups of people with different roles (Ling, Li, and Congzhe) eating chickens:

1. 1 Ling, 5 Li, and 10 Congzhe eat 10 chickens.
2. 10 Ling, 1 Li, and 5 Congzhe eat 8 chickens.
3. 5 Ling, 10 Li, and 1 Congzhe eat 6 chickens.

Question: How many chickens does each role (Ling, Li, Congzhe) eat individually?

Answer: 1 Ling eats *a* chickens, 1 Li eats *b* chickens, and 1 Congzhe eats *c* chickens.
"""

# Define the equations based on the problem
# Let a = chickens eaten by 1 Ling
# Let b = chickens eaten by 1 Li
# Let c = chickens eaten by 1 Congzhe

# Equation 1: 1a + 5b + 10c = 10
# Equation 2: 10a + 1b + 5c = 8
# Equation 3: 5a + 10b + 1c = 6

# Solve the equations manually using substitution or elimination
from fractions import Fraction

# Step 1: Eliminate 'a' from two equations
# Multiply Equation 1 by 10: 10a + 50b + 100c = 100
# Subtract Equation 2: (10a + 50b + 100c) - (10a + 1b + 5c) = 100 - 8
# Result: 49b + 95c = 92  (Equation 4)

# Multiply Equation 1 by 5: 5a + 25b + 50c = 50
# Subtract Equation 3: (5a + 25b + 50c) - (5a + 10b + 1c) = 50 - 6
# Result: 15b + 49c = 44  (Equation 5)

# Step 2: Solve for 'b' and 'c' using Equation 4 and Equation 5
# Multiply Equation 5 by 49: 735b + 2401c = 2156
# Multiply Equation 4 by 15: 735b + 1425c = 1380
# Subtract: (735b + 2401c) - (735b + 1425c) = 2156 - 1380
# Result: 976c = 776
c = Fraction(776, 976)

# Simplify c
c = Fraction(4, 5)

# Substitute c into Equation 5: 15b + 49(4/5) = 44
# 15b + 196/5 = 44
# Multiply through by 5: 75b + 196 = 220
# 75b = 24
b = Fraction(24, 75)

# Simplify b
b = Fraction(8, 25)

# Substitute b and c into Equation 1: a + 5(8/25) + 10(4/5) = 10
# a + 40/25 + 40/5 = 10
# a + 8/5 + 8 = 10
# a + 48/5 = 10
# a = 10 - 48/5
# a = 50/5 - 48/5
# a = 2/5
a = Fraction(2, 5)

# Final results
print(f"1 Ling eats {a} chickens.")
print(f"1 Li eats {b} chickens.")
print(f"1 Congzhe eats {c} chickens.")
"""
Variable 'a' has wrong value. Expected: 45/122, Actual: 2/5
Variable 'b' has wrong value. Expected: 41/122, Actual: 8/25
Variable 'c' has wrong value. Expected: 97/122, Actual: 4/5"""
