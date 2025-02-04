"""
今有牛五羊二直金十兩牛二羊五直金八兩問牛羊各直金幾何
術曰如方程
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
荅曰牛一直金 a兩 羊一直金 b兩 
"""

"""
Suppose there are 5 oxen and 2 sheep, worth a total of 10 liang of gold.
Additionally, 2 oxen and 5 sheep are worth a total of 8 liang of gold.
Question: how much is each ox and each sheep worth in gold?

The procedure says: This is solved using the method of simultaneous equations (方程).

The 方程術 (method of simultaneous equations) is as follows:
1. Place the coefficients of the unknowns (oxen and sheep) in rows, with the total values on the right.
2. Use elimination to simplify the system by multiplying rows and subtracting appropriately.
3. Solve for each unknown step by step, starting from the bottom row and working upwards.

Answer: Each ox is worth *a* liang of gold, and each sheep is worth *b* liang of gold.
"""

# 牛五羊二直金十兩
牛1 = 5
羊1 = 2
金1 = 10

# 牛二羊五直金八兩
牛2 = 2
羊2 = 5
金2 = 8

# Step 1: Eliminate one variable (羊)
# Multiply the first equation by 5 (羊2 coefficient) and the second equation by 2 (羊1 coefficient)
eq1 = (5 * 牛1, 5 * 羊1, 5 * 金1)  # 25牛 + 10羊 = 50
eq2 = (2 * 牛2, 2 * 羊2, 2 * 金2)  # 4牛 + 10羊 = 16

# Subtract the second equation from the first to eliminate 羊
牛_coeff = eq1[0] - eq2[0]  # 25牛 - 4牛 = 21牛
金_coeff = eq1[2] - eq2[2]  # 50 - 16 = 34
牛_value = Fraction(金_coeff, 牛_coeff)  # 牛 = 34 / 21

# Step 2: Solve for 羊 using one of the original equations
# Substitute 牛_value into the first equation: 5牛 + 2羊 = 10
羊_value = Fraction(金1 - (牛1 * 牛_value), 羊1)  # 羊 = (10 - 5 * (34 / 21)) / 2

# Final results
a = 牛_value
b = 羊_value
"""
"""
