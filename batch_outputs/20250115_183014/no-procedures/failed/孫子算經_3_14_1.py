"""
今有粟一十二萬八千九百四十斛九斗三合，出與人買絹一匹，直粟三斛五斗七升。問：絹幾何？
答曰： a匹 b丈 。
"""

"""
Suppose there are 128,940 hu, 9 dou, and 3 sheng of millet. It is used to buy silk, where 1 bolt of silk costs 3 hu, 5 dou, and 7 sheng of millet.
Question: how many bolts of silk and how much leftover silk (in zhang) can be obtained?

Answer: *a* bolts and *b* zhang.
"""

from fractions import Fraction

# Total millet in hu, converted to the smallest unit (sheng)
total_millet_in_sheng = (
    128940 * 10 * 10  # Convert hu to sheng
    + 9 * 10          # Convert dou to sheng
    + 3               # Add sheng
)

# Cost of 1 bolt of silk in millet, converted to sheng
cost_per_bolt_in_sheng = (
    3 * 10 * 10  # Convert hu to sheng
    + 5 * 10     # Convert dou to sheng
    + 7          # Add sheng
)

# Calculate the number of full bolts of silk
a = total_millet_in_sheng // cost_per_bolt_in_sheng

# Calculate the leftover millet in sheng
leftover_millet_in_sheng = total_millet_in_sheng % cost_per_bolt_in_sheng

# Convert leftover millet to zhang (1 bolt = 10 zhang)
b = Fraction(leftover_millet_in_sheng, cost_per_bolt_in_sheng) * 10

# Final result
a, b
"""
Variable 'b' has wrong value. Expected: 18/5, Actual: 1080/119"""
