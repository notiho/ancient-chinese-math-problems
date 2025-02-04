"""
今有令一人、吏五人、從者一十人，食雞一十；令一十人、吏一人、從者五人，食雞八；令五人、吏一十人、從者一人，食雞六。問︰令、吏、從者食雞各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：令一人食 a雞 ，吏一人食 b雞 ，從者一人食 c雞 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into a system of linear equations and solve it using Python. The problem involves three unknowns: the amount of chicken eaten by a "令" (a), a "吏" (b), and a "從者" (c). Here's the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Define the equations based on the problem:
# 1. a + 5b + 10c = 10
# 2. 10a + b + 5c = 8
# 3. 5a + 10b + c = 6

# Solve the system of equations using substitution/elimination:
# Multiply the first equation by 10 to eliminate 'a' in the second equation:
# 10a + 50b + 100c = 100
# Subtract the second equation from this:
# (10a + 50b + 100c) - (10a + b + 5c) = 100 - 8
# 49b + 95c = 92  (Equation 4)

# Multiply the first equation by 5 to eliminate 'a' in the third equation:
# 5a + 25b + 50c = 50
# Subtract the third equation from this:
# (5a + 25b + 50c) - (5a + 10b + c) = 50 - 6
# 15b + 49c = 44  (Equation 5)

# Solve Equation 4 and Equation 5 for b and c:
# Multiply Equation 5 by 49 and Equation 4 by 15 to align coefficients of b:
# 49(15b + 49c) = 49(44)
# 15(49b + 95c) = 15(92)
# 735b + 2401c = 2156
# 735b + 1425c = 1380

# Subtract the second equation from the first:
# (735b + 2401c) - (735b + 1425c) = 2156 - 1380
# 976c = 776
# c = 776 / 976 = 97 / 122

c = Fraction(97, 122)

# Substitute c back into Equation 5 to solve for b:
# 15b + 49(97/122) = 44
# 15b + 4753/122 = 44
# 15b = 44 - 4753/122
# 15b = (5376 - 4753) / 122
# 15b = 623 / 122
# b = (623 / 122) / 15
# b = 623 / (122 * 15)
# b = 623 / 1830

b = Fraction(623, 1830)

# Substitute b and c back into the first equation to solve for a:
# a + 5b + 10c = 10
# a + 5(623/1830) + 10(97/122) = 10
# a + 3115/1830 + 970/122 = 10
# a + 3115/1830 + (970 * 15) / (122 * 15) = 10
# a + 3115/1830 + 14550/1830 = 10
# a + (3115 + 14550) / 1830 = 10
# a + 17665 / 1830 = 10
# a = 10 - 17665 / 1830
# a = (18300 - 17665) / 1830
# a = 635 / 1830
# a = 127 / 366

a = Fraction(127, 366)

# Final results:
print("令一人食 a雞 =", a)
print("吏一人食 b雞 =", b)
print("從者一人食 c雞 =", c)
#----- content ends here -----


"""


### Solution:
- 令一人食 `a = 127/366` 雞
- 吏一人食 `b = 623/1830` 雞
- 從者一人食 `c = 97/122` 雞
"""


"""
Variable 'a' has wrong value. Expected: 45/122, Actual: 127/366
Variable 'b' has wrong value. Expected: 41/122, Actual: 623/1830"""
