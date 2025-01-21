"""
今有粟一十二萬八千九百四十斛九斗三合，出與人買絹一匹，直粟三斛五斗七升。問：絹幾何？
答曰： a匹 b丈 。
"""

"""
Suppose there are 128,940 hu, 9 dou, and 3 sheng of millet. It is used to buy silk, where 1 bolt of silk costs 3 hu, 5 dou, and 7 sheng of millet.
Question: how many bolts of silk and how much leftover silk (in zhang) can be purchased?

Answer: *a* bolts and *b* zhang.
"""

from fractions import Fraction

# Total millet in hu, dou, and sheng
total_millet_hu = 128940
total_millet_dou = 9
total_millet_sheng = 3

# Convert everything to sheng (1 hu = 10 dou, 1 dou = 10 sheng)
total_millet_in_sheng = (total_millet_hu * 10 * 10) + (total_millet_dou * 10) + total_millet_sheng

# Cost of 1 bolt of silk in hu, dou, and sheng
cost_per_bolt_hu = 3
cost_per_bolt_dou = 5
cost_per_bolt_sheng = 7

# Convert cost per bolt to sheng
cost_per_bolt_in_sheng = (cost_per_bolt_hu * 10 * 10) + (cost_per_bolt_dou * 10) + cost_per_bolt_sheng

# Calculate the number of full bolts of silk that can be purchased
a = total_millet_in_sheng // cost_per_bolt_in_sheng

# Calculate the remaining millet in sheng
remaining_millet_in_sheng = total_millet_in_sheng % cost_per_bolt_in_sheng

# Convert the remaining millet to zhang (1 zhang = 1/10 of a bolt)
b = Fraction(remaining_millet_in_sheng, cost_per_bolt_in_sheng)

# Final result
a, b
"""
Variable 'b' has wrong value. Expected: 18/5, Actual: 108/119"""
