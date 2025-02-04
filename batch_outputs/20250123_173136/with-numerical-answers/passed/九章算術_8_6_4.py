"""
今有牛五、羊二，直金十兩。牛二、羊五直金八兩。問︰牛羊各直金幾何？
術曰：如方程。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：牛一，直金 a(=34/21)兩 ，羊一，直金 b(=20/21)兩 。
"""

"""
Suppose there are 5 oxen and 2 sheep, worth 10 liang of gold in total.
Additionally, 2 oxen and 5 sheep are worth 8 liang of gold in total.
Question: how much is each ox and each sheep worth in gold?

The procedure says: Solve this as a system of linear equations.

The method for solving systems of linear equations says:
Place the coefficients of the variables (oxen and sheep) into rows, with the total values on the right-hand side.
Perform row operations to eliminate variables step by step, dividing by the coefficients as needed.
Continue until each variable is isolated, and solve for their values.

Answer: Each ox is worth *a*(=34/21) liang of gold, and each sheep is worth *b*(=20/21) liang of gold.
"""

from fractions import Fraction

# 牛五、羊二，直金十兩
牛1 = 5
羊1 = 2
金1 = 10

# 牛二、羊五，直金八兩
牛2 = 2
羊2 = 5
金2 = 8

# Step 1: Eliminate one variable (e.g., 牛)
# Multiply the first equation by 牛2 and the second equation by 牛1
eq1_multiplier = 牛2
eq2_multiplier = 牛1

牛1_new = eq1_multiplier * 牛1
羊1_new = eq1_multiplier * 羊1
金1_new = eq1_multiplier * 金1

牛2_new = eq2_multiplier * 牛2
羊2_new = eq2_multiplier * 羊2
金2_new = eq2_multiplier * 金2

# Subtract the second equation from the first to eliminate 牛
羊_diff = 羊1_new - 羊2_new
金_diff = 金1_new - 金2_new

# Step 2: Solve for 羊
羊_value = Fraction(金_diff, 羊_diff)  # b = 20/21

# Step 3: Substitute 羊_value back into one of the original equations to solve for 牛
金_remaining = 金1 - 羊1 * 羊_value
牛_value = Fraction(金_remaining, 牛1)  # a = 34/21

# Final results
a = 牛_value  # 34/21
b = 羊_value  # 20/21
"""
"""
