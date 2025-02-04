"""
今有上禾六秉損實一斗八升當下禾一十秉下禾十五秉損實五升當上禾五秉問上下禾實一秉各幾何
術曰如方程置上禾六秉正下禾一十秉負損實一斗八升正次置上禾五秉負下禾一十五秉正損實五升正以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
荅曰上禾一秉實 a升 下禾一秉實 b升 
"""

#----- content starts here -----
"""
Suppose there are 6 bundles of superior millet (上禾), with a loss of 1 dou and 8 sheng.
There are 10 bundles of inferior millet (下禾).
There are 15 bundles of inferior millet (下禾), with a loss of 5 sheng.
There are 5 bundles of superior millet (上禾).
Question: how much grain does one bundle of superior millet and one bundle of inferior millet yield respectively?

The procedure says: Treat it as a system of linear equations.
Place 6 bundles of superior millet as positive, 10 bundles of inferior millet as negative, and the loss of 1 dou and 8 sheng as positive.
Next, place 5 bundles of superior millet as negative, 15 bundles of inferior millet as positive, and the loss of 5 sheng as positive.
Use the method of positive and negative to solve.

The method for solving systems of equations says: Place 3 bundles of superior millet, 2 bundles of medium millet, and 1 bundle of inferior millet, with a total yield of 39 dou on the right side.
For the left side, arrange the superior, medium, and inferior millet in columns as on the right side.
Use the top row of the right side to multiply the middle row, and divide directly.
Then multiply the next row and divide directly again.
For the middle row, if there is a remainder, multiply it by the left row and divide directly.
For the left side, if there is a remainder, the top becomes the divisor and the bottom becomes the dividend.
The result is the yield of inferior millet.
To find the yield of medium millet, multiply the divisor by the middle row and divide by the yield of inferior millet, adjusting for the remainder.
To find the yield of superior millet, multiply the divisor by the top row and divide by the yield of inferior and medium millet, adjusting for the remainder.
The result for each is the yield per bundle.

Answer: one bundle of superior millet yields *a* sheng, and one bundle of inferior millet yields *b* sheng.
"""

from fractions import Fraction

# 上禾六秉損實一斗八升
上禾1 = 6
損實1 = 1 * 10 + 8  # Convert 1 dou 8 sheng to sheng

# 下禾一十秉
下禾1 = 10

# 下禾十五秉損實五升
下禾2 = 15
損實2 = 5  # Already in sheng

# 上禾五秉
上禾2 = 5

# 方程式表示
# Equation 1: 6a - 10b = 18 (1斗8升 = 18升)
# Equation 2: -5a + 15b = 5

# 解方程
# Multiply Equation 1 by 5 and Equation 2 by 6 to align coefficients of 'a'
eq1 = [6 * 5, -10 * 5, 18 * 5]  # 30a - 50b = 90
eq2 = [-5 * 6, 15 * 6, 5 * 6]   # -30a + 90b = 30

# Add the two equations to eliminate 'a'
combined = [0, eq1[1] + eq2[1], eq1[2] + eq2[2]]  # 40b = 120
b = Fraction(combined[2], combined[1])  # b = 120 / 40 = 3

# Substitute b = 3 into Equation 1 to solve for 'a'
a = Fraction((損實1 - 下禾1 * b), 上禾1)  # a = (18 - 10 * 3) / 6 = 2

# 答案
a升 = a  # 上禾一秉實
b升 = b  # 下禾一秉實#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 8, Actual: -2"""
