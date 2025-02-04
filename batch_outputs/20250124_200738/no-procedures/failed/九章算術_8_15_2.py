"""
今有令一人、吏五人、從者一十人，食雞一十；令一十人、吏一人、從者五人，食雞八；令五人、吏一十人、從者一人，食雞六。問︰令、吏、從者食雞各幾何？
荅曰：令一人食 a雞 ，吏一人食 b雞 ，從者一人食 c雞 。
"""

#----- content starts here -----
"""
Suppose there are three groups of people with different roles (Ling, Li, and Congzhe) eating chickens:

1. 1 Ling, 5 Li, and 10 Congzhe eat 10 chickens.
2. 10 Ling, 1 Li, and 5 Congzhe eat 8 chickens.
3. 5 Ling, 10 Li, and 1 Congzhe eat 6 chickens.

Question: How many chickens does each role (Ling, Li, Congzhe) eat individually?

Answer: 1 Ling eats *a* chickens, 1 Li eats *b* chickens, and 1 Congzhe eats *c* chickens.
"""

from fractions import Fraction

# Let:
# a = chickens eaten by 1 Ling
# b = chickens eaten by 1 Li
# c = chickens eaten by 1 Congzhe

# Equations based on the problem:
# 1a + 5b + 10c = 10
# 10a + 1b + 5c = 8
# 5a + 10b + 1c = 6

# Solve the system of equations step by step:

# Step 1: Eliminate one variable (e.g., `a`) using the first two equations.
# Multiply the first equation by 10 and the second equation by 1 to align the coefficients of `a`:
# 10(1a + 5b + 10c = 10) -> 10a + 50b + 100c = 100
# 1(10a + 1b + 5c = 8) -> 10a + 1b + 5c = 8

# Subtract the second equation from the first:
# (10a + 50b + 100c) - (10a + 1b + 5c) = 100 - 8
# 49b + 95c = 92  -> Equation (4)

# Step 2: Eliminate `a` using the first and third equations.
# Multiply the first equation by 5 and the third equation by 1 to align the coefficients of `a`:
# 5(1a + 5b + 10c = 10) -> 5a + 25b + 50c = 50
# 1(5a + 10b + 1c = 6) -> 5a + 10b + 1c = 6

# Subtract the second equation from the first:
# (5a + 25b + 50c) - (5a + 10b + 1c) = 50 - 6
# 15b + 49c = 44  -> Equation (5)

# Step 3: Solve the system of two equations (4 and 5) with two variables (`b` and `c`):
# Equation (4): 49b + 95c = 92
# Equation (5): 15b + 49c = 44

# Multiply Equation (5) by 49 and Equation (4) by 15 to align the coefficients of `b`:
# 49(15b + 49c = 44) -> 735b + 2401c = 2156
# 15(49b + 95c = 92) -> 735b + 1425c = 1380

# Subtract the second equation from the first:
# (735b + 2401c) - (735b + 1425c) = 2156 - 1380
# 976c = 776
# c = 776 / 976 = Fraction(194, 244) = Fraction(97, 122)

# Substitute `c = 97/122` into Equation (5) to solve for `b`:
# 15b + 49(97/122) = 44
# 15b + 4753/122 = 44
# 15b = 44 - 4753/122
# 15b = (5376/122) - (4753/122)
# 15b = 623/122
# b = (623/122) / 15 = 623 / (122 * 15) = Fraction(623, 1830)

# Substitute `b = 623/1830` and `c = 97/122` into the first equation to solve for `a`:
# 1a + 5(623/1830) + 10(97/122) = 10
# 1a + (3115/1830) + (970/122) = 10
# 1a + (3115/1830) + (14585/1830) = 10
# 1a + (17700/1830) = 10
# 1a = 10 - (17700/1830)
# 1a = (18300/1830) - (17700/1830)
# 1a = 600/1830 = Fraction(200, 610) = Fraction(100, 305)

# Final answers:
a = Fraction(100, 305)  # Chickens eaten by 1 Ling
b = Fraction(623, 1830)  # Chickens eaten by 1 Li
c = Fraction(97, 122)  # Chickens eaten by 1 Congzhe

a, b, c#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 45/122, Actual: 20/61
Variable 'b' has wrong value. Expected: 41/122, Actual: 623/1830"""
