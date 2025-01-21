"""
今有粟一十二萬八千九百四十斛九斗三合，出與人買絹一匹，直粟三斛五斗七升。問：絹幾何？
答曰： a匹 b丈 。
"""

"""
Suppose there are 128,940 hu, 9 dou, and 3 sheng of millet. It is used to buy silk, where each bolt of silk costs 3 hu, 5 dou, and 7 sheng of millet.
Question: how many bolts of silk and how much leftover silk (in zhang) can be obtained?

Answer: *a* bolts and *b* zhang.
"""

from fractions import Fraction

# Total millet in hu
total_millet = 128940 + Fraction(9, 10) + Fraction(3, 100)

# Cost of one bolt of silk in hu
cost_per_bolt = 3 + Fraction(5, 10) + Fraction(7, 100)

# Calculate the number of bolts of silk
a = total_millet // cost_per_bolt

# Calculate the leftover millet
leftover_millet = total_millet % cost_per_bolt

# Convert leftover millet into zhang of silk
b = leftover_millet / cost_per_bolt

# Final result
a, b
"""
Variable 'b' has wrong value. Expected: 18/5, Actual: 108/119"""
