"""
今有令一人、吏五人、從者一十人，食雞一十；令一十人、吏一人、從者五人，食雞八；令五人、吏一十人、從者一人，食雞六。問︰令、吏、從者食雞各幾何？
荅曰：令一人食 a雞 ，吏一人食 b雞 ，從者一人食 c雞 。
"""

"""
Suppose there are three groups of people:
1. One Ling (official), five Li (clerks), and ten Congzhe (attendants) eat 10 chickens.
2. Ten Ling, one Li, and five Congzhe eat 8 chickens.
3. Five Ling, ten Li, and one Congzhe eat 6 chickens.

Question: How many chickens does one Ling, one Li, and one Congzhe eat respectively?

Answer: One Ling eats *a* chickens, one Li eats *b* chickens, and one Congzhe eats *c* chickens.
"""

# Let:
# a = number of chickens eaten by one Ling
# b = number of chickens eaten by one Li
# c = number of chickens eaten by one Congzhe

# Equations:
# 1a + 5b + 10c = 10
# 10a + 1b + 5c = 8
# 5a + 10b + 1c = 6

# Solve the system of equations using substitution/elimination:
from fractions import Fraction

# Step 1: Solve for a, b, c
# Multiply the first equation by 10 to eliminate fractions:
# 10a + 50b + 100c = 100
# Subtract the second equation:
# (10a + 50b + 100c) - (10a + 1b + 5c) = 100 - 8
# 49b + 95c = 92  (Equation 4)

# Multiply the first equation by 5 to eliminate fractions:
# 5a + 25b + 50c = 50
# Subtract the third equation:
# (5a + 25b + 50c) - (5a + 10b + 1c) = 50 - 6
# 15b + 49c = 44  (Equation 5)

# Step 2: Solve Equations 4 and 5 for b and c
# Multiply Equation 4 by 15 and Equation 5 by 49 to align coefficients of b:
# (15)(49b + 95c) = (15)(92)
# (49)(15b + 49c) = (49)(44)
# 735b + 1425c = 1380
# 735b + 2401c = 2156

# Subtract the two equations:
# (735b + 2401c) - (735b + 1425c) = 2156 - 1380
# 976c = 776
# c = 776 / 976 = Fraction(194, 244) = Fraction
"""
Missing variable in output: 'a'
Missing variable in output: 'b'
Missing variable in output: 'c'"""
