"""
今有上禾六秉損實一斗八升當下禾一十秉下禾十五秉損實五升當上禾五秉問上下禾實一秉各幾何
術曰如方程置上禾六秉正下禾一十秉負損實一斗八升正次置上禾五秉負下禾一十五秉正損實五升正以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
荅曰上禾一秉實 a升 下禾一秉實 b升 
"""

"""
Suppose there are 6 bundles of superior millet (上禾), with a loss of 1 dou and 8 sheng. 
This corresponds to 10 bundles of inferior millet (下禾). 
There are 15 bundles of inferior millet, with a loss of 5 sheng. 
This corresponds to 5 bundles of superior millet. 
Question: how much grain does one bundle of superior millet and one bundle of inferior millet yield?

The procedure says: Treat it as a system of linear equations.
Place 6 bundles of superior millet as positive, 10 bundles of inferior millet as negative, and the loss of 1 dou and 8 sheng as positive. 
Next, place 5 bundles of superior millet as negative, 15 bundles of inferior millet as positive, and the loss of 5 sheng as positive. 
Use the positive-negative method to solve.

The procedure for solving systems of equations says: 
Place 3 bundles of superior millet, 2 bundles of middle millet, and 1 bundle of inferior millet, with a total yield of 39 dou on the right side. 
Align the left-hand millet terms as on the right-hand side. 
Using the right-hand row of superior millet, multiply it across the middle row and divide directly. 
Then multiply it across the next row and divide directly again. 
For the middle row, if there is a remainder, multiply it across the left-hand row and divide directly. 
For the left-hand inferior millet, if there is a remainder, take the upper term as the divisor and the lower term as the dividend. 
The result is the yield of inferior millet. 
To find the yield of middle millet, multiply the divisor by the middle row's remainder and divide by the inferior millet's yield. 
The remainder corresponds to the number of middle millet bundles, and the result is the yield of middle millet. 
To find the yield of superior millet, multiply the divisor by the right-hand row's remainder and divide by the yields of inferior and middle millet. 
The remainder corresponds to the number of superior millet bundles, and the result is the yield of superior millet. 
All results follow this method, and each yields 1 dou.

Answer: one bundle of superior millet yields *a* sheng, and one bundle of inferior millet yields *b* sheng.
"""

# 上禾六秉損實一斗八升
上禾1 = 6
損實1 = 1 * 10 + 8  # Convert 1 dou 8 sheng to sheng

# 下禾一十秉
下禾1 = -10

# 下禾十五秉損實五升
下禾2 = 15
損實2 = 5  # 5 sheng

# 上禾五秉
上禾2 = -5

# Solve the system of equations using the positive-negative method
# Equation 1: 6a - 10b = 18 (損實1 in sheng)
# Equation 2: -5a + 15b = 5 (損實2 in sheng)

# Step 1: Eliminate one variable by multiplying and adding equations
# Multiply Equation 1 by 5 and Equation 2 by 6 to align coefficients of 'a'
eq1 = 5 * 6 * 上禾1 - 5 * 10 * 下禾1 - 5 * 損實1
eq2 = 6 * -5 * 上禾2 + 6 * 15 * 下禾2 - 6 * 損實2

# Add the two equations to eliminate 'a'
combined = eq1 + eq2

# Solve for 'b' (下禾一秉實)
b = Fraction(combined, 5 * 15 - 6 * -10)

# Substitute 'b' back into one of the original equations to solve for 'a' (上禾一秉實)
a = Fraction(損實1 - 10 * b, 6)

# Results
a = a  # 上禾一秉實 in sheng
b = b  # 下禾一秉實 in sheng
"""
Variable 'a' has wrong value. Expected: 8, Actual: -1817/81
Variable 'b' has wrong value. Expected: 3, Actual: 412/27"""
