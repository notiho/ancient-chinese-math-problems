"""
今有牛五羊二直金十兩牛二羊五直金八兩問牛羊各直金幾何
術曰如方程
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
荅曰牛一直金 a兩 羊一直金 b兩 
"""

"""
Suppose there are 5 oxen and 2 sheep worth 10 liang of gold, and 2 oxen and 5 sheep worth 8 liang of gold.
Question: how much is each ox and each sheep worth in gold?

The procedure says: as in the method of simultaneous equations.

The method of simultaneous equations says:
1. Place the coefficients of the first equation (the upper row) as the upper terms, the second equation (the middle row) as the middle terms, and the third equation (the lower row) as the lower terms.
2. Place the constants of the equations on the right-hand side.
3. Multiply the upper row by the middle row and divide by the diagonal coefficient, then multiply by the next term and divide again by the diagonal coefficient.
4. For the middle row, multiply the remaining terms by the lower row and divide by the diagonal coefficient.
5. For the lower row, the remaining terms are divided by the diagonal coefficient.
6. Solve for the middle term by substituting back, and then solve for the upper term similarly.

Answer: Each ox is worth *a* liang of gold, and each sheep is worth *b* liang of gold.
"""

from fractions import Fraction

# 牛五羊二直金十兩
牛1 = 5
羊1 = 2
金1 = 10

# 牛二羊五直金八兩
牛2 = 2
羊2 = 5
金2 = 8

# Step 1: Eliminate one variable (羊)
# Multiply the first equation by 5 and the second equation by 2 to align the coefficients of 羊
eq1牛 = 5 * 牛1
eq1羊 = 5 * 羊1
eq1金 = 5 * 金1

eq2牛 = 2 * 牛2
eq2羊 = 2 * 羊2
eq2金 = 2 * 金2

# Subtract the second equation from the first to eliminate 羊
牛_coeff = eq1牛 - eq2牛
金_coeff = eq1金 - eq2金

# 牛_coeff now represents the coefficient for 牛
a = Fraction(金_coeff, 牛_coeff)

# Step 2: Solve for 羊 using one of the original equations
# Substitute the value of 牛 into the first equation
羊_coeff = 金1 - (牛1 * a)
b = Fraction(羊_coeff, 羊1)

# Final Answer
a = a  # 牛一直金 a兩
b = b  # 羊一直金 b兩
"""
"""
