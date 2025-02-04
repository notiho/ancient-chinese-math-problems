"""
今有上禾六秉損實一斗八升當下禾一十秉下禾十五秉損實五升當上禾五秉問上下禾實一秉各幾何
術曰如方程置上禾六秉正下禾一十秉負損實一斗八升正次置上禾五秉負下禾一十五秉正損實五升正以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
荅曰上禾一秉實 a升 下禾一秉實 b升 
"""

"""
Suppose there are 6 bundles of superior millet, with a loss of 1 dou and 8 sheng. 
This corresponds to 10 bundles of inferior millet. 
Additionally, there are 15 bundles of inferior millet, with a loss of 5 sheng. 
This corresponds to 5 bundles of superior millet. 
Question: How much grain does one bundle of superior millet and one bundle of inferior millet yield?

The procedure says: Treat this as a system of linear equations. 
Place 6 bundles of superior millet as positive, 10 bundles of inferior millet as negative, and the loss of 1 dou and 8 sheng as positive. 
Next, place 5 bundles of superior millet as negative, 15 bundles of inferior millet as positive, and the loss of 5 sheng as positive. 
Use the positive-negative method to solve.

The procedure for solving systems of equations says: Place the coefficients of the superior millet, middle millet, and inferior millet, along with the total yield, on the right-hand side. 
Arrange the left-hand side coefficients similarly. 
Multiply the superior millet row by the middle millet row and divide directly. 
Repeat for the next row, dividing directly. 
For the middle millet, multiply the middle row by the left row and divide directly. 
For the inferior millet, use the superior millet as the divisor and the inferior millet as the dividend. 
The result is the yield of the inferior millet. 
To find the middle millet, multiply the divisor by the middle row and divide by the inferior millet's yield. 
The remainder corresponds to the middle millet's yield. 
To find the superior millet, multiply the divisor by the superior row and divide by the inferior and middle millet's yield. 
The remainder corresponds to the superior millet's yield. 
The results are as per the procedure.

Answer: One bundle of superior millet yields *a* sheng, and one bundle of inferior millet yields *b* sheng.
"""

from fractions import Fraction

# Convert dou and sheng to sheng (1 dou = 10 sheng)
損實1 = 1 * 10 + 8  # 1 dou 8 sheng
損實2 = 5  # 5 sheng

# Coefficients for the equations
# Equation 1: 6上禾 - 10下禾 = 1斗8升
上禾1 = 6
下禾1 = -10
常數1 = 損實1

# Equation 2: -5上禾 + 15下禾 = 5升
上禾2 = -5
下禾2 = 15
常數2 = 損實2

# Solve using elimination
# Multiply the first equation by 5 and the second equation by 6 to align 上禾 coefficients
上禾系數 = 上禾1 * 5 - 上禾2 * 6
下禾系數 = 下禾1 * 5 - 下禾2 * 6
常數項 = 常數1 * 5 - 常數2 * 6

# Solve for 下禾 (one bundle of inferior millet)
下禾每秉實 = Fraction(常數項, 下禾系數)

# Substitute 下禾 into the first equation to solve for 上禾 (one bundle of superior millet)
上禾每秉實 = Fraction(常數1 - 下禾1 * 下禾每秉實, 上禾1)

# Results
a = 上禾每秉實  # Yield of one bundle of superior millet in sheng
b = 下禾每秉實  # Yield of one bundle of inferior millet in sheng
"""
Variable 'a' has wrong value. Expected: 8, Actual: 16/7
Variable 'b' has wrong value. Expected: 3, Actual: -3/7"""
