"""
今有粟一十二萬八千九百四十斛九斗三合，出與人買絹一匹，直粟三斛五斗七升。問：絹幾何？
答曰： a匹 。
"""

#----- content starts here -----
"""
Suppose there is 128,940 hu, 9 dou, and 3 sheng of millet. It is used to buy silk, where 1 bolt of silk costs 3 hu, 5 dou, and 7 sheng of millet.
Question: how many bolts of silk can be bought?

Answer: *a* bolts of silk.
"""

from fractions import Fraction

# Convert all millet into sheng (smallest unit)
# 1 hu = 10 dou, 1 dou = 10 sheng
millet_total_sheng = (128940 * 10 * 10) + (9 * 10) + 3

# Convert the cost of 1 bolt of silk into sheng
cost_per_bolt_sheng = (3 * 10 * 10) + (5 * 10) + 7

# Calculate the number of bolts of silk that can be bought
a = millet_total_sheng // cost_per_bolt_sheng

# Output the result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 361179/10, Actual: 36117"""
