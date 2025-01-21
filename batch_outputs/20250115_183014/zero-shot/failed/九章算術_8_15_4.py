"""
今有令一人、吏五人、從者一十人，食雞一十；令一十人、吏一人、從者五人，食雞八；令五人、吏一十人、從者一人，食雞六。問︰令、吏、從者食雞各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：令 a人 食 b雞 ，吏 c人 食 d雞 ，從者 e人 食 f雞 。
"""

"""
To solve the problem, we will translate the ancient Chinese math problem into Python code and compute the values of the unknowns. The problem involves solving a system of linear equations. Here's the Python implementation:


"""


from fractions import Fraction

# Define the equations based on the problem:
# Let:
# a = chicken consumed by one "令" (leader)
# b = chicken consumed by one "吏" (official)
# c = chicken consumed by one "從者" (attendant)

# Equations:
# 1 * a + 5 * b + 10 * c = 10
# 10 * a + 1 * b + 5 * c = 8
# 5 * a + 10 * b + 1 * c = 6

# Solve the system of equations using substitution/elimination:
# Representing the equations:
# Equation 1: a + 5b + 10c = 10
# Equation 2: 10a + b + 5c = 8
# Equation 3: 5a + 10b + c = 6

# Step 1: Eliminate "a" from equations 2 and 3 using equation 1
# Multiply equation 1 by 10 and subtract from equation 2:
# 10(a + 5b + 10c) = 100
# 10a + b + 5c - (10a + 50b + 100c) = 8 - 100
# -49b - 95c = -92  (Equation 4)

# Multiply equation 1 by 5 and subtract from equation 3:
# 5(a + 5b + 10c) = 50
# 5a + 10b + c - (5a + 25b + 50c) = 6 - 50
# -15b - 49c = -44  (Equation 5)

# Step 2: Solve for "b" and "c" using equations 4 and 5
# Multiply equation 4 by 15 and equation 5 by 49 to align coefficients of "b":
# 15(-49b - 95c) = 15(-92)
# 49(-15b - 49c) = 49(-44)
# -735b - 1425c = -1380
# -735b - 2401c = -2156

# Subtract the two equations:
# -1425c + 2401c = -1380 + 2156
# 976c = 776
c = Fraction(776, 976)

# Simplify "c":
c = c.limit_denominator()

# Substitute "c" back into equation 4 to solve for "b":
# -49b - 95c = -92
# -49b = -92 + 95c
# b = (-92 + 95c) / -49
b = Fraction(-92 + 95 * c, -49)

# Simplify "b":
b = b.limit_denominator()

# Substitute "b" and "c" back into equation 1 to solve for "a":
# a + 5b + 10c = 10
# a = 10 - 5b - 10c
a = Fraction(10 - 5 * b - 10 * c)

# Simplify "a":
a = a.limit_denominator()

# Results:
print("a (chicken consumed by one '令') =", a)
print("b (chicken consumed by one '吏') =", b)
print("c (chicken consumed by one '從者') =", c)


"""


This Python code solves the system of equations step by step using substitution and elimination, and it outputs the values of `a`, `b`, and `c` as fractions.
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 45/122
Variable 'b' has wrong value. Expected: 45/122, Actual: 41/122
Variable 'c' has wrong value. Expected: 1, Actual: 97/122
Missing variable in output: 'd'
Missing variable in output: 'e'
Missing variable in output: 'f'"""
