"""
今有粟一十二萬八千九百四十斛九斗三合，出與人買絹一匹，直粟三斛五斗七升。問：絹幾何？
答曰： a匹 。
"""

#----- content starts here -----
"""
Suppose there are 128,940 hu, 9 dou, and 3 sheng of millet. It is used to buy silk, where each bolt of silk costs 3 hu, 5 dou, and 7 sheng of millet.
Question: how many bolts of silk can be bought?

Answer: *a* bolts.
"""

from fractions import Fraction

# Total millet in hu, dou, and sheng
total_millet_hu = 128940
total_millet_dou = 9
total_millet_sheng = 3

# Convert everything to sheng (1 hu = 10 dou, 1 dou = 10 sheng)
total_millet_in_sheng = (total_millet_hu * 10 * 10) + (total_millet_dou * 10) + total_millet_sheng

# Cost of one bolt of silk in hu, dou, and sheng
cost_per_bolt_hu = 3
cost_per_bolt_dou = 5
cost_per_bolt_sheng = 7

# Convert cost of one bolt of silk to sheng
cost_per_bolt_in_sheng = (cost_per_bolt_hu * 10 * 10) + (cost_per_bolt_dou * 10) + cost_per_bolt_sheng

# Calculate the number of bolts of silk that can be bought
a = Fraction(total_millet_in_sheng, cost_per_bolt_in_sheng)

# Output the result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 361179/10, Actual: 4298031/119"""
