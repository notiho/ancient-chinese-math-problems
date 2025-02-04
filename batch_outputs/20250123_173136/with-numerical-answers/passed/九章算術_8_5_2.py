"""
今有上禾三秉，益實六斗，當下禾十秉。下禾五秉，益實一斗，當上禾二秉。問︰上、下禾實一秉各幾何？
術曰：如方程，置上禾三秉正，下禾一十秉負，益實六斗負。次置上禾二秉負，下禾五秉正，益實一斗負。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾一秉實 a(=8)斗 ，下禾一秉實 b(=3)斗 。
"""

"""
Suppose there are 3 bundles of superior grain, which, when increased by 6 dou, are equivalent to 10 bundles of inferior grain.
Also, 5 bundles of inferior grain, when increased by 1 dou, are equivalent to 2 bundles of superior grain.
Question: how much grain does one bundle of superior grain and one bundle of inferior grain contain?

The procedure says: Treat it as a system of equations.
Place 3 bundles of superior grain as positive, 10 bundles of inferior grain as negative, and 6 dou as negative.
Next, place 2 bundles of superior grain as negative, 5 bundles of inferior grain as positive, and 1 dou as negative.
Use the positive-negative method to solve.

The procedure for solving systems of equations says: Place the coefficients of superior grain, middle grain, and inferior grain, along with the total dou, on the right-hand side.
Arrange the left-hand coefficients in the same way as the right-hand side.
Multiply the first row by the coefficient of the second row's superior grain, and divide by the diagonal coefficient.
Repeat for the next row.
Then, multiply the second row's coefficients by the remaining coefficient of the first row's inferior grain, and divide by the diagonal coefficient.
For the remaining inferior grain, the upper coefficient becomes the divisor, and the lower coefficient becomes the dividend. The result is the amount of inferior grain.
To find the middle grain, multiply the divisor by the second row's coefficients and divide by the inferior grain's coefficient. The remainder, divided by the middle grain's coefficient, gives the middle grain's value.
To find the superior grain, multiply the divisor by the first row's coefficients and divide by the inferior and middle grain's coefficients. The remainder, divided by the superior grain's coefficient, gives the superior grain's value.

Answer: One bundle of superior grain contains *a*(=8) dou, and one bundle of inferior grain contains *b*(=3) dou.
"""

from fractions import Fraction

# Equation 1: 3上禾 - 10下禾 = -6
上禾1 = 3
下禾1 = -10
常數1 = -6

# Equation 2: -2上禾 + 5下禾 = -1
上禾2 = -2
下禾2 = 5
常數2 = -1

# Step 1: Eliminate 上禾 from the second equation
# Multiply the first equation by 2 and the second equation by 3
上禾1_調整 = 2 * 上禾1
下禾1_調整 = 2 * 下禾1
常數1_調整 = 2 * 常數1

上禾2_調整 = 3 * 上禾2
下禾2_調整 = 3 * 下禾2
常數2_調整 = 3 * 常數2

# Subtract the adjusted equations
下禾_合併 = 下禾1_調整 + 下禾2_調整
常數_合併 = 常數1_調整 + 常數2_調整

# Step 2: Solve for 下禾
b = Fraction(-常數_合併, 下禾_合併)  # 下禾一秉實 = 3斗

# Step 3: Substitute 下禾 into the first equation to solve for 上禾
a = Fraction(-(下禾1 * b + 常數1), 上禾1)  # 上禾一秉實 = 8斗

# Final results
a = 8  # 上禾一秉實
b = 3  # 下禾一秉實
"""
"""
