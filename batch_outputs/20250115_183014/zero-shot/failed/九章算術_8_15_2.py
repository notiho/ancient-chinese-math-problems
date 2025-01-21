"""
今有令一人、吏五人、從者一十人，食雞一十；令一十人、吏一人、從者五人，食雞八；令五人、吏一十人、從者一人，食雞六。問︰令、吏、從者食雞各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：令 a人 食 b雞 ，吏 c人 食 d雞 ，從者 e人 食 f雞 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves solving a system of linear equations to determine how many chickens each type of person (令, 吏, 從者) consumes.

Here is the Python code:


"""


from fractions import Fraction

# Let:
# a = number of chickens consumed by one 令 (official)
# b = number of chickens consumed by one 吏 (clerk)
# c = number of chickens consumed by one 從者 (attendant)

# The equations are:
# 1a + 5b + 10c = 10
# 10a + 1b + 5c = 8
# 5a + 10b + 1c = 6

# Solve using substitution or elimination method.

# Step 1: Represent the equations
# Equation 1: a + 5b + 10c = 10
# Equation 2: 10a + b + 5c = 8
# Equation 3: 5a + 10b + c = 6

# Step 2: Solve for one variable in terms of the others
# From Equation 1: a = 10 - 5b - 10c

# Substitute a into Equation 2:
# 10(10 - 5b - 10c) + b + 5c = 8
# 100 - 50b - 100c + b + 5c = 8
# -49b - 95c = -92
# Equation 4: 49b + 95c = 92

# Substitute a into Equation 3:
# 5(10 - 5b - 10c) + 10b + c = 6
# 50 - 25b - 50c + 10b + c = 6
# -15b - 49c = -44
# Equation 5: 15b + 49c = 44

# Step 3: Solve the system of two equations (Equation 4 and Equation 5)
# 49b + 95c = 92
# 15b + 49c = 44

# Multiply Equation 4 by 15 and Equation 5 by 49 to eliminate b:
# 15(49b + 95c) = 15(92)
# 49(15b + 49c) = 49(44)

# 735b + 1425c = 1380
# 735b + 2401c = 2156

# Subtract the first equation from the second:
# (735b + 2401c) - (735b + 1425c) = 2156 - 1380
# 976c = 776
# c = 776 / 976
c = Fraction(776, 976)

# Simplify c:
c = Fraction(4, 5)

# Substitute c back into Equation 4 to solve for b:
# 49b + 95c = 92
# 49b + 95(Fraction(4, 5)) = 92
# 49b + 76 = 92
# 49b = 16
b = Fraction(16, 49)

# Substitute b and c into Equation 1 to solve for a:
# a + 5b + 10c = 10
# a + 5(Fraction(16, 49)) + 10(Fraction(4, 5)) = 10
# a + Fraction(80, 49) + Fraction(40, 5) = 10
# a + Fraction(80, 49) + 8 = 10
# a + Fraction(80, 49) = 2
# a = 2 - Fraction(80, 49)
a = Fraction(98, 49) - Fraction(80, 49)
a = Fraction(18, 49)

# Final results:
令 = a = Fraction(18, 49)  # Chickens consumed by one 令
吏 = b = Fraction(16, 49)  # Chickens consumed by one 吏
從者 = c = Fraction(4, 5)  # Chickens consumed by one 從者


"""


The solutions are:
- Each 令 (official) consumes `18/49` chickens.
- Each 吏 (clerk) consumes `16/49` chickens.
- Each 從者 (attendant) consumes `4/5` chickens.
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 18/49
Variable 'b' has wrong value. Expected: 45/122, Actual: 16/49
Variable 'c' has wrong value. Expected: 1, Actual: 4/5
Missing variable in output: 'd'
Missing variable in output: 'e'
Missing variable in output: 'f'"""
