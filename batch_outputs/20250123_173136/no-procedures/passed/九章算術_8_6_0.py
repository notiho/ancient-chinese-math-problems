"""
今有牛五、羊二，直金十兩。牛二、羊五直金八兩。問︰牛羊各直金幾何？
荅曰：牛一，直金 a兩 ，羊一，直金 b兩 。
"""

"""
Suppose there are 5 cows and 2 sheep worth a total of 10 liang of gold.
And 2 cows and 5 sheep are worth a total of 8 liang of gold.
Question: how much is one cow and one sheep worth respectively?

Answer: one cow is worth *a* liang of gold, and one sheep is worth *b* liang of gold.
"""

# Represent the equations:
# 5牛 + 2羊 = 10
# 2牛 + 5羊 = 8

from fractions import Fraction

# Let 牛 = x (value of one cow) and 羊 = y (value of one sheep)
# Solve the system of linear equations using substitution or elimination

# Multiply the first equation by 5 and the second equation by 2 to align coefficients of 羊:
# 25牛 + 10羊 = 50
# 4牛 + 10羊 = 16

# Subtract the second equation from the first:
# (25牛 - 4牛) + (10羊 - 10羊) = 50 - 16
# 21牛 = 34
# 牛 = 34 / 21

a = Fraction(34, 21)  # Value of one cow

# Substitute 牛 = 34/21 into the first equation to solve for 羊:
# 5牛 + 2羊 = 10
# 5(34/21) + 2羊 = 10
# 170/21 + 2羊 = 10
# 2羊 = 10 - 170/21
# 2羊 = 210/21 - 170/21
# 2羊 = 40/21
# 羊 = 40 / (21 * 2)

b = Fraction(40, 42)  # Value of one sheep, simplified to 20/21

# Final results:
# 牛 = a = 34/21
# 羊 = b = 20/21
"""
"""
