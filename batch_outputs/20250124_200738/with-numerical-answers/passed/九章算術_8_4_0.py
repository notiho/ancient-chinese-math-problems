"""
今有上禾六秉，損實一斗八升，當下禾一十秉。下禾十五秉，損實五升，當上禾五秉。問︰上、下禾實一秉各幾何？
術曰：如方程，置上禾六秉正，下禾一十秉負，損實一斗八升正。次置上禾五秉負，下禾一十五秉正，損實五升正。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾一秉實 a(=8)升 ，下禾一秉實 b(=3)升 。
"""

#----- content starts here -----
"""
Suppose there are 6 bundles of superior grain, which lose 1 dou and 8 sheng in weight, equivalent to 10 bundles of inferior grain.
And 15 bundles of inferior grain lose 5 sheng in weight, equivalent to 5 bundles of superior grain.
Question: how much does one bundle of superior grain and one bundle of inferior grain weigh respectively?

The procedure says: As in the method of simultaneous equations, place 6 bundles of superior grain as positive, 10 bundles of inferior grain as negative, and the loss of 1 dou and 8 sheng as positive.
Next, place 5 bundles of superior grain as negative, 15 bundles of inferior grain as positive, and the loss of 5 sheng as positive.
Use the method of positive and negative to solve.

The method of simultaneous equations says: Place 3 bundles of superior grain, 2 bundles of middle grain, and 1 bundle of inferior grain, with a total weight of 39 dou, on the right side.
The middle and left grains are arranged as on the right side.
Multiply the top row of superior grain by the middle row and divide by the diagonal.
Then multiply the next row and also divide by the diagonal.
For the middle row, multiply the middle grain row by the left row and divide by the diagonal.
For the left side, if the inferior grain is not fully divisible, the top becomes the divisor and the bottom becomes the dividend.
The result is the weight of one bundle of inferior grain.
To find the middle grain, multiply the divisor by the middle row's weight and divide by the weight of the inferior grain.
The remainder, divided by the number of middle grain bundles plus one, gives the weight of one bundle of middle grain.
To find the superior grain, multiply the divisor by the right row's weight and divide by the weight of the inferior and middle grains.
The remainder, divided by the number of superior grain bundles plus one, gives the weight of one bundle of superior grain.
The weights are all calculated according to the rules, and each is obtained as 1 dou.

Answer: One bundle of superior grain weighs *a*(=8) sheng, and one bundle of inferior grain weighs *b*(=3) sheng.
"""

from fractions import Fraction

# 上禾六秉正，下禾一十秉負，損實一斗八升正
eq1_上禾 = 6
eq1_下禾 = -10
eq1_損實 = 1 * 10 + 8  # Convert 1 dou 8 sheng to sheng

# 上禾五秉負，下禾一十五秉正，損實五升正
eq2_上禾 = -5
eq2_下禾 = 15
eq2_損實 = 5  # 5 sheng

# Solve using simultaneous equations
# Multiply eq1 by 15 (to eliminate 下禾), and eq2 by 10 (to eliminate 下禾)
eq1_scaled = [15 * eq1_上禾, 15 * eq1_下禾, 15 * eq1_損實]
eq2_scaled = [10 * eq2_上禾, 10 * eq2_下禾, 10 * eq2_損實]

# Subtract the equations to eliminate 下禾
上禾_coeff = eq1_scaled[0] + eq2_scaled[0]
損實_total = eq1_scaled[2] + eq2_scaled[2]

# Solve for one bundle of superior grain
a = Fraction(損實_total, 上禾_coeff)  # 8 sheng

# Substitute back to find one bundle of inferior grain
下禾_coeff = eq1_下禾
損實_remaining = eq1_損實 - eq1_上禾 * a
b = Fraction(損實_remaining, 下禾_coeff)  # 3 sheng#----- content ends here -----

"""
"""
