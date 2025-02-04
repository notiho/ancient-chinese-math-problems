"""
今有上禾六秉，損實一斗八升，當下禾一十秉。下禾十五秉，損實五升，當上禾五秉。問︰上、下禾實一秉各幾何？
術曰：如方程，置上禾六秉正，下禾一十秉負，損實一斗八升正。次置上禾五秉負，下禾一十五秉正，損實五升正。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾一秉實 a(=8)升 ，下禾一秉實 b(=3)升 。
"""

"""
Suppose there are 6 bundles of superior grain, which lose 1 dou and 8 sheng of grain, equivalent to 10 bundles of inferior grain.
Additionally, 15 bundles of inferior grain lose 5 sheng of grain, equivalent to 5 bundles of superior grain.
Question: how much grain does one bundle of superior grain and one bundle of inferior grain yield?

The procedure says: Treat it as a system of linear equations.
Place 6 bundles of superior grain as positive, 10 bundles of inferior grain as negative, and the loss of 1 dou and 8 sheng as positive.
Next, place 5 bundles of superior grain as negative, 15 bundles of inferior grain as positive, and the loss of 5 sheng as positive.
Use the positive-negative procedure to solve.

The procedure for solving systems of equations says: Place the coefficients of superior grain, middle grain, and inferior grain, along with the total grain loss, on the right side.
Arrange the rows for the middle and left grains similarly.
Multiply the first row by the coefficient of superior grain in the second row, and divide directly.
Repeat for the next row, also dividing directly.
Then, multiply the second row by the coefficient of middle grain in the third row and divide directly.
For the left side, if the coefficient of inferior grain does not divide evenly, take the numerator as the dividend and the denominator as the divisor.
The result is the yield of inferior grain.
To find the yield of middle grain, multiply the divisor by the second row's coefficient of inferior grain and divide by the total grain loss for inferior grain.
The remainder, divided by the coefficient of middle grain, gives the yield of middle grain.
To find the yield of superior grain, multiply the divisor by the first row's coefficient of inferior grain and divide by the total grain loss for inferior and middle grains.
The remainder, divided by the coefficient of superior grain, gives the yield of superior grain.
The yields are all as per the procedure.

Answer: one bundle of superior grain yields *a*(=8) sheng, and one bundle of inferior grain yields *b*(=3) sheng.
"""

from fractions import Fraction

# Define the system of equations:
# 6 bundles of superior grain - 10 bundles of inferior grain = 1 dou 8 sheng (18 sheng)
# -5 bundles of superior grain + 15 bundles of inferior grain = 5 sheng

# Coefficients for the equations
上禾1 = 6  # Coefficient for superior grain in the first equation
下禾1 = -10  # Coefficient for inferior grain in the first equation
實1 = 18  # Grain loss in the first equation (1 dou 8 sheng = 18 sheng)

上禾2 = -5  # Coefficient for superior grain in the second equation
下禾2 = 15  # Coefficient for inferior grain in the second equation
實2 = 5  # Grain loss in the second equation (5 sheng)

# Solve using elimination:
# Multiply the first equation by 5 (coefficient of superior grain in the second equation)
# Multiply the second equation by 6 (coefficient of superior grain in the first equation)
# Then subtract to eliminate superior grain.

# Multiply equations
上禾1_乘 = 上禾1 * 5
下禾1_乘 = 下禾1 * 5
實1_乘 = 實1 * 5

上禾2_乘 = 上禾2 * 6
下禾2_乘 = 下禾2 * 6
實2_乘 = 実2 * 6

# Eliminate superior grain
下禾 = 下禾1_乘 + 下禾2_乘
實 = 實1_乘 + 實2_乘

# Solve for inferior grain (下禾)
下禾實 = Fraction(實, 下禾)  # b = 3 sheng

# Substitute back to solve for superior grain (上禾)
實1_代入 = 實1 - (下禾1 * 下禾實)
上禾實 = Fraction(實1_代入, 上禾1)  # a = 8 sheng

a = 上禾實  # 8 sheng
b = 下禾實  # 3 sheng
"""
Code error: name '実2' is not defined"""
