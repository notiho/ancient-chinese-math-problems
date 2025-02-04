"""
今有牛五、羊二，直金十兩。牛二、羊五直金八兩。問︰牛羊各直金幾何？
術曰：如方程。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：牛一，直金 a(=34/21)兩 ，羊一，直金 b(=20/21)兩 。
"""

"""
Suppose there are 5 oxen and 2 sheep, worth 10 liang of gold.
Also, 2 oxen and 5 sheep are worth 8 liang of gold.
Question: how much is each ox and each sheep worth in gold?

The procedure says: Solve using the method of simultaneous equations ("方程").
The method of simultaneous equations says:
Place the coefficients of the unknowns (oxen and sheep) in rows, along with their totals on the right-hand side.
Perform elimination by multiplying rows and dividing by the coefficients to simplify the system.
Finally, solve for each unknown step by step.

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

# Eliminate one variable (e.g., 牛) using the method of simultaneous equations
# Multiply the first equation by 牛2 and the second equation by 牛1
eq1 = 牛2 * 牛1  # Coefficient for 牛 in the first equation
eq2 = 牛1 * 牛2  # Coefficient for 牛 in the second equation

# Adjust the equations
羊_eq1 = 牛2 * 羊1
羊_eq2 = 牛1 * 羊2
金_eq1 = 牛2 * 金1
金_eq2 = 牛1 * 金2

# Subtract the equations to eliminate 牛
羊_total = 羊_eq1 - 羊_eq2
金_total = 金_eq1 - 金_eq2

# Solve for 羊 (sheep's worth in gold)
b = Fraction(金_total, 羊_total)  # 羊一，直金 b(=20/21)兩

# Substitute 羊's value back into the first equation to solve for 牛
金_for_牛 = 金1 - (羊1 * b)
a = Fraction(金_for_牛, 牛1)  # 牛一，直金 a(=34/21)兩

# Final results
a, b  # 牛一，直金 34/21 兩；羊一，直金 20/21 兩
"""
"""
