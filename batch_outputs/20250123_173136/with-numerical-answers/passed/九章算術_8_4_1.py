"""
今有上禾六秉，損實一斗八升，當下禾一十秉。下禾十五秉，損實五升，當上禾五秉。問︰上、下禾實一秉各幾何？
術曰：如方程，置上禾六秉正，下禾一十秉負，損實一斗八升正。次置上禾五秉負，下禾一十五秉正，損實五升正。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾一秉實 a(=8)升 ，下禾一秉實 b(=3)升 。
"""

"""
Suppose there are 6 bundles of superior grain, which lose 1 dou and 8 sheng of substance, equivalent to 10 bundles of inferior grain.
And suppose there are 15 bundles of inferior grain, which lose 5 sheng of substance, equivalent to 5 bundles of superior grain.
Question: how much substance does one bundle of superior grain and one bundle of inferior grain contain?

The procedure says: As in the method of simultaneous equations, place 6 bundles of superior grain as positive, 10 bundles of inferior grain as negative, and the loss of 1 dou and 8 sheng as positive.
Next, place 5 bundles of superior grain as negative, 15 bundles of inferior grain as positive, and the loss of 5 sheng as positive.
Use the method of positive and negative to solve.

The method of simultaneous equations says: Place 3 bundles of superior grain, 2 bundles of middle grain, and 1 bundle of inferior grain, with 39 dou on the right side.
Arrange the middle and left grains as on the right side.
Multiply the top row of superior grain across the middle row and divide directly.
Then multiply the next row and divide directly again.
For the middle row, multiply the middle grain row across the left row and divide directly.
For the left side, if the inferior grain is not fully divisible, take the upper as the divisor and the lower as the dividend.
The result is the substance of the inferior grain.
To find the middle grain, multiply the divisor by the middle row's lower result and divide by the inferior grain's result.
The remainder, divided by the middle grain's bundle count plus one, is the middle grain's substance.
To find the superior grain, multiply the divisor by the right row's lower result and divide by the inferior and middle grain's results.
The remainder, divided by the superior grain's bundle count plus one, is the superior grain's substance.
The results are as per the method, with each obtaining 1 dou.

Answer: One bundle of superior grain contains *a*(=8) sheng, and one bundle of inferior grain contains *b*(=3) sheng.
"""

from fractions import Fraction

# 上禾六秉正，下禾一十秉負，損實一斗八升正
eq1_上禾 = 6
eq1_下禾 = -10
eq1_實 = 1 * 10 + 8  # 1斗8升 converted to sheng

# 上禾五秉負，下禾一十五秉正，損實五升正
eq2_上禾 = -5
eq2_下禾 = 15
eq2_實 = 5  # 5升

# Solve using elimination
# Multiply eq1 by 5 and eq2 by 6 to align 上禾 coefficients
eq1_上禾_scaled = eq1_上禾 * 5
eq1_下禾_scaled = eq1_下禾 * 5
eq1_實_scaled = eq1_實 * 5

eq2_上禾_scaled = eq2_上禾 * 6
eq2_下禾_scaled = eq2_下禾 * 6
eq2_實_scaled = eq2_實 * 6

# Eliminate 上禾
下禾_combined = eq1_下禾_scaled + eq2_下禾_scaled
實_combined = eq1_實_scaled + eq2_實_scaled

# Solve for 下禾實 (one bundle of inferior grain)
b = Fraction(實_combined, 下禾_combined)  # 下禾一秉實 = 3升

# Substitute b back into eq1 to solve for 上禾實 (one bundle of superior grain)
上禾_combined = eq1_上禾
實_combined = eq1_實 - (eq1_下禾 * b)

a = Fraction(實_combined, 上禾_combined)  # 上禾一秉實 = 8升

a, b  # 8升, 3升
"""
"""
