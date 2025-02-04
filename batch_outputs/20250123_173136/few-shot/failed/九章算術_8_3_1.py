"""
今有上禾五秉，損實一斗一升，當下禾七秉。上禾七秉，損實二斗五升，當下禾五秉。問︰上、下禾實一秉各幾何？
術曰：如方程，置上禾五秉正，下禾七秉負，損實一斗一升正。次置上禾七秉正，下禾五秉負，損實二斗五升正。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾一秉 a升 ，下禾一秉 b升 。
"""

"""
Suppose there are 5 bundles of upper millet, losing 1 dou and 1 sheng of grain, equivalent to 7 bundles of lower millet.
And suppose there are 7 bundles of upper millet, losing 2 dou and 5 sheng of grain, equivalent to 5 bundles of lower millet.
Question: how much grain does one bundle of upper millet and one bundle of lower millet yield respectively?

The procedure says: Treat it as a system of linear equations.
Place 5 bundles of upper millet as positive, 7 bundles of lower millet as negative, and the loss of 1 dou and 1 sheng as positive.
Next, place 7 bundles of upper millet as positive, 5 bundles of lower millet as negative, and the loss of 2 dou and 5 sheng as positive.
Use the positive-negative method to solve.

The method for solving linear equations says: Place 3 unknowns (upper millet, middle millet, lower millet) on the left, and their total grain (39 dou) on the right.
Arrange the coefficients of the middle and left unknowns as on the right.
Multiply the top row by the second row, dividing directly by the diagonal.
Repeat for the next row, also dividing directly by the diagonal.
For the middle unknown, multiply the middle row by the left row, dividing directly by the diagonal.
For the lower unknown, if it does not divide evenly, take the top as the divisor and the bottom as the dividend.
The result is the grain of the lower millet.
To find the middle unknown, multiply the divisor by the middle row and divide by the lower unknown's grain.
The remainder, divided by the middle unknown's coefficient plus 1, gives the grain of the middle millet.
To find the upper unknown, multiply the divisor by the top row and divide by the grain of the lower and middle millet.
The remainder, divided by the upper unknown's coefficient plus 1, gives the grain of the upper millet.
All results follow this method, yielding 1 dou per unknown.

Answer: one bundle of upper millet yields *a* sheng, and one bundle of lower millet yields *b* sheng.
"""

# Convert dou and sheng to sheng (1 dou = 10 sheng)
損實1 = 1 * 10 + 1  # 1斗1升 = 11升
損實2 = 2 * 10 + 5  # 2斗5升 = 25升

# Set up the equations:
# 5上禾 - 7下禾 = 11升
# 7上禾 - 5下禾 = 25升

# Coefficients of the equations
上禾1, 下禾1, 常數1 = 5, -7, 11
上禾2, 下禾2, 常數2 = 7, -5, 25

# Solve using elimination:
# Multiply the first equation by 7 and the second equation by 5 to align coefficients of 上禾
方程1 = (上禾1 * 7, 下禾1 * 7, 常數1 * 7)  # (35上禾, -49下禾, 77升)
方程2 = (上禾2 * 5, 下禾2 * 5, 常數2 * 5)  # (35上禾, -25下禾, 125升)

# Subtract the second equation from the first to eliminate 上禾
_, 下禾系數, 常數差 = 方程1[1] - 方程2[1], 方程1[2] - 方程2[2]

# Solve for 下禾
b = Fraction(常數差, 下禾系數)

# Substitute b back into the first equation to solve for 上禾
a = Fraction(常數1 - 下禾1 * b, 上禾1)

# Convert results to sheng
a = a  # 上禾一秉的實
b = b  # 下禾一秉的實
"""
Code error: not enough values to unpack (expected 3, got 2)"""
