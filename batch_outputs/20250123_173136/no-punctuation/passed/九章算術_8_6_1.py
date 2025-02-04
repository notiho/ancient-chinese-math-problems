"""
今有牛五羊二直金十兩牛二羊五直金八兩問牛羊各直金幾何
術曰如方程
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
荅曰牛一直金 a兩 羊一直金 b兩 
"""

"""
Suppose there are 5 oxen and 2 sheep worth 10 liang of gold, and 2 oxen and 5 sheep worth 8 liang of gold.
Question: how much is each ox and each sheep worth in gold?

The procedure says: This is solved using the method of simultaneous equations (方程).

The method of simultaneous equations says:
1. Place the coefficients of the first equation (upper row), the second equation (middle row), and the third equation (lower row) in order.
2. Place the constants (results) on the right-hand side.
3. Use elimination to solve for each variable step by step, starting from the bottom row and working upwards.
4. Substitute back to find the values of the variables.

Answer: Each ox is worth *a* liang of gold, and each sheep is worth *b* liang of gold.
"""

# 牛五羊二直金十兩 (5x + 2y = 10)
牛1 = 5
羊1 = 2
金1 = 10

# 牛二羊五直金八兩 (2x + 5y = 8)
牛2 = 2
羊2 = 5
金2 = 8

# Step 1: Eliminate one variable (e.g., 牛)
# Multiply the first equation by 2 and the second equation by 5 to align 牛 coefficients
牛1_調整 = 2 * 牛1
羊1_調整 = 2 * 羊1
金1_調整 = 2 * 金1

牛2_調整 = 5 * 牛2
羊2_調整 = 5 * 羊2
金2_調整 = 5 * 金2

# Subtract the adjusted equations to eliminate 牛
羊_消去 = 羊1_調整 - 羊2_調整
金_消去 = 金1_調整 - 金2_調整

# Solve for 羊 (y)
b = Fraction(金_消去, 羊_消去)

# Step 2: Substitute 羊 (y) back into one of the original equations to solve for 牛 (x)
金_代入 = 金1 - 羊1 * b
a = Fraction(金_代入, 牛1)

# Results
a, b  # 牛 (x) and 羊 (y) values in liang of gold
"""
"""
