"""
今有上禾五秉，損實一斗一升，當下禾七秉。上禾七秉，損實二斗五升，當下禾五秉。問︰上、下禾實一秉各幾何？
術曰：如方程，置上禾五秉正，下禾七秉負，損實一斗一升正。次置上禾七秉正，下禾五秉負，損實二斗五升正。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：上禾 a秉 b升 ，下禾 c秉 d升 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves solving a system of linear equations to determine the values of the unknowns. Here's the Python code:


"""


from fractions import Fraction

# Define the equations based on the problem:
# Equation 1: 5a - 7c = 1斗1升 (1斗 = 10升, so 1斗1升 = 10 + 1 = 11升)
# Equation 2: 7a - 5c = 2斗5升 (2斗 = 20升, so 2斗5升 = 20 + 5 = 25升)

# Convert the equations into a system of linear equations:
# 5a - 7c = 11
# 7a - 5c = 25

# Solve for 'a' (上禾實一秉) and 'c' (下禾實一秉):
# Multiply the first equation by 7 and the second equation by 5 to eliminate 'c':
# 35a - 49c = 77
# 35a - 25c = 125

# Subtract the first equation from the second:
# (35a - 25c) - (35a - 49c) = 125 - 77
# 24c = 48
c = Fraction(48, 24)  # 下禾實一秉
c = Fraction(2)  # Simplify

# Substitute 'c' back into the first equation to solve for 'a':
# 5a - 7(2) = 11
# 5a - 14 = 11
# 5a = 25
a = Fraction(25, 5)  # 上禾實一秉
a = Fraction(5)  # Simplify

# Now we know 'a' and 'c'. To find the remaining units (升), we calculate the fractional part:
# 上禾實一秉 = a秉 b升
# 下禾實一秉 = c秉 d升

# Since the problem states that the solution is in terms of 1斗 (10升), we already have the answer:
b = 0  # 上禾實一秉 has no additional 升
d = 0  # 下禾實一秉 has no additional 升

# Final answers:
a = Fraction(5)  # 上禾實一秉
b = Fraction(0)  # 上禾實 additional 升
c = Fraction(2)  # 下禾實一秉
d = Fraction(0)  # 下禾實 additional 升


"""


### Explanation of the solution:
1. The problem is translated into a system of linear equations.
2. The equations are solved using substitution and elimination methods.
3. The results are expressed in terms of 秉 (a unit of measure) and 升 (a smaller unit of measure, where 1斗 = 10升).

### Final Results:
- 上禾實一秉 (a) = 5秉
- 上禾實 additional 升 (b) = 0升
- 下禾實一秉 (c) = 2秉
- 下禾實 additional 升 (d) = 0升
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 5
Variable 'b' has wrong value. Expected: 5, Actual: 0
Variable 'c' has wrong value. Expected: 1, Actual: 2
Variable 'd' has wrong value. Expected: 2, Actual: 0"""
