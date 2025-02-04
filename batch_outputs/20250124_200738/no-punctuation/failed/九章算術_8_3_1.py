"""
今有上禾五秉損實一斗一升當下禾七秉上禾七秉損實二斗五升當下禾五秉問上下禾實一秉各幾何
術曰如方程置上禾五秉正下禾七秉負損實一斗一升正次置上禾七秉正下禾五秉負損實二斗五升正以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
荅曰上禾一秉 a升 下禾一秉 b升 
"""

#----- content starts here -----
"""
Suppose there are 5 bundles of superior grain, which lose 1 dou and 1 sheng in total when processed, and correspond to 7 bundles of inferior grain.
Similarly, 7 bundles of superior grain lose 2 dou and 5 sheng in total when processed, and correspond to 5 bundles of inferior grain.
Question: how much processed grain does one bundle of superior grain and one bundle of inferior grain yield?

The procedure says: Treat this as a system of linear equations.
Place 5 bundles of superior grain as positive, 7 bundles of inferior grain as negative, and the loss of 1 dou and 1 sheng as positive.
Next, place 7 bundles of superior grain as positive, 5 bundles of inferior grain as negative, and the loss of 2 dou and 5 sheng as positive.
Use the method of solving linear equations.

The method for solving linear equations says: Place the coefficients of superior grain, middle grain, and inferior grain, along with the total processed grain, on the right side.
For the middle and left grains, arrange them similarly to the right side.
Using the right row, multiply the superior grain row throughout, and divide directly.
Then multiply the next row similarly and divide directly.
For the middle row, multiply the middle grain row by the remaining terms and divide directly.
For the left row, multiply the inferior grain row by the remaining terms, using the superior grain as the divisor and the inferior grain as the dividend.
The result is the processed grain for the inferior grain.
To find the middle grain, multiply the middle row by the divisor and divide by the remaining terms.
To find the superior grain, multiply the right row by the divisor and divide by the remaining terms.
The results are the processed grain for each type of grain.

Answer: one bundle of superior grain yields *a* sheng, and one bundle of inferior grain yields *b* sheng.
"""

from fractions import Fraction

# Convert dou and sheng to sheng (1 dou = 10 sheng)
損實1 = 1 * 10 + 1  # 1 dou 1 sheng = 11 sheng
損實2 = 2 * 10 + 5  # 2 dou 5 sheng = 25 sheng

# Coefficients for the equations
# Equation 1: 5上禾 - 7下禾 = 11
# Equation 2: 7上禾 - 5下禾 = 25
上禾1, 下禾1, 常數1 = 5, -7, 11
上禾2, 下禾2, 常數2 = 7, -5, 25

# Solve using elimination
# Multiply the first equation by 7 and the second equation by 5 to align coefficients of 上禾
eq1_multiplied = (7 * 上禾1, 7 * 下禾1, 7 * 常數1)  # (35, -49, 77)
eq2_multiplied = (5 * 上禾2, 5 * 下禾2, 5 * 常數2)  # (35, -25, 125)

# Subtract the first equation from the second to eliminate 上禾
_, 下禾_coeff, 常數_diff = (
    eq2_multiplied[1] - eq1_multiplied[1],
    eq2_multiplied[2] - eq1_multiplied[2],
)  # (-25 - (-49), 125 - 77) = (24, 48)

# Solve for 下禾
下禾實 = Fraction(常數_diff, 下禾_coeff)  # 下禾 = 48 / 24 = 2 sheng

# Substitute 下禾實 back into the first equation to solve for 上禾
上禾實 = Fraction(常數1 - 下禾1 * 下禾實, 上禾1)  # 上禾 = (11 - (-7 * 2)) / 5 = 5 sheng

# Final results
a = 上禾實  # 上禾一秉 yields a sheng
b = 下禾實  # 下禾一秉 yields b sheng#----- content ends here -----

"""
Code error: not enough values to unpack (expected 3, got 2)"""
