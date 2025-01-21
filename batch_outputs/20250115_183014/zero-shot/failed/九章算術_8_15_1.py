"""
今有令一人、吏五人、從者一十人，食雞一十；令一十人、吏一人、從者五人，食雞八；令五人、吏一十人、從者一人，食雞六。問︰令、吏、從者食雞各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：令 a人 食 b雞 ，吏 c人 食 d雞 ，從者 e人 食 f雞 。
"""

"""
To solve the problem, we will translate the ancient Chinese mathematical problem into Python code. The problem involves solving a system of linear equations to determine the amount of chicken consumed by each type of person (令, 吏, 從者). Here's the Python code:


"""


from fractions import Fraction

# Let:
# a = chicken consumed by one 令 (leader)
# b = chicken consumed by one 吏 (official)
# c = chicken consumed by one 從者 (attendant)

# The equations based on the problem:
# 1令 + 5吏 + 10從者 = 10 chickens
# 10令 + 1吏 + 5從者 = 8 chickens
# 5令 + 10吏 + 1從者 = 6 chickens

# Representing the equations:
# a + 5b + 10c = 10
# 10a + b + 5c = 8
# 5a + 10b + c = 6

# Solving the system of equations using substitution and elimination:
# Step 1: Eliminate one variable (e.g., c) from two equations
# From the first equation: c = (10 - a - 5b) / 10
# Substitute c into the second and third equations

# Second equation becomes:
# 10a + b + 5((10 - a - 5b) / 10) = 8
# Multiply through by 10 to eliminate the fraction:
# 100a + 10b + 50 - 5a - 25b = 80
# 95a - 15b = 30  -> Equation (4)

# Third equation becomes:
# 5a + 10b + (10 - a - 5b) / 10 = 6
# Multiply through by 10 to eliminate the fraction:
# 50a + 100b + 10 - a - 5b = 60
# 49a + 95b = 50  -> Equation (5)

# Step 2: Solve the two-variable system (Equations 4 and 5)
# 95a - 15b = 30
# 49a + 95b = 50

# Multiply the first equation by 95 and the second equation by 15 to align coefficients of b:
# 9025a - 1425b = 2850
# 735a + 1425b = 750

# Add the two equations to eliminate b:
# 9025a + 735a = 2850 + 750
# 9760a = 3600
# a = 3600 / 9760 = 45 / 122

a = Fraction(45, 122)

# Substitute a back into Equation (4) to solve for b:
# 95a - 15b = 30
# 95(45 / 122) - 15b = 30
# (4275 / 122) - 15b = 30
# -15b = 30 - (4275 / 122)
# -15b = (3660 / 122) - (4275 / 122)
# -15b = -615 / 122
# b = (615 / 122) / 15 = 41 / 122

b = Fraction(41, 122)

# Substitute a and b back into the first equation to solve for c:
# a + 5b + 10c = 10
# (45 / 122) + 5(41 / 122) + 10c = 10
# (45 / 122) + (205 / 122) + 10c = 10
# (250 / 122) + 10c = 10
# 10c = 10 - (250 / 122)
# 10c = (1220 / 122) - (250 / 122)
# 10c = 970 / 122
# c = (970 / 122) / 10 = 97 / 122

c = Fraction(97, 122)

# The solution:
# a = chicken consumed by one 令 (leader)
# b = chicken consumed by one 吏 (official)
# c = chicken consumed by one 從者 (attendant)

print("令 (leader) consumes:", a, "chickens")
print("吏 (official) consumes:", b, "chickens")
print("從者 (attendant) consumes:", c, "chickens")


"""


This code calculates the amount of chicken consumed by each type of person using fractions for precise arithmetic. The results are stored in variables `a`, `b`, and `c`.
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 45/122
Variable 'b' has wrong value. Expected: 45/122, Actual: 41/122
Variable 'c' has wrong value. Expected: 1, Actual: 97/122
Missing variable in output: 'd'
Missing variable in output: 'e'
Missing variable in output: 'f'"""
