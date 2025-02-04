"""
今有上禾五秉，損實一斗一升，當下禾七秉。上禾七秉，損實二斗五升，當下禾五秉。問︰上、下禾實一秉各幾何？
術曰：如方程，置上禾五秉正，下禾七秉負，損實一斗一升正。次置上禾七秉正，下禾五秉負，損實二斗五升正。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾一秉 a(=5)升 ，下禾一秉 b(=2)升 。
"""

#----- content starts here -----
"""
Suppose there are 5 bundles of upper millet, losing 1 dou and 1 sheng of grain, equivalent to 7 bundles of lower millet.
Also, suppose there are 7 bundles of upper millet, losing 2 dou and 5 sheng of grain, equivalent to 5 bundles of lower millet.
Question: how much grain does one bundle of upper millet and one bundle of lower millet yield?

The procedure says: Treat it as a system of linear equations.
Place 5 bundles of upper millet as positive, 7 bundles of lower millet as negative, and 1 dou and 1 sheng as positive.
Next, place 7 bundles of upper millet as positive, 5 bundles of lower millet as negative, and 2 dou and 5 sheng as positive.
Use the positive-negative method to solve.

The method for solving linear equations says:
Place 3 bundles of upper millet, 2 bundles of middle millet, and 1 bundle of lower millet, with a total of 39 dou on the right side.
Arrange the middle and left millet as on the right side.
Multiply the upper row by the middle row and divide by the diagonal.
Repeat for the next step, also dividing by the diagonal.
Then, multiply the middle row by the lower row and divide by the diagonal.
For the lower millet, if it is not exact, take the upper as the divisor and the lower as the dividend.
The result is the yield of one bundle of lower millet.
To find the middle millet, multiply the middle row by the lower result and divide by the yield of the lower millet.
The remainder, divided by the number of middle millet bundles plus one, gives the yield of one bundle of middle millet.
To find the upper millet, multiply the right row by the lower result and divide by the yields of the lower and middle millet.
The remainder, divided by the number of upper millet bundles plus one, gives the yield of one bundle of upper millet.
The yields are all as calculated, each yielding 1 dou.

Answer: one bundle of upper millet yields *a*(=5) sheng, and one bundle of lower millet yields *b*(=2) sheng.
"""

from fractions import Fraction

# 上禾五秉正，下禾七秉負，損實一斗一升正
eq1_upper = 5
eq1_lower = -7
eq1_loss = 1 * 10 + 1  # Convert 1 dou 1 sheng to sheng

# 上禾七秉正，下禾五秉負，損實二斗五升正
eq2_upper = 7
eq2_lower = -5
eq2_loss = 2 * 10 + 5  # Convert 2 dou 5 sheng to sheng

# Solve the system of equations using elimination
# Multiply eq1 by 7 and eq2 by 5 to align the upper millet coefficients
eq1_upper_scaled = eq1_upper * 7
eq1_lower_scaled = eq1_lower * 7
eq1_loss_scaled = eq1_loss * 7

eq2_upper_scaled = eq2_upper * 5
eq2_lower_scaled = eq2_lower * 5
eq2_loss_scaled = eq2_loss * 5

# Subtract the scaled equations to eliminate the upper millet term
lower_coefficient = eq1_lower_scaled - eq2_lower_scaled
loss_coefficient = eq1_loss_scaled - eq2_loss_scaled

# Solve for one bundle of lower millet
b = Fraction(loss_coefficient, lower_coefficient)  # b = 2 sheng

# Substitute b into one of the original equations to solve for one bundle of upper millet
a = Fraction(eq1_loss - eq1_lower * b, eq1_upper)  # a = 5 sheng

a, b  # a = 5 sheng, b = 2 sheng#----- content ends here -----

"""
"""
