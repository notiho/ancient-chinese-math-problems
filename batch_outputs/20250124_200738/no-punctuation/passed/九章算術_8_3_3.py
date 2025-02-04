"""
今有上禾五秉損實一斗一升當下禾七秉上禾七秉損實二斗五升當下禾五秉問上下禾實一秉各幾何
術曰如方程置上禾五秉正下禾七秉負損實一斗一升正次置上禾七秉正下禾五秉負損實二斗五升正以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
荅曰上禾一秉 a升 下禾一秉 b升 
"""

#----- content starts here -----
"""
Suppose there are 5 bundles of upper millet, with a loss of 1 dou and 1 sheng. 
This corresponds to 7 bundles of lower millet.
Similarly, there are 7 bundles of upper millet, with a loss of 2 dou and 5 sheng. 
This corresponds to 5 bundles of lower millet.
Question: how much does one bundle of upper millet and one bundle of lower millet yield respectively?

The procedure says: Treat this as a system of linear equations.
Place 5 bundles of upper millet as positive, 7 bundles of lower millet as negative, and the loss of 1 dou and 1 sheng as positive.
Next, place 7 bundles of upper millet as positive, 5 bundles of lower millet as negative, and the loss of 2 dou and 5 sheng as positive.
Use the positive-negative method to solve.

The method for solving systems of equations says:
Place the coefficients of the upper millet, middle millet, and lower millet on the left, and the total yield on the right.
For the middle millet, multiply the first row by the second row's coefficient of the upper millet, and divide by the diagonal coefficient.
Repeat for the second row, and eliminate terms systematically.
Finally, solve for the unknowns by back-substitution.

Answer: one bundle of upper millet yields *a* sheng, and one bundle of lower millet yields *b* sheng.
"""

# Convert dou and sheng to sheng (1 dou = 10 sheng)
損實1 = 1 * 10 + 1  # 1斗1升 = 11升
損實2 = 2 * 10 + 5  # 2斗5升 = 25升

# Coefficients from the problem
上禾1 = 5  # First equation: 5 bundles of upper millet
下禾1 = -7  # First equation: -7 bundles of lower millet
上禾2 = 7  # Second equation: 7 bundles of upper millet
下禾2 = -5  # Second equation: -5 bundles of lower millet

# Solve using elimination
# Multiply first equation by 7 (coefficient of 上禾 in second equation)
# Multiply second equation by 5 (coefficient of 上禾 in first equation)
eq1_scaled = (上禾1 * 7, 下禾1 * 7, 損實1 * 7)  # (35, -49, 77)
eq2_scaled = (上禾2 * 5, 下禾2 * 5, 損實2 * 5)  # (35, -25, 125)

# Subtract the first scaled equation from the second scaled equation
# This eliminates 上禾
下禾_coeff = eq2_scaled[1] - eq1_scaled[1]  # -25 - (-49) = 24
損實_diff = eq2_scaled[2] - eq1_scaled[2]  # 125 - 77 = 48

# Solve for 下禾 (one bundle of lower millet)
b = Fraction(損實_diff, 下禾_coeff)  # b = 48 / 24 = 2升

# Substitute b back into the first equation to solve for 上禾
損實1_adjusted = 損實1 - (下禾1 * b)  # 11 - (-7 * 2) = 11 + 14 = 25
a = Fraction(損實1_adjusted, 上禾1)  # a = 25 / 5 = 5升

# Final results
a = Fraction(5)  # Upper millet yield per bundle
b = Fraction(2)  # Lower millet yield per bundle#----- content ends here -----

"""
"""
