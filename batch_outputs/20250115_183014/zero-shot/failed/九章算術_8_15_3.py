"""
今有令一人、吏五人、從者一十人，食雞一十；令一十人、吏一人、從者五人，食雞八；令五人、吏一十人、從者一人，食雞六。問︰令、吏、從者食雞各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：令 a人 食 b雞 ，吏 c人 食 d雞 ，從者 e人 食 f雞 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical problem into Python code. The problem involves solving a system of linear equations to determine how many chickens each type of person (令, 吏, 從者) eats.

Here is the Python code:


"""


from fractions import Fraction

# Let:
# a = number of chickens eaten by one 令
# b = number of chickens eaten by one 吏
# c = number of chickens eaten by one 從者

# The system of equations is:
# 1a + 5b + 10c = 10
# 10a + 1b + 5c = 8
# 5a + 10b + 1c = 6

# Solve using substitution or elimination:
# Multiply equations to align coefficients and eliminate variables step by step.

# Step 1: Eliminate one variable (e.g., c).
# Multiply the first equation by 5 and the second equation by 10:
# 5(1a + 5b + 10c = 10) -> 5a + 25b + 50c = 50
# 10(10a + 1b + 5c = 8) -> 100a + 10b + 50c = 80

# Subtract the first modified equation from the second:
# (100a + 10b + 50c) - (5a + 25b + 50c) = 80 - 50
# 95a - 15b = 30  -> Equation (4)

# Step 2: Eliminate c using the first and third equations.
# Multiply the first equation by 1 and the third equation by 10:
# 1(1a + 5b + 10c = 10) -> 1a + 5b + 10c = 10
# 10(5a + 10b + 1c = 6) -> 50a + 100b + 10c = 60

# Subtract the first modified equation from the second:
# (50a + 100b + 10c) - (1a + 5b + 10c) = 60 - 10
# 49a + 95b = 50  -> Equation (5)

# Step 3: Solve the system of two equations (4) and (5).
# Equation (4): 95a - 15b = 30
# Equation (5): 49a + 95b = 50

# Multiply Equation (4) by 95 and Equation (5) by 15 to align coefficients of b:
# 95(95a - 15b = 30) -> 9025a - 1425b = 2850
# 15(49a + 95b = 50) -> 735a + 1425b = 750

# Add the two equations:
# (9025a - 1425b) + (735a + 1425b) = 2850 + 750
# 9760a = 3600
a = Fraction(3600, 9760)

# Simplify a:
a = a.limit_denominator()

# Substitute a back into Equation (4) to solve for b:
# 95a - 15b = 30
b = Fraction(95 * a - 30, 15)

# Simplify b:
b = b.limit_denominator()

# Substitute a and b back into the first equation to solve for c:
# 1a + 5b + 10c = 10
c = Fraction(10 - a - 5 * b, 10)

# Simplify c:
c = c.limit_denominator()

# Results:
令 = a
吏 = b
從者 = c

print(f"令 eats {令} chickens.")
print(f"吏 eats {吏} chickens.")
print(f"從者 eats {從者} chickens.")


"""


This code solves the system of linear equations step by step using substitution and elimination, and it uses the `Fraction` class to ensure precise calculations with fractions. The final results are stored in the variables `令`, `吏`, and `從者`, which represent the number of chickens eaten by each type of person.
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 45/122
Variable 'b' has wrong value. Expected: 45/122, Actual: 41/122
Variable 'c' has wrong value. Expected: 1, Actual: 97/122
Missing variable in output: 'd'
Missing variable in output: 'e'
Missing variable in output: 'f'"""
