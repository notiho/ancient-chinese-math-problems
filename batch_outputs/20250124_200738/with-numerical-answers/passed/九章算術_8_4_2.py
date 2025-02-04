"""
今有上禾六秉，損實一斗八升，當下禾一十秉。下禾十五秉，損實五升，當上禾五秉。問︰上、下禾實一秉各幾何？
術曰：如方程，置上禾六秉正，下禾一十秉負，損實一斗八升正。次置上禾五秉負，下禾一十五秉正，損實五升正。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾一秉實 a(=8)升 ，下禾一秉實 b(=3)升 。
"""

#----- content starts here -----
"""
Suppose there are 6 bundles of superior grain, which lose 1 dou and 8 sheng in weight, equivalent to 10 bundles of inferior grain.
Additionally, 15 bundles of inferior grain lose 5 sheng in weight, equivalent to 5 bundles of superior grain.
Question: how much weight does one bundle of superior grain and one bundle of inferior grain have?

The procedure says: Treat this as a system of linear equations.
Place 6 bundles of superior grain as positive, 10 bundles of inferior grain as negative, and the loss of 1 dou and 8 sheng as positive.
Next, place 5 bundles of superior grain as negative, 15 bundles of inferior grain as positive, and the loss of 5 sheng as positive.
Use the method of solving equations with positive and negative terms.

The method of solving equations says: Place the coefficients of superior grain, middle grain, and inferior grain, along with the total weight, on the right side.
Align the coefficients of the middle and left grains as on the right side.
Multiply the top row by the middle row and divide by the diagonal term.
Repeat this for the next row, also dividing by the diagonal term.
Then, multiply the middle row by the remaining terms in the left row and divide by the diagonal term.
For the left side, if the inferior grain is not fully reduced, take the top term as the divisor and the bottom term as the dividend.
The result is the weight of one bundle of inferior grain.
To find the weight of one bundle of middle grain, multiply the divisor by the middle row's remaining term and divide by the inferior grain's weight.
The remainder, divided by the middle grain's coefficient, gives the weight of one bundle of middle grain.
To find the weight of one bundle of superior grain, multiply the divisor by the right row's remaining term and divide by the weights of the inferior and middle grains.
The remainder, divided by the superior grain's coefficient, gives the weight of one bundle of superior grain.
The weights are all calculated according to this method.

Answer: One bundle of superior grain weighs *a*(=8) sheng, and one bundle of inferior grain weighs *b*(=3) sheng.
"""

from fractions import Fraction

# 上禾六秉正，下禾一十秉負，損實一斗八升正
eq1_上禾 = 6
eq1_下禾 = -10
eq1_實 = 1 * 10 + 8  # 1斗8升 = 18升

# 上禾五秉負，下禾一十五秉正，損實五升正
eq2_上禾 = -5
eq2_下禾 = 15
eq2_實 = 5  # 5升

# 消去上禾
# Multiply eq1 by 5 and eq2 by 6 to align coefficients of 上禾
eq1_上禾, eq1_下禾, eq1_實 = 5 * eq1_上禾, 5 * eq1_下禾, 5 * eq1_實
eq2_上禾, eq2_下禾, eq2_實 = 6 * eq2_上禾, 6 * eq2_下禾, 6 * eq2_實

# Add the equations to eliminate 上禾
下禾 = eq1_下禾 + eq2_下禾
實 = eq1_實 + eq2_實

# Solve for 下禾 (one bundle)
b = Fraction(實, 下禾)  # 下禾一秉實 = 3升

# Substitute b back into eq1 to solve for 上禾
實 = eq1_實 - (eq1_下禾 * b)
a = Fraction(實, eq1_上禾)  # 上禾一秉實 = 8升

# Results
a, b  # a = 8升, b = 3升#----- content ends here -----

"""
"""
