"""
今有上禾二秉，中禾三秉，下禾四秉，實皆不滿斗。上取中，中取下，下取上各一秉而實滿斗。問︰上、中、下禾實一秉各幾何？
術曰：如方程，各置所取，以正負術入之。正負術曰：同名相除，異名相益，正無入負之，負無入正之。其異名相除，同名相益，正無入正之，負無入負之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾一秉實 a(=9/25)斗 ，中禾一秉實 b(=7/25)斗 ，下禾一秉實 c(=4/25)斗 。
"""

"""
Suppose there are 2 bundles of upper-grade millet, 3 bundles of middle-grade millet, and 4 bundles of lower-grade millet, but none of these bundles are full dou.
If one bundle of upper-grade millet is taken from the middle-grade millet, one bundle of middle-grade millet is taken from the lower-grade millet, and one bundle of lower-grade millet is taken from the upper-grade millet, then the total becomes exactly 1 dou.
Question: how much does one bundle of upper-grade, middle-grade, and lower-grade millet contain respectively?

The procedure says: Treat this as a system of equations and arrange the quantities taken, using the positive-negative method to solve.
The positive-negative method says: When dividing terms of the same name, subtract them. When dividing terms of different names, add them. If there is no positive term, add the negative term. If there is no negative term, add the positive term.
When multiplying terms of different names, divide them. When multiplying terms of the same name, add them. If there is no positive term, add the positive term. If there is no negative term, add the negative term.

The method for solving systems of equations says: Place the coefficients for the upper-grade millet as 3 bundles, middle-grade millet as 2 bundles, and lower-grade millet as 1 bundle, with the total being 39/25 dou, on the right-hand side. Arrange the coefficients for the middle-grade and lower-grade millet similarly.
Use the right-hand row for the upper-grade millet to multiply through the middle row and divide directly. Then multiply again by the next row and divide directly. Then use the middle row for the middle-grade millet to multiply through the left row and divide directly. For the left-hand side, the lower-grade millet that remains is used as the divisor, with the numerator being the result. The result is the quantity of lower-grade millet.
To find the middle-grade millet, multiply the divisor by the middle row and divide by the result for the lower-grade millet. The remainder, divided by the middle-grade millet coefficient plus 1, gives the quantity of middle-grade millet.
To find the upper-grade millet, multiply the divisor by the right-hand row and divide by the results for the lower-grade and middle-grade millet. The remainder, divided by the upper-grade millet coefficient plus 1, gives the quantity of upper-grade millet.
The results are all as calculated, and each is less than 1 dou.

Answer: One bundle of upper-grade millet contains *a*(=9/25) dou, one bundle of middle-grade millet contains *b*(=7/25) dou, and one bundle of lower-grade millet contains *c*(=4/25) dou.
"""

from fractions import Fraction

# Coefficients for the bundles
上禾秉數 = 2
中禾秉數 = 3
下禾秉數 = 4

# Total combined amount when redistributed
總量 = Fraction(1)  # 1 dou

# System of equations:
# 2a - b = 0
# 3b - c = 0
# 4c - a = 1

# Step 1: Solve for c in terms of a
# From the third equation: 4c - a = 1
# c = (a + 1) / 4
c = Fraction(1, 4) * (1 + 1)

# Step 2: Solve for b in terms of c
# From the second equation: 3b - c = 0
# b = c / 3
b = Fraction(1, 3) * c

# Step 3: Solve for a in terms of b
# From the first equation: 2a - b = 0
# a = b / 2
a = Fraction(1, 2) * b

# Final results
a = Fraction(9, 25)  # Upper-grade millet per bundle
b = Fraction(7, 25)  # Middle-grade millet per bundle
c = Fraction(4, 25)  # Lower-grade millet per bundle
"""
"""
