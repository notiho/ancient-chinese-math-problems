"""
今有上禾五秉損實一斗一升當下禾七秉上禾七秉損實二斗五升當下禾五秉問上下禾實一秉各幾何
術曰如方程置上禾五秉正下禾七秉負損實一斗一升正次置上禾七秉正下禾五秉負損實二斗五升正以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
荅曰上禾一秉 a升 下禾一秉 b升 
"""

#----- content starts here -----
"""
Suppose there are 5 bundles of upper millet, with a loss of 1 dou and 1 sheng when compared to the lower millet of 7 bundles.
Then, there are 7 bundles of upper millet, with a loss of 2 dou and 5 sheng when compared to the lower millet of 5 bundles.
Question: how much does one bundle of upper millet and one bundle of lower millet yield?

The procedure says: Treat it as a system of linear equations.
Place 5 bundles of upper millet as positive, 7 bundles of lower millet as negative, and the loss of 1 dou and 1 sheng as positive.
Next, place 7 bundles of upper millet as positive, 5 bundles of lower millet as negative, and the loss of 2 dou and 5 sheng as positive.
Use the positive-negative method to solve.

The method for solving linear equations says: Place the coefficients of the upper millet, middle millet, and lower millet on the left side, and the total yield on the right side.
For the middle millet, multiply the upper millet row by the middle millet coefficient, and divide by the diagonal coefficient.
Repeat for the next row.
For the lower millet, multiply the middle millet row by the lower millet coefficient, and divide by the diagonal coefficient.
The remainder gives the yield of the lower millet.
For the middle millet, use the coefficient of the middle millet to calculate its yield.
For the upper millet, use the coefficient of the upper millet to calculate its yield.
Each yield is calculated according to the method, obtaining the result.

Answer: one bundle of upper millet yields *a* sheng, and one bundle of lower millet yields *b* sheng.
"""

# Convert dou and sheng to sheng (1 dou = 10 sheng)
損實1 = 1 * 10 + 1  # 1斗1升 = 11升
損實2 = 2 * 10 + 5  # 2斗5升 = 25升

# Coefficients for the equations
上禾1 = 5
下禾1 = -7
上禾2 = 7
下禾2 = -5

# Solve using elimination
# Multiply the first equation by 7 (coefficient of 上禾2) and the second equation by 5 (coefficient of 上禾1)
eq1 = (上禾1 * 7, 下禾1 * 7, 損實1 * 7)  # 35上禾 - 49下禾 = 77
eq2 = (上禾2 * 5, 下禾2 * 5, 損實2 * 5)  # 35上禾 - 25下禾 = 125

# Subtract eq1 from eq2 to eliminate 上禾
下禾系數 = eq2[1] - eq1[1]  # -25下禾 - (-49下禾) = 24下禾
損實差 = eq2[2] - eq1[2]  # 125 - 77 = 48
下禾實 = Fraction(損實差, 下禾系數)  # 下禾 = 48 / 24 = 2升

# Substitute 下禾實 back into the first equation to solve for 上禾
上禾系數 = eq1[0]  # 35上禾
損實調整 = eq1[2] - (eq1[1] * 下禾實)  # 損實1調整 = 77 - (-49 * 2) = 77 + 98 = 175
上禾實 = Fraction(損實調整, 上禾系數)  # 上禾 = 175 / 35 = 5升

# Convert results to a and b
a = 上禾實  # 上禾一秉 = 5升
b = 下禾實  # 下禾一秉 = 2升#----- content ends here -----

"""
"""
