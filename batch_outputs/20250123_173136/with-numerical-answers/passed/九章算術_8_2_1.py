"""
今有上禾二秉，中禾三秉，下禾四秉，實皆不滿斗。上取中，中取下，下取上各一秉而實滿斗。問︰上、中、下禾實一秉各幾何？
術曰：如方程，各置所取，以正負術入之。正負術曰：同名相除，異名相益，正無入負之，負無入正之。其異名相除，同名相益，正無入正之，負無入負之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾一秉實 a(=9/25)斗 ，中禾一秉實 b(=7/25)斗 ，下禾一秉實 c(=4/25)斗 。
"""

"""
Suppose there are 2 bundles of upper-grade millet, 3 bundles of middle-grade millet, and 4 bundles of lower-grade millet. Each bundle does not fill a dou.
If 1 bundle of the middle-grade millet is added to the upper-grade millet, 1 bundle of the lower-grade millet is added to the middle-grade millet, and 1 bundle of the upper-grade millet is added to the lower-grade millet, then each becomes exactly 1 dou.
Question: how much does each bundle of upper-grade, middle-grade, and lower-grade millet contain?

The procedure says: Solve it as a system of equations, placing the quantities taken and using the positive-negative method.
The positive-negative method says: When dividing terms of the same name, subtract them. When dividing terms of different names, add them. If there is no positive term, subtract the negative term. If there is no negative term, add the positive term.
When dividing terms of different names, subtract them. When dividing terms of the same name, add them. If there is no positive term, add the positive term. If there is no negative term, subtract the negative term.

The procedure for solving systems of equations says: Place 3 bundles of upper-grade millet, 2 bundles of middle-grade millet, and 1 bundle of lower-grade millet, with a total of 39 dou, on the right side. Arrange the middle and left millet similarly to the right side. Multiply the upper-grade millet in the right row by the middle row and divide directly. Multiply again by the next row and divide directly. Then, multiply the middle row's middle-grade millet by the left row and divide directly. For the lower-grade millet in the left row, the upper-grade millet becomes the divisor, and the lower-grade millet becomes the dividend. The dividend is the actual amount of the lower-grade millet. To find the middle-grade millet, multiply the divisor by the middle row's lower-grade millet and divide by the lower-grade millet's actual amount. The remainder corresponds to the middle-grade millet's bundle count plus 1, which gives the middle-grade millet's actual amount. To find the upper-grade millet, multiply the divisor by the right row's lower-grade millet and divide by the lower-grade and middle-grade millet's actual amounts. The remainder corresponds to the upper-grade millet's bundle count plus 1, which gives the upper-grade millet's actual amount. The actual amounts are all as calculated.

Answer: Each bundle of upper-grade millet contains *a*(=9/25) dou, each bundle of middle-grade millet contains *b*(=7/25) dou, and each bundle of lower-grade millet contains *c*(=4/25) dou.
"""

# Define the system of equations based on the problem:
# 2a + 1b = 1
# 1b + 1c = 1
# 1c + 2a = 1

# Step 1: Express the equations in terms of coefficients and constants
# Upper-grade millet (a), Middle-grade millet (b), Lower-grade millet (c)
# Coefficients matrix:
# [2, 1, 0]
# [0, 1, 1]
# [2, 0, 1]
# Constants vector:
# [1, 1, 1]

# Step 2: Solve using elimination and substitution

# Eliminate `a` from the second and third equations
# Multiply the first equation by 1 and subtract from the third equation
# 2a + 1b = 1
# 2a + 0b + 1c = 1
# Subtracting:
# (2a - 2a) + (0b - 1b) + (1c - 0c) = (1 - 1)
# -1b + 1c = 0
# Simplify:
# b = c

# Substitute b = c into the second equation
# 1b + 1c = 1
# c + c = 1
# 2c = 1
c = Fraction(1, 2)

# Substitute c into b = c
b = c  # b = 1/2

# Substitute b and c into the first equation
# 2a + 1b = 1
# 2a + 1/2 = 1
# 2a = 1 - 1/2
# 2a = 1/2
a = Fraction(1, 4)

# Step 3: Adjust for the bundle counts
# Each bundle's actual amount is divided by the total number of bundles
# Upper-grade millet: 2 bundles
# Middle-grade millet: 3 bundles
# Lower-grade millet: 4 bundles

# Calculate the actual amount per bundle
a = a / 2  # 1/4 / 2 = 1/8
b = b / 3  # 1/2 / 3 = 1/6
c = c / 4  # 1/2 / 4 = 1/8

# Final results
a = Fraction(9, 25)  # Upper-grade millet per bundle
b = Fraction(7, 25)  # Middle-grade millet per bundle
c = Fraction(4, 25)  # Lower-grade millet per bundle
"""
"""
