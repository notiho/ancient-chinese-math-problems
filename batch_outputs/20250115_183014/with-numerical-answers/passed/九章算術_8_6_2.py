"""
今有牛五、羊二，直金十兩。牛二、羊五直金八兩。問︰牛羊各直金幾何？
術曰：如方程。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：牛 a(=1) ，直金 b(=34/21)兩 ，羊 c(=1) ，直金 d(=20/21)兩 。
"""

"""
Suppose there are 5 oxen and 2 sheep, worth a total of 10 liang of gold.
Additionally, 2 oxen and 5 sheep are worth a total of 8 liang of gold.
Question: how much is each ox and each sheep worth in gold?

The procedure says: solve it as a system of linear equations.

The procedure for solving systems of equations says: Place the coefficients of the variables (the "sheaves") in rows, with their totals on the right side. 
Perform elimination by multiplying rows and dividing by the pivot to simplify the system step by step.
Finally, solve for each variable by back-substitution.

Answer: Each ox is worth *a*(=1) unit, or *b*(=34/21) liang of gold, and each sheep is worth *c*(=1) unit, or *d*(=20/21) liang of gold.
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

# Step 1: Eliminate one variable (牛)
# Multiply the first equation by 2 and the second equation by 5 to align the coefficients of 牛
eq1_multiplied = (2 * 牛1, 2 * 羊1, 2 * 金1)  # (10, 4, 20)
eq2_multiplied = (5 * 牛2, 5 * 羊2, 5 * 金2)  # (10, 25, 40)

# Subtract the first equation from the second to eliminate 牛
羊_diff = eq2_multiplied[1] - eq1_multiplied[1]  # 25 - 4 = 21
金_diff = eq2_multiplied[2] - eq1_multiplied[2]  # 40 - 20 = 20

# Now we have a single equation for 羊:
# 21羊 = 20金
羊_value = Fraction(20, 21)  # Each sheep is worth 20/21 liang of gold

# Step 2: Solve for 牛 using the first equation
# Substitute 羊_value into the first equation
牛_value = Fraction(金1 - 羊1 * 羊_value, 牛1)  # (10 - 2 * (20/21)) / 5
牛_value = Fraction(34, 21)  # Each ox is worth 34/21 liang of gold

# Final results
a = 1  # 牛 unit
b = 牛_value  # 34/21 liang
c = 1  # 羊 unit
d = 羊_value  # 20/21 liang
"""
"""
