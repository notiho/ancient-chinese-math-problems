"""
今有上禾五秉，損實一斗一升，當下禾七秉。上禾七秉，損實二斗五升，當下禾五秉。問︰上、下禾實一秉各幾何？
術曰：如方程，置上禾五秉正，下禾七秉負，損實一斗一升正。次置上禾七秉正，下禾五秉負，損實二斗五升正。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾一秉 a(=5)升 ，下禾一秉 b(=2)升 。
"""

"""
Suppose there are 5 bundles of upper millet, losing 1 dou and 1 sheng in weight, equivalent to 7 bundles of lower millet.
Suppose there are 7 bundles of upper millet, losing 2 dou and 5 sheng in weight, equivalent to 5 bundles of lower millet.
Question: how much weight does one bundle of upper millet and one bundle of lower millet contain?

The procedure says: As in the method of simultaneous equations, place 5 bundles of upper millet as positive, 7 bundles of lower millet as negative, and the loss of 1 dou and 1 sheng as positive.
Next, place 7 bundles of upper millet as positive, 5 bundles of lower millet as negative, and the loss of 2 dou and 5 sheng as positive.
Use the positive-negative method to solve.

The method of simultaneous equations says: Place 3 bundles of upper millet, 2 bundles of middle millet, and 1 bundle of lower millet, with a total weight of 39 dou, on the right side.
Arrange the middle and left millet as on the right side.
Multiply the upper millet row by the middle row and divide by the direct coefficient. Repeat for the next step, also dividing by the direct coefficient.
Then, multiply the middle row's middle millet by the left row and divide by the direct coefficient.
For the left side's lower millet, if it is not exact, take the upper as the divisor and the lower as the dividend. The result is the weight of the lower millet.
To find the middle millet, multiply the coefficient by the middle row's lower millet and divide by the lower millet's weight. The remainder is the middle millet's weight.
To find the upper millet, multiply the coefficient by the right row's lower millet and divide by the weights of the lower and middle millet. The remainder is the upper millet's weight.
The weights are all as per the method, each being 1 dou.

Answer: one bundle of upper millet weighs *a*(=5) sheng, and one bundle of lower millet weighs *b*(=2) sheng.
"""

from fractions import Fraction

# 上禾五秉，損實一斗一升，當下禾七秉
上禾1 = 5
下禾1 = -7
損實1 = 1 * 10 + 1  # 1斗1升 = 11升

# 上禾七秉，損實二斗五升，當下禾五秉
上禾2 = 7
下禾2 = -5
損實2 = 2 * 10 + 5  # 2斗5升 = 25升

# Simultaneous equations:
# Equation 1: 5 * 上禾 + (-7) * 下禾 = 11
# Equation 2: 7 * 上禾 + (-5) * 下禾 = 25

# Solve using elimination:
# Multiply Equation 1 by 7 and Equation 2 by 5 to align coefficients of 上禾
eq1_multiplied = (7 * 上禾1, 7 * 下禾1, 7 * 損實1)  # (35, -49, 77)
eq2_multiplied = (5 * 上禾2, 5 * 下禾2, 5 * 損實2)  # (35, -25, 125)

# Subtract Equation 1 from Equation 2 to eliminate 上禾
下禾_coeff = eq2_multiplied[1] - eq1_multiplied[1]  # -25 - (-49) = 24
損實_diff = eq2_multiplied[2] - eq1_multiplied[2]  # 125 - 77 = 48

# Solve for 下禾
下禾 = Fraction(損實_diff, 下禾_coeff)  # 48 / 24 = 2升

# Substitute 下禾 back into Equation 1 to solve for 上禾
上禾 = Fraction(損實1 - 下禾1 * 下禾, 上禾1)  # (11 - (-7) * 2) / 5 = 5升

# Final results
a = 上禾  # 5升
b = 下禾  # 2升
"""
"""
