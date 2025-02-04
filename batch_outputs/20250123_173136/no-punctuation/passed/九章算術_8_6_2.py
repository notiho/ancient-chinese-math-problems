"""
今有牛五羊二直金十兩牛二羊五直金八兩問牛羊各直金幾何
術曰如方程
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
荅曰牛一直金 a兩 羊一直金 b兩 
"""

"""
Suppose there are 5 oxen and 2 sheep, worth 10 liang of gold.
And 2 oxen and 5 sheep, worth 8 liang of gold.
Question: how much is each ox and each sheep worth in gold?

The procedure says: This is solved using the method of simultaneous equations.

The method of simultaneous equations says:
1. Place the coefficients of the unknowns (oxen and sheep) in rows, and the constants (gold values) on the right-hand side.
2. Use elimination to reduce the system to a simpler form, solving for one variable at a time.
3. Substitute back to find the values of the unknowns.

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

# Eliminate one variable (羊) using the equations
# Multiply the first equation by 5 and the second by 2 to align the coefficients of 羊
eq1 = 5 * 牛1 + 5 * 羊1 - 5 * 金1  # 25牛 + 10羊 = 50
eq2 = 2 * 牛2 + 2 * 羊2 - 2 * 金2  # 4牛 + 10羊 = 16

# Subtract the second equation from the first to eliminate 羊
eliminated_eq = (25 * 牛1 - 4 * 牛2) - (50 - 16)  # 21牛 = 34
牛_value = Fraction(34, 21)

# Substitute 牛_value back into the first equation to solve for 羊
羊_value = Fraction(金1 - 牛1 * 牛_value, 羊1)

# Results
a = 牛_value
b = 羊_value
"""
"""
