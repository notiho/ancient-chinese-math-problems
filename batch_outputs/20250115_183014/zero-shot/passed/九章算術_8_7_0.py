"""
今有賣牛二、羊五，以買十三豕，有餘錢一千。賣牛三、豕三，以買九羊，錢適足。賣羊六、豕八，以買五牛，錢不足六百。問︰牛、羊、豕價各幾何？
術曰：如方程，置牛二、羊五正，豕一十三負，餘錢數正；次牛三正，羊九負，豕三正；次牛五負，羊六正，豕八正，不足錢負。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：牛價 a ，羊價 b ，豕價 c 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical problem into Python code. The problem involves solving a system of linear equations to determine the prices of a cow (`a`), a sheep (`b`), and a pig (`c`). Here's the Python code:


"""


from fractions import Fraction

# The system of equations is:
# 2a + 5b - 13c = 1000
# 3a - 9b + 3c = 0
# -5a + 6b + 8c = -600

# Solve the system of equations using substitution or elimination.

# Step 1: Represent the equations
# Equation 1: 2a + 5b - 13c = 1000
# Equation 2: 3a - 9b + 3c = 0
# Equation 3: -5a + 6b + 8c = -600

# Step 2: Solve for one variable in terms of the others
# From Equation 2: 3a - 9b + 3c = 0
# Divide through by 3: a - 3b + c = 0
# Rearrange: a = 3b - c

# Step 3: Substitute a = 3b - c into the other equations
# Substitute into Equation 1: 2(3b - c) + 5b - 13c = 1000
# Expand: 6b - 2c + 5b - 13c = 1000
# Combine like terms: 11b - 15c = 1000  (Equation 4)

# Substitute into Equation 3: -5(3b - c) + 6b + 8c = -600
# Expand: -15b + 5c + 6b + 8c = -600
# Combine like terms: -9b + 13c = -600  (Equation 5)

# Step 4: Solve the two-variable system (Equation 4 and Equation 5)
# Equation 4: 11b - 15c = 1000
# Equation 5: -9b + 13c = -600

# Multiply Equation 4 by 9 and Equation 5 by 11 to eliminate b:
# 9(11b - 15c) = 9(1000) -> 99b - 135c = 9000
# 11(-9b + 13c) = 11(-600) -> -99b + 143c = -6600

# Add the two equations:
# (99b - 135c) + (-99b + 143c) = 9000 + (-6600)
# 8c = 2400
# Solve for c: c = 2400 / 8 = 300

c = Fraction(300)

# Substitute c = 300 into Equation 4 to solve for b:
# 11b - 15(300) = 1000
# 11b - 4500 = 1000
# 11b = 5500
# b = 5500 / 11 = 500

b = Fraction(500)

# Substitute b = 500 and c = 300 into a = 3b - c to solve for a:
# a = 3(500) - 300
# a = 1500 - 300
# a = 1200

a = Fraction(1200)

# The prices are:
# a = 1200 (price of a cow)
# b = 500 (price of a sheep)
# c = 300 (price of a pig)


"""


### Final Results:
- `a` (price of a cow) = 1200
- `b` (price of a sheep) = 500
- `c` (price of a pig) = 300
"""


"""
"""
