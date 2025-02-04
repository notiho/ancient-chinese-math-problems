"""
今有牛五、羊二，直金十兩。牛二、羊五直金八兩。問︰牛羊各直金幾何？
術曰：如方程。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：牛一，直金 a(=34/21)兩 ，羊一，直金 b(=20/21)兩 。
"""

"""
Suppose there are 5 oxen and 2 sheep, worth 10 liang of gold.
And 2 oxen and 5 sheep are worth 8 liang of gold.
Question: how much is each ox and each sheep worth in gold?

The procedure says: Solve using the method of simultaneous equations.

The method of simultaneous equations says:
Place the coefficients of the unknowns (oxen and sheep) in a matrix-like structure.
Perform row operations to simplify the equations step by step, dividing and eliminating terms to isolate the unknowns.
Finally, calculate the values of the unknowns based on the simplified equations.

Answer: Each ox is worth *a*(=34/21) liang of gold, and each sheep is worth *b*(=20/21) liang of gold.
"""

# 牛五、羊二，直金十兩
牛1 = 5
羊1 = 2
金1 = 10

# 牛二、羊五，直金八兩
牛2 = 2
羊2 = 5
金2 = 8

# 使用方程術解法
# Step 1: Eliminate one variable (e.g., 牛)
# Multiply the first equation by 牛2 and the second equation by 牛1
eq1 = [牛1 * 牛2, 羊1 * 牛2, 金1 * 牛2]  # [10, 4, 20]
eq2 = [牛2 * 牛1, 羊2 * 牛1, 金2 * 牛1]  # [10, 25, 40]

# Subtract eq1 from eq2 to eliminate 牛
羊系數 = eq2[1] - eq1[1]  # 25 - 4 = 21
金系數 = eq2[2] - eq1[2]  # 40 - 20 = 20

# Solve for 羊 (sheep)
羊價值 = Fraction(金系數, 羊系數)  # 20/21

# Substitute 羊價值 back into the first equation to solve for 牛 (ox)
牛價值 = Fraction(金1 - 羊1 * 羊價值, 牛1)  # (10 - 2 * (20/21)) / 5 = 34/21

# Final answers
a = 牛價值  # 34/21
b = 羊價值  # 20/21
"""
"""
