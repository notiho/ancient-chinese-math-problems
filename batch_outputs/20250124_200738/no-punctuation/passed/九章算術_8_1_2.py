"""
今有上禾七秉損實一斗益之下禾二秉而實一十斗下禾八秉益實一斗與上禾二秉而實一十斗問上下禾實一秉各幾何
術曰如方程損之曰益益之曰損損實一斗者其實過一十斗也益實一斗者其實不滿一十斗也
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
荅曰上禾一秉實 a斗 下禾一秉實 b斗 
"""

#----- content starts here -----
"""
Suppose there are 7 bundles of upper millet, which lose 1 dou of yield, and add it to 2 bundles of lower millet, resulting in 10 dou of yield.
Then, there are 8 bundles of lower millet, which gain 1 dou of yield, and add it to 2 bundles of upper millet, resulting in 10 dou of yield.
Question: what is the yield per bundle of upper millet and lower millet?

The procedure says: Treat it like a system of equations.
"Loss" means subtract, and "gain" means add.
Losing 1 dou means its yield exceeds 10 dou.
Gaining 1 dou means its yield is less than 10 dou.

The method for solving systems of equations says:
Place 3 bundles of upper millet, 2 bundles of middle millet, and 1 bundle of lower millet, with a total yield of 39 dou, on the right side.
Arrange the millet types on the left side, as on the right side.
For the right row, multiply the upper millet throughout the middle row, then divide directly.
Also multiply the next row and divide directly.
For the middle row, if the middle millet is not exhausted, multiply it throughout the left row, then divide directly.
For the left row, if the lower millet is not exhausted, use the upper as the divisor and the lower as the dividend.
The result is the yield of the lower millet.
To find the middle millet, multiply the middle row by the divisor, then divide by the lower millet's yield.
The remainder corresponds to the middle millet's bundles, plus one, which gives the middle millet's yield.
To find the upper millet, multiply the right row by the divisor, then divide by the lower and middle millet's yields.
The remainder corresponds to the upper millet's bundles, plus one, which gives the upper millet's yield.
The results are all calculated as described, and each yields 1 dou.

Answer: the yield per bundle of upper millet is *a* dou, and the yield per bundle of lower millet is *b* dou.
"""

# Define the problem as a system of equations:
# Let x = yield per bundle of upper millet (in dou)
# Let y = yield per bundle of lower millet (in dou)

# Equation 1: 7x - 1 + 2y = 10
# Equation 2: 8y + 1 + 2x = 10

# Rewrite the equations:
# 7x + 2y = 11  (from Equation 1)
# 2x + 8y = 9   (from Equation 2)

# Solve using the method described in the procedure.

# Step 1: Multiply the first equation by 8 (coefficient of y in the second equation),
# and the second equation by 2 (coefficient of y in the first equation), to align the y terms.
eq1 = [7 * 8, 2 * 8, 11 * 8]  # 56x + 16y = 88
eq2 = [2 * 2, 8 * 2, 9 * 2]   # 4x + 16y = 18

# Step 2: Subtract the second equation from the first to eliminate y.
# (56x + 16y) - (4x + 16y) = 88 - 18
x_coefficient = eq1[0] - eq2[0]  # 56 - 4 = 52
y_coefficient = eq1[1] - eq2[1]  # 16 - 16 = 0
constant = eq1[2] - eq2[2]       # 88 - 18 = 70

# This simplifies to:
# 52x = 70
# Solve for x:
x = Fraction(70, 52)

# Simplify x:
x = x.limit_denominator()  # x = 35/26

# Step 3: Substitute x back into one of the original equations to solve for y.
# Use the first equation: 7x + 2y = 11
# 7(35/26) + 2y = 11
lhs = 7 * x  # 7 * (35/26) = 245/26
rhs = 11
remaining = rhs - lhs  # 11 - (245/26) = (286/26) - (245/26) = 41/26
y = Fraction(41, 26) / 2  # y = (41/26) / 2 = 41/52

# Simplify y:
y = y.limit_denominator()  # y = 41/52

# Final results:
a = x  # Yield per bundle of upper millet
b = y  # Yield per bundle of lower millet#----- content ends here -----

"""
"""
